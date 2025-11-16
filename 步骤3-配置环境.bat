@echo off
chcp 65001 >nul
echo.
echo ========================================
echo  配置 Ubuntu 构建环境
echo ========================================
echo.

echo 📋 即将在 Ubuntu 中安装构建工具...
echo ⏰ 预计需要 15-20 分钟
echo.
pause

echo.
echo 🚀 启动 Ubuntu 并运行配置脚本...
echo.

wsl -d Ubuntu-22.04 bash /mnt/c/Users/Martin/Desktop/FactionGame/android_version/02-配置Ubuntu环境.sh

if %errorLevel% == 0 (
    echo.
    echo ========================================
    echo ✅ 环境配置完成！
    echo ========================================
    echo.
    echo 📋 下一步：运行 步骤4-构建APK.bat
    echo.
) else (
    echo.
    echo ❌ 配置失败
    echo.
    echo 💡 手动配置方法：
    echo 1. 打开 Ubuntu 应用
    echo 2. 运行以下命令：
    echo    cd /mnt/c/Users/Martin/Desktop/FactionGame/android_version
    echo    bash 02-配置Ubuntu环境.sh
    echo.
)

pause
