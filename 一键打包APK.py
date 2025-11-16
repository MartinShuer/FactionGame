# ========== 一键打包APK脚本 - 专为iQOO Pad2 Pro优化 ==========
# 使用方法：复制此脚本内容到 Google Colab 运行

# 1. 挂载Google Drive
from google.colab import drive
drive.mount('/content/drive')

# 2. 安装打包工具
print("📦 正在安装打包工具...")
!apt-get update -qq
!apt-get install -y -qq git zip unzip openjdk-17-jdk wget autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
!pip install -q --upgrade pip
!pip install -q buildozer cython==0.29.33

# 3. 切换到项目目录（请修改为您的实际路径）
import os
project_path = '/content/drive/MyDrive/FactionGame'  # ⚠️ 修改为您的Drive路径
os.chdir(project_path)
print(f"📁 当前目录: {os.getcwd()}")
print("\n📄 项目文件:")
!ls -lh *.py *.spec *.png *.mp4 2>/dev/null || ls -lh

# 4. 优化 buildozer.spec 配置（专为平板优化）
print("\n🔧 优化平板全屏配置...")
spec_content = """[app]
# 应用基本信息
title = Faction Game
package.name = factiongame
package.domain = org.factiongame
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp4
source.include_patterns = *.mp4,*.png
version = 1.0

# Python要求
requirements = python3,kivy==2.3.0,ffpyplayer

# 屏幕方向和显示 - 专为平板优化
orientation = portrait
fullscreen = 1

# Android权限
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Android版本
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# 架构支持（仅arm64，适合现代平板，构建更快）
android.archs = arm64-v8a

# 全屏主题（无状态栏、无导航栏）
android.theme = @android:style/Theme.NoTitleBar.Fullscreen

# 优化日志
android.logcat_filters = *:S python:D

[buildozer]
log_level = 2
warn_on_root = 0
"""

with open('buildozer.spec', 'w') as f:
    f.write(spec_content)

print("✅ 已应用平板全屏优化配置")

# 5. 清理旧构建
print("\n🧹 清理旧构建文件...")
!rm -rf .buildozer
!rm -rf bin

# 6. 设置环境变量
os.environ['GRADLE_OPTS'] = '-Xmx2048m -Dorg.gradle.daemon=false'

# 7. 开始构建APK
print("\n🔨 开始构建APK...")
print("⏰ 首次构建需要 30-50 分钟（会下载 Android SDK、NDK 等）")
print("💡 后续构建只需 10-20 分钟\n")

try:
    !buildozer -v android debug
    print("\n✅✅✅ 构建成功！✅✅✅")
except Exception as e:
    print(f"\n⚠️ 构建过程出现问题: {e}")
    print("💡 如果是网络问题，请重新运行此脚本")

# 8. 查找并下载APK
print("\n🔍 查找生成的APK...")
import glob
from google.colab import files

apk_files = glob.glob('./bin/*.apk')
if apk_files:
    apk_path = apk_files[0]
    print(f"\n✅ 找到APK: {apk_path}")
    
    # 显示文件信息
    size_mb = os.path.getsize(apk_path) / (1024*1024)
    print(f"📦 文件大小: {size_mb:.1f} MB")
    print(f"📱 目标设备: iQOO Pad2 Pro")
    print(f"🎮 分辨率: 自动适配 (3096×2064)")
    
    # 下载APK
    print("\n📥 开始下载APK...")
    files.download(apk_path)
    print("\n🎉 下载完成！请在浏览器下载目录中查找APK文件")
    print("\n📌 安装步骤:")
    print("   1. 将APK传输到iQOO Pad2 Pro（USB或QQ/微信）")
    print("   2. 在平板上点击APK文件安装")
    print("   3. 如提示'未知来源'，请到设置中允许安装")
    print("   4. 安装后打开'Faction Game'即可全屏运行！")
else:
    print("\n❌ 未找到APK文件")
    print("\n🔍 检查所有APK文件:")
    !find . -name "*.apk" -type f
    print("\n📋 检查bin目录:")
    !ls -la bin/ 2>/dev/null || echo "bin目录不存在，构建可能失败"

