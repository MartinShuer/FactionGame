# ========== WSL 一键安装脚本 ==========
# 使用方法：以管理员身份运行此脚本

Write-Host "🚀 FactionGame APK 构建环境配置" -ForegroundColor Cyan
Write-Host "="*50 -ForegroundColor Cyan

# 检查是否以管理员身份运行
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "❌ 错误：需要管理员权限" -ForegroundColor Red
    Write-Host "请右键点击 PowerShell，选择'以管理员身份运行'" -ForegroundColor Yellow
    Read-Host "按回车键退出"
    exit
}

Write-Host "✅ 管理员权限已确认" -ForegroundColor Green

# 检查 WSL 状态
Write-Host "`n📋 检查 WSL 安装状态..." -ForegroundColor Yellow
$wslStatus = wsl --status 2>&1

if ($LASTEXITCODE -ne 0) {
    Write-Host "📦 WSL 未安装，开始安装..." -ForegroundColor Yellow
    
    # 安装 WSL
    wsl --install -d Ubuntu
    
    Write-Host "`n✅ WSL 安装完成！" -ForegroundColor Green
    Write-Host "⚠️  需要重启电脑" -ForegroundColor Yellow
    Write-Host "`n重启后请运行下一步脚本：" -ForegroundColor Cyan
    Write-Host ".\02-配置Ubuntu环境.ps1" -ForegroundColor White
    
    $reboot = Read-Host "`n是否立即重启？(Y/N)"
    if ($reboot -eq "Y" -or $reboot -eq "y") {
        Restart-Computer
    }
} else {
    Write-Host "✅ WSL 已安装" -ForegroundColor Green
    Write-Host "`n📋 WSL 状态：" -ForegroundColor Cyan
    wsl --status
    
    Write-Host "`n✅ 安装完成！请运行下一步脚本：" -ForegroundColor Green
    Write-Host ".\02-配置Ubuntu环境.ps1" -ForegroundColor White
}

Read-Host "`n按回车键退出"
