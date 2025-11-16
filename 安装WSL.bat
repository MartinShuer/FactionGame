@echo off
chcp 65001 >nul
echo.
echo ========================================
echo  FactionGame APK 构建 - WSL 安装
echo ========================================
echo.

REM 检查管理员权限
net session >nul 2>&1
if %errorLevel% == 0 (
    echo ✅ 管理员权限已确认
) else (
    echo ❌ 错误：需要管理员权限
    echo.
    echo 请右键点击此文件，选择 "以管理员身份运行"
    echo.
    pause
    exit
)

echo.
echo 📦 开始安装 WSL + Ubuntu...
echo ⏰ 预计需要 5-10 分钟
echo.

REM 安装 WSL
wsl --install -d Ubuntu

echo.
echo ========================================
if %errorLevel% == 0 (
    echo ✅ WSL 安装成功！
    echo.
    echo 📋 下一步：
    echo 1. 重启电脑（必需）
    echo 2. 重启后打开 "Ubuntu" 应用
    echo 3. 设置用户名和密码
    echo 4. 运行配置脚本
    echo.
    echo 是否立即重启？
    choice /C YN /M "选择 (Y=是, N=否)"
    if errorlevel 2 goto :no_reboot
    if errorlevel 1 goto :reboot
) else (
    echo ❌ 安装失败
    echo 请检查网络连接或手动运行: wsl --install
)
pause
exit

:reboot
echo.
echo 🔄 正在重启...
shutdown /r /t 10 /c "WSL 安装完成，10秒后重启"
exit

:no_reboot
echo.
echo ⚠️  请记得稍后手动重启电脑！
pause
exit
