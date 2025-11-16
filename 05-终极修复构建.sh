#!/bin/bash
# ========== 终极修复：完全清理并使用稳定配置 ==========

echo "🗑️  完全清理所有缓存..."
cd /mnt/c/Users/Martin/Desktop/FactionGame/android_version

# 清理所有 buildozer 缓存
rm -rf .buildozer
rm -rf bin
rm -rf ~/.buildozer/android/platform/build-*
rm -rf ~/.buildozer/android/platform/python-for-android

echo "✅ 缓存已清理"
echo ""

# 确保 PATH 正确
export PATH="$HOME/.local/bin:$PATH"

# 配置 Git 忽略证书（解决 Google 源访问问题）
git config --global http.sslVerify false
git config --global http.postBuffer 524288000
git config --global http.lowSpeedLimit 0
git config --global http.lowSpeedTime 999999

echo "🔧 Git 配置已优化"
echo ""

echo "🔨 开始构建 APK (使用 Kivy 2.1.0 稳定版)..."
echo "⏰ 预计需要 25-40 分钟"
echo ""

# 设置环境变量
export GRADLE_OPTS="-Xmx2048m -Dorg.gradle.daemon=false"

# 使用 p4a 缓存
export P4A_RELEASE_KEYSTORE=~/.buildozer/android/platform/python-for-android/dist/default
export USE_SDK_WRAPPER=1

# 开始构建
buildozer -v android debug 2>&1 | tee build.log

# 检查结果
if [ ${PIPESTATUS[0]} -eq 0 ]; then
    echo ""
    echo "========================================="
    echo "✅ 构建成功！"
    echo "========================================="
    echo ""
    
    # 查找 APK
    APK_FILE=$(find . -name "*.apk" -type f 2>/dev/null | head -n 1)
    
    if [ -n "$APK_FILE" ]; then
        echo "📦 APK 文件: $APK_FILE"
        ls -lh "$APK_FILE"
        
        # 复制到桌面
        DESKTOP_PATH="/mnt/c/Users/Martin/Desktop/FactionGame.apk"
        cp "$APK_FILE" "$DESKTOP_PATH"
        echo ""
        echo "✅ APK 已复制到桌面: FactionGame.apk"
        echo "📱 文件大小: $(du -h "$DESKTOP_PATH" | cut -f1)"
    else
        echo "⚠️  APK 已生成但未找到，请检查 bin 目录"
    fi
else
    echo ""
    echo "❌ 构建失败"
    echo ""
    echo "📋 错误日志已保存到: build.log"
    echo ""
    echo "最后 30 行错误信息："
    tail -n 30 build.log | grep -E "fatal|error|Error|ERROR|failed|Failed|FAILED" || tail -n 30 build.log
fi
