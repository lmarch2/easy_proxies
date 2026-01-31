#!/usr/bin/env python3
import urllib.parse
import base64
import json

nodes = [
    {"name": "剩余流量：999.51 GB", "type": "vless", "server": "unamecf.xn--ghqu5fm27b67w.com", "port": 443, "uuid": "b962a7cf-2963-4c00-9fc8-931d649d6178", "tls": True, "servername": "ujp1.xn--ghqu5fm27b67w.com", "network": "ws", "ws_path": "/pq/jp1", "ws_host": "ujp1.xn--ghqu5fm27b67w.com"},
    {"name": "套餐到期：长期有效", "type": "vless", "server": "unamecf.xn--ghqu5fm27b67w.com", "port": 443, "uuid": "b962a7cf-2963-4c00-9fc8-931d649d6178", "tls": True, "servername": "ujp1.xn--ghqu5fm27b67w.com", "network": "ws", "ws_path": "/pq/jp1", "ws_host": "ujp1.xn--ghqu5fm27b67w.com"},
    {"name": "🇯🇵日本东京01 | 电信联通推荐", "type": "vless", "server": "unamecf.xn--ghqu5fm27b67w.com", "port": 443, "uuid": "b962a7cf-2963-4c00-9fc8-931d649d6178", "tls": True, "servername": "ujp1.xn--ghqu5fm27b67w.com", "network": "ws", "ws_path": "/pq/jp1", "ws_host": "ujp1.xn--ghqu5fm27b67w.com"},
    {"name": "🇯🇵日本东京02 | 电信联通推荐", "type": "vless", "server": "unamecf.xn--ghqu5fm27b67w.com", "port": 443, "uuid": "b962a7cf-2963-4c00-9fc8-931d649d6178", "tls": True, "servername": "ujp2.xn--ghqu5fm27b67w.com", "network": "ws", "ws_path": "/pq/jp2", "ws_host": "ujp2.xn--ghqu5fm27b67w.com"},
    {"name": "🇯🇵日本东京03 | 电信联通推荐", "type": "vless", "server": "unamecf.xn--ghqu5fm27b67w.com", "port": 443, "uuid": "b962a7cf-2963-4c00-9fc8-931d649d6178", "tls": True, "servername": "ujp3.xn--ghqu5fm27b67w.com", "network": "ws", "ws_path": "/pq/jp3", "ws_host": "ujp3.xn--ghqu5fm27b67w.com"},
    {"name": "🇯🇵日本东京04 | 电信联通推荐", "type": "vless", "server": "unamecf.xn--ghqu5fm27b67w.com", "port": 443, "uuid": "b962a7cf-2963-4c00-9fc8-931d649d6178", "tls": True, "servername": "ujp4.xn--ghqu5fm27b67w.com", "network": "ws", "ws_path": "/pq/jp4", "ws_host": "ujp4.xn--ghqu5fm27b67w.com"},
    {"name": "🇯🇵日本东京05 | 电信联通推荐", "type": "vless", "server": "unamecf.xn--ghqu5fm27b67w.com", "port": 443, "uuid": "b962a7cf-2963-4c00-9fc8-931d649d6178", "tls": True, "servername": "ujp5.xn--ghqu5fm27b67w.com", "network": "ws", "ws_path": "/pq/jp5", "ws_host": "ujp5.xn--ghqu5fm27b67w.com"},
    {"name": "🇯🇵日本东京06 | 高速专线推荐", "type": "vless", "server": "104.18.125.69", "port": 443, "uuid": "b962a7cf-2963-4c00-9fc8-931d649d6178", "tls": True, "servername": "ujp2.xn--ghqu5fm27b67w.com", "network": "ws", "ws_path": "/pq/jp2", "ws_host": "ujp2.xn--ghqu5fm27b67w.com"},
    {"name": "🇯🇵日本东京07 | 高速专线推荐", "type": "vless", "server": "104.18.125.69", "port": 443, "uuid": "b962a7cf-2963-4c00-9fc8-931d649d6178", "tls": True, "servername": "ujp3.xn--ghqu5fm27b67w.com", "network": "ws", "ws_path": "/pq/jp3", "ws_host": "ujp3.xn--ghqu5fm27b67w.com"},
    {"name": "🇯🇵日本东京08 | 高速专线推荐", "type": "vless", "server": "104.18.125.69", "port": 443, "uuid": "b962a7cf-2963-4c00-9fc8-931d649d6178", "tls": True, "servername": "ujp4.xn--ghqu5fm27b67w.com", "network": "ws", "ws_path": "/pq/jp4", "ws_host": "ujp4.xn--ghqu5fm27b67w.com"},
    {"name": "🇯🇵日本东京09 | 高速专线推荐", "type": "vless", "server": "104.18.125.69", "port": 443, "uuid": "b962a7cf-2963-4c00-9fc8-931d649d6178", "tls": True, "servername": "ujp5.xn--ghqu5fm27b67w.com", "network": "ws", "ws_path": "/pq/jp5", "ws_host": "ujp5.xn--ghqu5fm27b67w.com"},
    {"name": "🇸🇬新加坡01 | 电信联通推荐", "type": "vless", "server": "104.18.46.50", "port": 443, "uuid": "b962a7cf-2963-4c00-9fc8-931d649d6178", "tls": True, "servername": "sgp1.pqvip.top", "network": "ws", "ws_path": "/pq/sg1", "ws_host": "sgp1.pqvip.top"},
    {"name": "🇸🇬新加坡02 | 电信联通推荐", "type": "vless", "server": "104.18.46.50", "port": 443, "uuid": "b962a7cf-2963-4c00-9fc8-931d649d6178", "tls": True, "servername": "sgp1.pqvip.top", "network": "ws", "ws_path": "/pq/sg1", "ws_host": "sgp1.pqvip.top"},
]

reality_nodes = [
    {"name": "🇯🇵日本东京01-0.1倍 | 电信联通推荐", "server": "pq.vmjp.yydjc.top", "port": 443, "uuid": "b962a7cf-2963-4c00-9fc8-931d649d6178", "flow": "xtls-rprx-vision", "sni": "iosapps.itunes.apple.com", "pbk": "ybBxu1pW3O9Me954LCDfXgHW6lIYepAbnla82yaZ5HE", "sid": "6a1faecb"},
    {"name": "🇯🇵日本东京02-0.1倍 | 电信联通推荐", "server": "pq.vmjp2.yydjc.top", "port": 443, "uuid": "b962a7cf-2963-4c00-9fc8-931d649d6178", "flow": "xtls-rprx-vision", "sni": "cdn-dynmedia-1.microsoft.com", "pbk": "asLJREsp9L0JbURQPIhFxc6bZIgpunEOjOJeHv3YcEs", "sid": "b0fbe0f0"},
    {"name": "🇯🇵日本东京03-0.1倍 | 电信联通推荐", "server": "pq.vmjp3.yydjc.top", "port": 443, "uuid": "b962a7cf-2963-4c00-9fc8-931d649d6178", "flow": "xtls-rprx-vision", "sni": "iosapps.itunes.apple.com", "pbk": "pR8CV43xvSgvzSXPVLCVomjw-yZvNyqU32kietO2pEc", "sid": "a6115a2c"},
    {"name": "🇯🇵日本东京04-0.1倍 | 电信联通推荐", "server": "pq.vmjp4.yydjc.top", "port": 443, "uuid": "b962a7cf-2963-4c00-9fc8-931d649d6178", "flow": "xtls-rprx-vision", "sni": "cdn-dynmedia-1.microsoft.com", "pbk": "FrLhPuCVfzdM5rppzxHXQ5BZSGf1YHrXgo-cCtecGSo", "sid": "f3b38af2"},
    {"name": "🇯🇵日本东京05-0.1倍 | 电信联通推荐", "server": "pq.vmjp5.yydjc.top", "port": 443, "uuid": "b962a7cf-2963-4c00-9fc8-931d649d6178", "flow": "xtls-rprx-vision", "sni": "cdn-dynmedia-1.microsoft.com", "pbk": "FrLhPuCVfzdM5rppzxHXQ5BZSGf1YHrXgo-cCtecGSo", "sid": "f3b38af2"},
]

hk_ws_nodes = [
    ("🇭🇰香港01-0.1倍", "104.18.126.50", "hk1p1.pqvip.top", "/pq/hk1"),
    ("🇭🇰香港02-0.1倍", "104.18.126.50", "hk2p1.pqvip.top", "/pq/hk2"),
    ("🇭🇰香港03-0.1倍", "104.18.126.50", "hk3p1.pqvip.top", "/pq/hk3"),
    ("🇭🇰香港04-0.1倍", "104.18.126.50", "hk4p1.pqvip.top", "/pq/hk4"),
    ("🇭🇰香港05-0.1倍", "104.18.126.50", "hk5p1.pqvip.top", "/pq/hk5"),
    ("🇭🇰香港06-0.1倍", "104.18.126.50", "hk6p1.pqvip.top", "/pq/hk6"),
    ("🇭🇰香港07-0.1倍", "104.18.126.50", "hk7p1.pqvip.top", "/pq/hk7"),
    ("🇭🇰香港08-0.1倍", "104.18.126.50", "hk8p1.pqvip.top", "/pq/hk8"),
]

sg_reality_nodes = [
    {"name": "🇸🇬AWS新加坡01 | 移动联通推荐", "server": "pq.aws63.yydjc.top", "pbk": "mnshlVo5tkzYbmEB9xrgmUHwYETnXLAjjlGAssqaDGI", "sid": "436299c6"},
    {"name": "🇸🇬AWS新加坡02 | 移动联通推荐", "server": "pq.aws64.yydjc.top", "pbk": "xjWkdgeetCnB1-kHqwVnAaSUqg4qK9TFWQlamW8FSRI", "sid": "e2e15173"},
    {"name": "🇸🇬AWS新加坡03 | 移动联通推荐", "server": "pq.aws65.yydjc.top", "pbk": "9076EbD5vM8kATc_08QvDiqZF5KHTM_LaSrMOvcwfHw", "sid": "57b7989c"},
]

us_hy2_nodes = [
    ("🇺🇸美国01-0.1倍 | 电信联通移动推荐", "pq.us1.globals-download.com", 443, "www.apple.com"),
    ("🇺🇸美国02-0.1倍 | 电信联通移动推荐", "pq.us2.globals-download.com", 443, "www.apple.com"),
    ("🇺🇸美国03-0.1倍 | 电信联通移动推荐", "pq.us3.globals-download.com", 443, "tv.apple.com"),
    ("🇺🇸美国04-0.1倍 | 电信联通移动推荐", "pq.us4.globals-download.com", 443, "www.apple.com"),
    ("🇺🇸美国05-0.1倍 | 电信联通移动推荐", "pq.us5.globals-download.com", 443, "www.apple.com"),
    ("🇺🇸美国06-0.1倍 | 电信联通移动推荐", "pq.us6.globals-download.com", 443, "www.apple.com"),
    ("🇺🇸美国07-0.1倍 | 电信联通移动推荐", "pq.us7.globals-download.com", 443, "www.apple.com"),
    ("🇺🇸美国08-0.1倍 | 电信联通移动推荐", "pq.us8.globals-download.com", 443, "www.apple.com"),
]

hk_hy2_nodes = [
    ("🇭🇰香港01 | 移动联通推荐", "103.197.71.112"),
    ("🇭🇰香港02 | 移动联通推荐", "103.197.71.113"),
    ("🇭🇰香港03 | 移动联通推荐", "103.197.71.114"),
]

lines = []

for node in nodes:
    params = {
        "security": "tls",
        "sni": node["servername"],
        "type": node["network"],
        "path": node["ws_path"],
        "host": node["ws_host"],
    }
    params_str = "&".join(f"{k}={urllib.parse.quote(str(v))}" for k, v in params.items())
    name_encoded = urllib.parse.quote(node["name"])
    uri = f"vless://{node['uuid']}@{node['server']}:{node['port']}?{params_str}#{name_encoded}"
    lines.append(uri)

for node in reality_nodes:
    params = {
        "security": "reality",
        "flow": node["flow"],
        "pbk": node["pbk"],
        "sid": node["sid"],
        "sni": node["sni"],
        "fp": "chrome",
        "type": "tcp",
    }
    params_str = "&".join(f"{k}={urllib.parse.quote(str(v))}" for k, v in params.items())
    name_encoded = urllib.parse.quote(node["name"])
    uri = f"vless://{node['uuid']}@{node['server']}:{node['port']}?{params_str}#{name_encoded}"
    lines.append(uri)

for name, server, sni, path in hk_ws_nodes:
    params = {
        "security": "tls",
        "sni": sni,
        "type": "ws",
        "path": path,
        "host": sni,
    }
    params_str = "&".join(f"{k}={urllib.parse.quote(str(v))}" for k, v in params.items())
    name_encoded = urllib.parse.quote(name)
    uri = f"vless://b962a7cf-2963-4c00-9fc8-931d649d6178@{server}:443?{params_str}#{name_encoded}"
    lines.append(uri)

for node in sg_reality_nodes:
    params = {
        "security": "reality",
        "flow": "xtls-rprx-vision",
        "pbk": node["pbk"],
        "sid": node["sid"],
        "sni": "iosapps.itunes.apple.com",
        "fp": "chrome",
        "type": "tcp",
    }
    params_str = "&".join(f"{k}={urllib.parse.quote(str(v))}" for k, v in params.items())
    name_encoded = urllib.parse.quote(node["name"])
    uri = f"vless://b962a7cf-2963-4c00-9fc8-931d649d6178@{node['server']}:443?{params_str}#{name_encoded}"
    lines.append(uri)

for name, server, port, sni in us_hy2_nodes:
    name_encoded = urllib.parse.quote(name)
    uri = f"hysteria2://b962a7cf-2963-4c00-9fc8-931d649d6178@{server}:{port}?sni={sni}#{name_encoded}"
    lines.append(uri)

for name, server in hk_hy2_nodes:
    name_encoded = urllib.parse.quote(name)
    uri = f"hysteria2://b962a7cf-2963-4c00-9fc8-931d649d6178@{server}:443?sni=www.apple.com#{name_encoded}"
    lines.append(uri)

print("\n".join(lines))
