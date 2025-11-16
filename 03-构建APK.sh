#!/bin/bash
# ========== 一键构建 APK 脚本 ==========
# 在 WSL Ubuntu 中运行

echo "🔨 FactionGame APK 构建脚本"
echo "========================================"

# 设置项目路径
PROJECT_PATH="/mnt/c/Users/Martin/Desktop/FactionGame/android_version"

# 检查路径是否存在
if [ ! -d "$PROJECT_PATH" ]; then
    echo "❌ 错误：项目路径不存在: $PROJECT_PATH"
    exit 1
fi

cd "$PROJECT_PATH"
echo "📁 当前目录: $(pwd)"
echo ""

# 显示项目文件
echo "📄 项目文件："
ls -lh *.py *.spec *.png *.mp4 2>/dev/null
echo ""

# 询问是否清理旧构建
read -p "🧹 是否清理旧构建文件？(y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🧹 清理中..."
    rm -rf .buildozer bin
    echo "✅ 清理完成"
fi
echo ""

# 开始构建
echo "🔨 开始构建 APK..."
echo "⏰ 首次构建需要 30-50 分钟，请耐心等待..."
echo "💡 可以去喝杯咖啡 ☕"
echo ""

# 设置环境变量
export GRADLE_OPTS="-Xmx2048m -Dorg.gradle.daemon=false"

# 构建
buildozer -v android debug

# 检查结果
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ 构建成功！"
    echo ""
    echo "📦 APK 文件："
    ls -lh bin/*.apk
    
    # 复制到桌面
    APK_FILE=$(ls bin/*.apk | head -n 1)
    DESKTOP_PATH="/mnt/c/Users/Martin/Desktop/FactionGame.apk"
    
    cp "$APK_FILE" "$DESKTOP_PATH"
    echo ""
    echo "✅ APK 已复制到桌面: FactionGame.apk"
    echo "📱 现在可以传输到平板安装了！"
else
    echo ""
    echo "❌ 构建失败，请检查错误信息"
    echo ""
    echo "💡 常见问题："
    echo "1. 网络问题 → 重新运行此脚本"
    echo "2. 磁盘空间不足 → 至少需要 10GB"
    echo "3. 依赖问题 → 运行 02-配置Ubuntu环境.sh"
fi
