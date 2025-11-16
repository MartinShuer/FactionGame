@echo off
chcp 65001 >nul
echo.
echo ========================================
echo  FactionGame APK 构建 - 完整流程
echo ========================================
echo.

echo 📋 构建步骤：
echo.
echo 第一步：安装 WSL（需要管理员权限）
echo   1. 右键点击 "安装WSL.bat"
echo   2. 选择 "以管理员身份运行"
echo   3. 等待安装完成
echo   4. 重启电脑
echo.
echo 第二步：配置 Ubuntu 环境（重启后）
echo   1. 打开 "Ubuntu" 应用
echo   2. 首次打开会自动安装（5-10分钟）
echo   3. 设置用户名和密码（记住密码！）
echo   4. 运行配置脚本：
echo      cd /mnt/c/Users/Martin/Desktop/FactionGame/android_version
echo      bash 02-配置Ubuntu环境.sh
echo.
echo 第三步：构建 APK（配置完成后）
echo   1. 在 Ubuntu 中运行：
echo      bash 03-构建APK.sh
echo   2. 等待构建完成（30-50分钟首次）
echo   3. APK 会自动复制到桌面
echo.
echo ========================================
echo.
echo 💡 提示：
echo   - 整个过程需要约 1-2 小时（首次）
echo   - 需要稳定的网络连接
echo   - 至少 10GB 可用磁盘空间
echo.
echo 🚀 准备好了吗？
echo.
pause

echo.
echo 📋 现在要做什么？
echo.
echo 1. 开始安装 WSL（需要管理员权限）
echo 2. 查看详细文档
echo 3. 退出
echo.
choice /C 123 /M "选择"

if errorlevel 3 goto :end
if errorlevel 2 goto :docs
if errorlevel 1 goto :install

:install
echo.
echo ⚠️  即将以管理员身份运行安装脚本...
echo 如果弹出 UAC 提示，请点击 "是"
echo.
pause
powershell -Command "Start-Process '安装WSL.bat' -Verb RunAs"
goto :end

:docs
echo.
echo 📖 打开文档: README-开始打包.md
start README-开始打包.md
goto :end

:end
echo.
echo 👋 再见！
echo.
pause
