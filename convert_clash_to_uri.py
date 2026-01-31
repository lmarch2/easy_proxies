#!/usr/bin/env python3
"""
Convert Clash YAML proxy nodes to sing-box URI format
"""
import yaml
import base64
import urllib.parse
import sys
from typing import Dict, Any


def convert_vless_to_uri(node: Dict[str, Any]) -> str:
    """Convert VLESS Clash node to URI"""
    name = node.get('name', 'unnamed')
    server = node['server']
    port = node['port']
    uuid = node['uuid']
    
    # Base URI
    uri = f"vless://{uuid}@{server}:{port}"
    
    # Query parameters
    params = {}
    
    # Security/TLS
    if node.get('tls'):
        params['security'] = 'tls'
        if node.get('skip-cert-verify'):
            params['allowInsecure'] = '1'
        if node.get('servername'):
            params['sni'] = node['servername']
        if node.get('client-fingerprint'):
            params['fp'] = node['client-fingerprint']
    
    # Flow
    if node.get('flow'):
        params['flow'] = node['flow']
    
    # Transport
    network = node.get('network', 'tcp')
    params['type'] = network
    
    if network == 'ws':
        ws_opts = node.get('ws-opts', {})
        if ws_opts.get('path'):
            params['path'] = ws_opts['path']
        if ws_opts.get('headers', {}).get('Host'):
            params['host'] = ws_opts['headers']['Host']
    
    # Reality
    if node.get('reality-opts'):
        reality = node['reality-opts']
        params['security'] = 'reality'
        if reality.get('public-key'):
            params['pbk'] = reality['public-key']
        if reality.get('short-id'):
            params['sid'] = reality['short-id']
    
    # Build query string
    query = '&'.join(f"{k}={urllib.parse.quote(str(v))}" for k, v in params.items())
    
    # Add fragment (node name)
    fragment = urllib.parse.quote(name)
    
    return f"{uri}?{query}#{fragment}"


def convert_hysteria2_to_uri(node: Dict[str, Any]) -> str:
    """Convert Hysteria2 Clash node to URI"""
    name = node.get('name', 'unnamed')
    server = node['server']
    port = node['port']
    password = node['password']
    
    # Base URI
    uri = f"hysteria2://{password}@{server}:{port}"
    
    # Query parameters
    params = {}
    
    if node.get('sni'):
        params['sni'] = node['sni']
    
    if node.get('skip-cert-verify'):
        params['insecure'] = '1'
    
    # Build query string
    query = '&'.join(f"{k}={urllib.parse.quote(str(v))}" for k, v in params.items())
    
    # Add fragment (node name)
    fragment = urllib.parse.quote(name)
    
    if query:
        return f"{uri}?{query}#{fragment}"
    else:
        return f"{uri}#{fragment}"


def convert_node(node: Dict[str, Any]) -> str | None:
    """Convert a Clash node to URI format"""
    node_type = node.get('type', '').lower()
    
    if node_type == 'vless':
        return convert_vless_to_uri(node)
    elif node_type == 'hysteria2':
        return convert_hysteria2_to_uri(node)
    else:
        print(f"Warning: Unsupported type '{node_type}' for node: {node.get('name')}", file=sys.stderr)
        return None


def main():
    # Read Clash YAML
    with open('clash_nodes.yaml', 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    proxies = data.get('proxies', [])
    
    # Convert to URIs
    uris = []
    for node in proxies:
        uri = convert_node(node)
        if uri:
            uris.append(uri)
    
    # Write to nodes.txt
    with open('nodes.txt', 'w', encoding='utf-8') as f:
        for uri in uris:
            f.write(uri + '\n')
    
    print(f"✓ Converted {len(uris)} nodes to nodes.txt")


if __name__ == '__main__':
    main()
