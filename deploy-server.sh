#!/bin/bash
# Easy Proxies 服务器一键部署脚本

set -e

echo "🚀 Easy Proxies Docker 部署脚本"
echo "================================"
echo ""

# 检查 Docker
if ! command -v docker &> /dev/null; then
    echo "❌ Docker 未安装！"
    echo ""
    echo "请先安装 Docker："
    echo "curl -fsSL https://get.docker.com | sh"
    exit 1
fi

# 检查 Docker Compose
if ! command -v docker compose &> /dev/null; then
    echo "❌ Docker Compose 未安装！"
    echo ""
    echo "请升级 Docker 到最新版本"
    exit 1
fi

echo "✅ Docker 环境检查通过"
echo ""

# 克隆仓库
if [ -d "easy_proxies" ]; then
    echo "📁 目录已存在，更新代码..."
    cd easy_proxies
    git pull
else
    echo "📥 克隆仓库..."
    git clone https://github.com/lmarch2/easy_proxies.git
    cd easy_proxies
fi

echo ""
echo "🔧 配置说明："
echo "- 代理端口: 2323 (HTTP + SOCKS5)"
echo "- WebUI端口: 9091"
echo "- 用户名: lmarch2"
echo "- 密码: LYFnb@@@"
echo ""

# 等待 GitHub Actions 构建完成提示
echo "⏳ 注意：首次部署需要等待 GitHub Actions 构建完成（约10-15分钟）"
echo "   构建状态: https://github.com/lmarch2/easy_proxies/actions"
echo ""

read -p "继续部署？(y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "已取消部署"
    exit 0
fi

# 启动服务
echo ""
echo "🐳 启动 Docker 容器..."
docker compose up -d

echo ""
echo "⏳ 等待服务启动（5秒）..."
sleep 5

# 检查状态
echo ""
echo "📊 容器状态："
docker compose ps

echo ""
echo "✅ 部署完成！"
echo "================================"
echo ""
echo "🌐 访问地址："
echo "   WebUI:  http://$(hostname -I | awk '{print $1}'):9091"
echo "   密码:   admin123"
echo ""
echo "🔌 代理配置："
echo "   地址:   $(hostname -I | awk '{print $1}'):2323"
echo "   用户名: lmarch2"
echo "   密码:   LYFnb@@@"
echo ""
echo "📝 常用命令："
echo "   查看日志: docker compose logs -f"
echo "   重启服务: docker compose restart"
echo "   停止服务: docker compose down"
echo ""
echo "🧪 测试代理："
echo "   curl -x http://lmarch2:LYFnb@@@localhost:2323 http://ip-api.com/json"
echo ""
