#!/bin/bash
# 一键Clash翻墙脚本
# 用法: ./clash_setup.sh <订阅地址>

set -e

SUBSCRIPTION_URL="$1"
CLASH_DIR="$HOME/.clash"
CLASH_BIN="$CLASH_DIR/clash"
CONFIG_FILE="$CLASH_DIR/config.yaml"
SERVICE_FILE="/etc/systemd/system/clash.service"

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

print_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# 检查参数
if [ -z "$SUBSCRIPTION_URL" ]; then
    print_error "请提供订阅地址"
    echo "用法: $0 <订阅地址>"
    exit 1
fi

# 检测系统架构
ARCH=$(uname -m)
case $ARCH in
    x86_64)
        CLASH_ARCH="amd64"
        ;;
    aarch64|arm64)
        CLASH_ARCH="arm64"
        ;;
    armv7l)
        CLASH_ARCH="armv7"
        ;;
    *)
        print_error "不支持的架构: $ARCH"
        exit 1
        ;;
esac

print_info "检测到系统架构: $ARCH (Clash: $CLASH_ARCH)"

# 创建目录
mkdir -p "$CLASH_DIR"

# 下载Clash
if [ ! -f "$CLASH_BIN" ]; then
    print_info "下载Clash..."
    CLASH_VERSION="v1.18.0"
    CLASH_URL="https://github.com/Dreamacro/clash/releases/download/${CLASH_VERSION}/clash-linux-${CLASH_ARCH}-${CLASH_VERSION}.gz"
    
    curl -L "$CLASH_URL" -o "$CLASH_DIR/clash.gz"
    gunzip -f "$CLASH_DIR/clash.gz"
    chmod +x "$CLASH_BIN"
    print_info "Clash下载完成"
else
    print_info "Clash已存在，跳过下载"
fi

# 下载订阅配置
print_info "下载订阅配置..."
curl -L "$SUBSCRIPTION_URL" -o "$CONFIG_FILE"

if [ ! -s "$CONFIG_FILE" ]; then
    print_error "配置文件下载失败或为空"
    exit 1
fi

print_info "配置文件下载成功"

# 下载Country.mmdb（GeoIP数据库）
if [ ! -f "$CLASH_DIR/Country.mmdb" ]; then
    print_info "下载GeoIP数据库..."
    curl -L "https://github.com/Dreamacro/maxmind-geoip/releases/latest/download/Country.mmdb" \
         -o "$CLASH_DIR/Country.mmdb"
fi

# 创建systemd服务
print_info "创建systemd服务..."
sudo tee "$SERVICE_FILE" > /dev/null <<EOF
[Unit]
Description=Clash daemon
After=network.target

[Service]
Type=simple
User=$USER
ExecStart=$CLASH_BIN -d $CLASH_DIR
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target
EOF

# 启动服务
print_info "启动Clash服务..."
sudo systemctl daemon-reload
sudo systemctl enable clash
sudo systemctl restart clash

# 等待服务启动
sleep 2

# 检查服务状态
if sudo systemctl is-active --quiet clash; then
    print_info "Clash服务启动成功"
else
    print_error "Clash服务启动失败"
    sudo systemctl status clash
    exit 1
fi

# 配置系统代理
print_info "配置系统代理..."

# 添加到bashrc
PROXY_CONFIG="
# Clash代理配置
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
export no_proxy=localhost,127.0.0.1,::1
"

if ! grep -q "Clash代理配置" "$HOME/.bashrc"; then
    echo "$PROXY_CONFIG" >> "$HOME/.bashrc"
    print_info "已添加代理配置到 ~/.bashrc"
fi

# 立即生效
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
export no_proxy=localhost,127.0.0.1,::1

# 测试连接
print_info "测试代理连接..."
if curl -s --max-time 10 -x http://127.0.0.1:7890 https://www.google.com > /dev/null; then
    print_info "代理连接测试成功！"
else
    print_warn "代理连接测试失败，请检查配置"
fi

# 输出信息
echo ""
echo "=========================================="
print_info "Clash配置完成！"
echo "=========================================="
echo ""
echo "代理地址:"
echo "  HTTP:  http://127.0.0.1:7890"
echo "  SOCKS: socks5://127.0.0.1:7891"
echo ""
echo "管理面板:"
echo "  http://127.0.0.1:9090/ui"
echo ""
echo "常用命令:"
echo "  启动: sudo systemctl start clash"
echo "  停止: sudo systemctl stop clash"
echo "  重启: sudo systemctl restart clash"
echo "  状态: sudo systemctl status clash"
echo "  日志: sudo journalctl -u clash -f"
echo ""
echo "更新订阅:"
echo "  $0 <新订阅地址>"
echo ""
echo "当前终端已启用代理，新终端请运行:"
echo "  source ~/.bashrc"
echo ""
print_info "请重新登录或运行 'source ~/.bashrc' 使代理生效"
