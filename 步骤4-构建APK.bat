@echo off
chcp 65001 >nul
echo.
echo ========================================
echo  构建 FactionGame APK
echo ========================================
echo.

echo 🔨 即将开始构建 APK...
echo ⏰ 首次构建需要 30-50 分钟
echo 💡 可以去喝杯咖啡 ☕
echo.
pause

echo.
echo 🚀 启动构建...
echo.

wsl -d Ubuntu-22.04 bash /mnt/c/Users/Martin/Desktop/FactionGame/android_version/03-构建APK.sh

if %errorLevel% == 0 (
    echo.
    echo ========================================
    echo ✅ 构建完成！
    echo ========================================
    echo.
    echo 📱 APK 已复制到桌面: FactionGame.apk
    echo.
    echo 📋 下一步：
    echo 1. 通过 USB/QQ/微信 传输到平板
    echo 2. 在平板上安装 APK
    echo 3. 测试应用
    echo.
) else (
    echo.
    echo ❌ 构建失败
    echo.
    echo 💡 查看构建日志查找错误原因
    echo.
    echo 手动构建方法：
    echo 1. 打开 Ubuntu 应用
    echo 2. 运行以下命令：
    echo    cd /mnt/c/Users/Martin/Desktop/FactionGame/android_version
    echo    bash 03-构建APK.sh
    echo.
)

pause
