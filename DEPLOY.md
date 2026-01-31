# 🚀 服务器部署指南

## 快速部署（3 步完成）

### 1. 克隆仓库

```bash
git clone https://github.com/lmarch2/easy_proxies.git
cd easy_proxies
```

### 2. 启动服务

```bash
docker compose up -d
```

### 3. 查看日志

```bash
docker compose logs -f
```

---

## 🎯 部署说明

### 端口

- **2323** - 代理池端口（HTTP + SOCKS5）
- **9091** - WebUI 管理界面

### 认证信息

**代理认证**：
- 用户名：`lmarch2`
- 密码：`LYFnb@@@`

**WebUI 密码**：
- 密码：`admin123`

---

## 🧪 测试部署

### 测试代理

```bash
# 获取出口 IP
curl -x http://lmarch2:LYFnb@@@localhost:2323 http://ip-api.com/json

# 访问 Google
curl -x http://lmarch2:LYFnb@@@localhost:2323 https://www.google.com -I
```

### 访问 WebUI

```
http://your-server-ip:9091
```

登录密码：`admin123`

---

## 🔧 常用命令

### 查看状态

```bash
docker compose ps
```

### 查看日志

```bash
# 实时日志
docker compose logs -f

# 最近 100 行
docker compose logs --tail 100
```

### 重启服务

```bash
docker compose restart
```

### 停止服务

```bash
docker compose down
```

### 更新代码

```bash
git pull
docker compose down
docker compose up -d --build
```

---

## 🔒 防火墙配置

### Ubuntu/Debian (ufw)

```bash
sudo ufw allow 2323/tcp
sudo ufw allow 9091/tcp
```

### CentOS/RHEL (firewalld)

```bash
sudo firewall-cmd --permanent --add-port=2323/tcp
sudo firewall-cmd --permanent --add-port=9091/tcp
sudo firewall-cmd --reload
```

---

## 📊 监控和维护

### 健康检查

```bash
# 检查容器状态
docker ps | grep easy-proxies

# 检查端口监听
netstat -tlnp | grep -E "2323|9091"
```

### 查看节点状态

访问 WebUI 或使用 API：

```bash
curl http://localhost:9091/api/export?format=all
```

---

## ⚙️ 配置修改

### 修改认证信息

编辑 `config.yaml`：

```yaml
listener:
  auth:
    - username: "your-username"
      password: "your-password"
```

重启服务：

```bash
docker compose restart
```

### 修改节点列表

编辑 `nodes.txt`，添加你的节点 URI，每行一个。

重启服务生效：

```bash
docker compose restart
```

---

## 🐛 故障排查

### 问题 1：端口被占用

```bash
# 检查端口占用
lsof -i :2323
lsof -i :9091

# 修改配置文件中的端口
vim config.yaml
```

### 问题 2：无法访问 WebUI

```bash
# 检查防火墙
sudo ufw status

# 检查容器日志
docker compose logs | grep -i error
```

### 问题 3：代理无响应

```bash
# 检查健康检查日志
docker compose logs | grep "health check"

# 手动触发探测
curl -X POST http://localhost:9091/api/probe
```

---

## 📝 高级配置

### 使用端口映射而非 host 网络

编辑 `docker-compose.yml`：

```yaml
services:
  easy-proxies:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: easy-proxies
    restart: unless-stopped
    ports:
      - "2323:2323"
      - "9091:9091"
    volumes:
      - ./config.yaml:/etc/easy-proxies/config.yaml
      - ./nodes.txt:/etc/easy-proxies/nodes.txt
```

### 持久化日志

```yaml
services:
  easy-proxies:
    # ... 其他配置
    volumes:
      - ./config.yaml:/etc/easy-proxies/config.yaml
      - ./nodes.txt:/etc/easy-proxies/nodes.txt
      - ./logs:/var/log/easy-proxies
```

---

## 🎉 完成

部署完成后，你可以：

1. **使用代理**：`http://lmarch2:LYFnb@@@your-server-ip:2323`
2. **管理节点**：`http://your-server-ip:9091`
3. **查看统计**：WebUI 中的实时监控

需要帮助？查看项目 [GitHub Issues](https://github.com/lmarch2/easy_proxies/issues)
