#!/bin/bash
# ========== Ubuntu 环境配置脚本 ==========
# 在 WSL Ubuntu 中运行此脚本

echo "🚀 配置 Android APK 构建环境"
echo "========================================"

# 更新系统
echo ""
echo "📦 更新系统包..."
sudo apt update
sudo apt upgrade -y

# 安装构建工具
echo ""
echo "🔧 安装构建工具..."
sudo apt install -y \
    python3 \
    python3-pip \
    git \
    zip \
    unzip \
    openjdk-17-jdk \
    wget \
    autoconf \
    libtool \
    pkg-config \
    zlib1g-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libtinfo5 \
    cmake \
    libffi-dev \
    libssl-dev

# 安装 Python 构建工具（以当前用户身份安装，避免权限问题）
echo ""
echo "🐍 安装 Python 构建工具 (user 模式)..."
python3 -m pip install --user --upgrade pip
python3 -m pip install --user buildozer cython==0.29.33

# 将 ~/.local/bin 加入 PATH（Buildozer 安装在这里）
echo ""
echo "🔧 配置 PATH 到 ~/.local/bin..."
if ! grep -q 'export PATH="$HOME/.local/bin:$PATH"' "$HOME/.bashrc"; then
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"
fi
export PATH="$HOME/.local/bin:$PATH"

# 验证安装
echo ""
echo "✅ 验证安装..."
echo "Python: $(python3 --version)"
echo "Buildozer: $(buildozer --version 2>&1 | head -n 1)"
echo "Buildozer 路径: $(command -v buildozer || echo not-found)"
echo "Java: $(java -version 2>&1 | head -n 1)"

echo ""
echo "✅ 环境配置完成！"
echo ""
echo "📋 下一步："
echo "1. cd /mnt/c/Users/Martin/Desktop/FactionGame/android_version"
echo "2. buildozer -v android debug"
