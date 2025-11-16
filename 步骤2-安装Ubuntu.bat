@echo off
chcp 65001 >nul
echo.
echo ========================================
echo  安装 Ubuntu 22.04 LTS
echo ========================================
echo.

echo 📦 开始安装 Ubuntu 22.04...
echo ⏰ 预计需要 5-10 分钟
echo.
wsl --install Ubuntu-22.04

REM 正确语法需使用 -d 指定发行版
echo 正在安装 Ubuntu 22.04 LTS (WSL)...
wsl --install -d Ubuntu-22.04

if %errorLevel% == 0 (
    echo.
    echo ========================================
    echo ✅ Ubuntu 安装成功！
    echo ========================================
    echo.
    echo 📋 下一步：
    echo 1. 会自动打开 Ubuntu 窗口
    echo 2. 首次启动需要等待 5-10 分钟自动配置
    echo 3. 设置用户名（例如: martin）
    echo 4. 设置密码（输入时不显示，正常输入即可）
    echo 5. 确认密码
    echo.
    echo 完成后运行: 步骤3-配置环境.bat
    echo.
 ) else (
    echo.
    echo ❌ 安装失败
    echo.
    echo 💡 可能的原因：
    echo 1. 功能未启用或未重启：请先运行 管理员 PowerShell 中的 步骤1-启用WSL功能.bat 然后重启
    echo 2. 网络问题：稍后重试。建议保持稳定网络
    echo 3. 虚拟化未启用：进 BIOS 检查 Virtualization / SVM / VT-x 是否 Enabled
    echo 4. 如果仍失败，可直接运行: wsl --install  (使用默认 Ubuntu)
    echo 5. 如果提示 "需要商店"，可打开 Microsoft Store 搜索 Ubuntu 安装，再返回本脚本
    echo.
)

pause
