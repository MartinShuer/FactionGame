#!/bin/bash
# ========== 修复 PATH 并构建 APK ==========

echo "🔧 修复 PATH 配置..."

# 确保 ~/.local/bin 在 PATH 中
export PATH="$HOME/.local/bin:$PATH"

# 验证 buildozer 是否可用
if command -v buildozer &> /dev/null; then
    echo "✅ Buildozer 已找到: $(command -v buildozer)"
    buildozer --version
else
    echo "❌ Buildozer 仍未找到，尝试重新安装..."
    python3 -m pip install --user --upgrade buildozer cython==0.29.33
    export PATH="$HOME/.local/bin:$PATH"
fi

echo ""
echo "🗑️  清理旧构建缓存..."
cd /mnt/c/Users/Martin/Desktop/FactionGame/android_version
rm -rf .buildozer
rm -rf bin

echo ""
echo "🔨 开始构建 APK..."
echo "⏰ 预计需要 30-50 分钟（首次）"
echo "💡 可以去喝杯咖啡 ☕"
echo ""

# 设置环境变量
export GRADLE_OPTS="-Xmx2048m -Dorg.gradle.daemon=false"

# 开始构建
buildozer -v android debug

# 检查结果
if [ $? -eq 0 ]; then
    echo ""
    echo "========================================="
    echo "✅ 构建成功！"
    echo "========================================="
    echo ""
    echo "📦 APK 文件："
    ls -lh bin/*.apk
    
    # 复制到桌面
    APK_FILE=$(ls bin/*.apk 2>/dev/null | head -n 1)
    if [ -n "$APK_FILE" ]; then
        DESKTOP_PATH="/mnt/c/Users/Martin/Desktop/FactionGame.apk"
        cp "$APK_FILE" "$DESKTOP_PATH"
        echo ""
        echo "✅ APK 已复制到桌面: FactionGame.apk"
        echo "📱 现在可以传输到平板安装了！"
    fi
else
    echo ""
    echo "❌ 构建失败，请检查错误信息"
    echo ""
    echo "💡 常见解决方案："
    echo "1. 网络问题 → 关闭代理后重试"
    echo "2. 磁盘空间不足 → 至少需要 10GB"
    echo "3. 依赖下载失败 → 重新运行此脚本"
fi
