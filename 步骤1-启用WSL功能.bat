@echo off
chcp 65001 >nul
echo.
echo ========================================
echo  WSL 完整安装与配置
echo ========================================
echo.

REM 检查管理员权限
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo ❌ 需要管理员权限！
    echo.
    echo 请右键点击此文件，选择 "以管理员身份运行"
    pause
    exit /b 1
)

echo ✅ 管理员权限已确认
echo.

echo 📋 步骤 1/3: 启用 WSL 功能...
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

echo.
echo 📋 步骤 2/3: 启用虚拟机平台...
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

echo.
echo 📋 步骤 3/3: 设置 WSL2 为默认版本...
wsl --set-default-version 2

echo.
echo ========================================
echo ✅ WSL 功能已启用！
echo ========================================
echo.
echo ⚠️  重要：需要重启电脑才能生效！
echo.
echo 重启后请运行: 安装Ubuntu.bat
echo.
choice /C YN /M "是否立即重启电脑？(Y=是, N=否)"
if errorlevel 2 goto :no_reboot
if errorlevel 1 goto :reboot

:reboot
echo.
echo 🔄 正在重启...（10秒后）
shutdown /r /t 10 /c "WSL 配置完成，10秒后重启"
exit

:no_reboot
echo.
echo ⚠️  请记得稍后手动重启电脑！
echo 重启后运行: 安装Ubuntu.bat
pause
exit
