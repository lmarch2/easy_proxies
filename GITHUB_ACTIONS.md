# 🐳 GitHub Actions 自动构建 Docker 镜像

本项目已配置 GitHub Actions 自动构建多架构 Docker 镜像。

## 📦 镜像地址

```
ghcr.io/lmarch2/easy_proxies:latest
```

## 🏗️ 构建触发条件

GitHub Actions 会在以下情况自动构建并推送镜像：

### 1. 推送到 main 分支

```bash
git push origin main
```

自动构建标签：
- `latest` - 最新版本
- `main` - main 分支版本
- `sha-xxxxxx` - Git commit SHA

### 2. 创建版本标签

```bash
# 创建版本标签
git tag v1.0.0
git push origin v1.0.0
```

自动构建标签：
- `v1.0.0` - 完整版本号
- `v1.0` - 主次版本
- `v1` - 主版本
- `latest` - 最新版本

### 3. Pull Request

PR 会触发构建测试（不推送镜像）

---

## 🌍 支持的架构

- ✅ **linux/amd64** - Intel/AMD 64位（服务器常用）
- ✅ **linux/arm64** - ARM 64位（树莓派、Apple Silicon）

---

## 🚀 使用预构建镜像部署

### 方式 1: Docker Compose（推荐）

```bash
git clone https://github.com/lmarch2/easy_proxies.git
cd easy_proxies
docker compose up -d
```

### 方式 2: Docker 命令

```bash
docker pull ghcr.io/lmarch2/easy_proxies:latest

docker run -d \
  --name easy-proxies \
  --restart unless-stopped \
  --network host \
  -v $(pwd)/config.yaml:/etc/easy-proxies/config.yaml \
  -v $(pwd)/nodes.txt:/etc/easy-proxies/nodes.txt \
  ghcr.io/lmarch2/easy_proxies:latest
```

---

## 🔄 查看构建状态

访问 [Actions 页面](https://github.com/lmarch2/easy_proxies/actions) 查看构建状态。

构建完成后，镜像会自动推送到：
- GitHub Container Registry: https://github.com/lmarch2/easy_proxies/pkgs/container/easy_proxies

---

## 📋 工作流程说明

### 构建流程

1. **触发** - Push 或创建 Tag
2. **拉取代码** - Checkout repository
3. **设置环境** - QEMU + Docker Buildx
4. **登录仓库** - GitHub Container Registry
5. **构建镜像** - 多架构并行构建
6. **推送镜像** - 推送到 GHCR
7. **缓存优化** - 使用 GitHub Actions Cache

### 构建时间

- 首次构建：~10-15 分钟
- 增量构建：~3-5 分钟（有缓存）

---

## 🔧 本地测试 Actions

安装 act 工具：

```bash
# macOS
brew install act

# Linux
curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash
```

运行本地测试：

```bash
act -j build
```

---

## 🎯 镜像标签策略

| 事件 | 标签 | 示例 |
|------|------|------|
| Push to main | `latest`, `main`, `sha-xxx` | `latest` |
| Tag v1.2.3 | `v1.2.3`, `v1.2`, `v1`, `latest` | `v1.2.3` |
| Pull Request | `pr-123` | `pr-456` |

---

## 📝 自定义构建

如需修改构建配置，编辑 `.github/workflows/docker-build.yml`：

```yaml
# 修改支持的架构
platforms: linux/amd64,linux/arm64,linux/arm/v7

# 修改 Go 版本
# Dockerfile 中修改 FROM golang:1.24

# 添加构建参数
build-args: |
  VERSION=${{ github.ref_name }}
  COMMIT=${{ github.sha }}
```

---

## 🔒 镜像安全

- ✅ 使用官方 Go 和 Debian 镜像
- ✅ 非 root 用户运行
- ✅ 最小化镜像体积
- ✅ 定期更新依赖

---

## 📊 镜像大小

预计镜像大小：
- **压缩后**：~50-80 MB
- **解压后**：~150-200 MB

---

需要帮助？查看 [GitHub Actions 文档](https://docs.github.com/en/actions)
