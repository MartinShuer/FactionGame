# ========== 一键打包APK - 终极稳定版 ==========
# 解决 Python 版本不兼容问题，使用最稳定的配置

# 1. 挂载Google Drive
from google.colab import drive
drive.mount('/content/drive')

# 2. 安装打包工具
print("📦 正在安装打包工具...")
!apt-get update -qq
!apt-get install -y -qq git zip unzip openjdk-17-jdk wget autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
!pip install -q --upgrade pip
!pip install -q buildozer cython==0.29.33

# 3. 切换到项目目录
import os
project_path = '/content/drive/MyDrive/FactionGame'  # ⚠️ 修改为您的Drive路径
os.chdir(project_path)
print(f"📁 当前目录: {os.getcwd()}")

# 4. 检查必需文件
required_files = ['main.py', 'hand.png', 'bg.png', 'rusher.mp4', 'defender.mp4']
missing_files = [f for f in required_files if not os.path.exists(f)]
if missing_files:
    print(f"\n❌ 缺少文件: {', '.join(missing_files)}")
    print("请确保所有文件都已上传!")
else:
    print(f"\n✅ 所有必需文件都存在")
    !ls -lh *.py *.png *.mp4 2>/dev/null

# 5. 完全清理旧构建（重要！）
print("\n🧹 完全清理旧构建...")
!rm -rf .buildozer
!rm -rf bin

# 6. 创建优化的 buildozer.spec（使用 Kivy 2.2.1，更稳定）
print("\n🔧 创建稳定配置...")
spec_content = """[app]
title = Faction Game
package.name = factiongame
package.domain = org.factiongame
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp4
source.include_patterns = *.mp4,*.png
version = 1.0

# 使用稳定的 Kivy 2.2.1（兼容性更好）
requirements = python3==3.10,kivy==2.2.1,ffpyplayer

orientation = portrait
fullscreen = 1
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# 仅构建 arm64（速度快，兼容iQOO Pad2 Pro）
android.archs = arm64-v8a

android.theme = @android:style/Theme.NoTitleBar.Fullscreen
android.logcat_filters = *:S python:D

[buildozer]
log_level = 2
warn_on_root = 0
"""

with open('buildozer.spec', 'w') as f:
    f.write(spec_content)

print("✅ 已创建稳定配置（Kivy 2.2.1 + Python 3.10）")

# 7. 设置环境变量
os.environ['GRADLE_OPTS'] = '-Xmx2048m -Dorg.gradle.daemon=false'
os.environ['ANDROIDSDK'] = '/root/.buildozer/android/platform/android-sdk'
os.environ['ANDROIDNDK'] = '/root/.buildozer/android/platform/android-ndk-r25b'

# 8. 配置 Git（避免下载失败）
!git config --global http.postBuffer 524288000
!git config --global http.lowSpeedLimit 0
!git config --global http.lowSpeedTime 999999

# 9. 开始构建
print("\n🔨 开始构建APK...")
print("⏰ 预计需要 30-50 分钟（首次）")
print("💡 使用稳定版 Kivy 2.2.1，避免 Python 版本冲突\n")

try:
    !buildozer -v android debug
    print("\n✅✅✅ 构建成功！✅✅✅")
except Exception as e:
    print(f"\n⚠️ 构建出错: {e}")
    print("\n💡 如果仍然失败，请尝试：")
    print("   1. 重新运行此脚本（会从断点继续）")
    print("   2. 或者换个时间段重试（避开网络高峰）")

# 10. 查找并下载APK
print("\n🔍 查找生成的APK...")
import glob
from google.colab import files

# 检查 bin 目录
if os.path.exists('bin'):
    print("\n📦 bin 目录内容:")
    !ls -lh bin/
    
    apk_files = glob.glob('./bin/*.apk')
    if apk_files:
        apk_path = apk_files[0]
        size_mb = os.path.getsize(apk_path) / (1024*1024)
        
        print(f"\n✅ 找到APK: {apk_path}")
        print(f"📦 文件大小: {size_mb:.1f} MB")
        
        if size_mb < 20:
            print("⚠️ 警告：APK文件太小，可能不完整")
        else:
            print(f"📱 目标设备: iQOO Pad2 Pro")
            print(f"🎮 配置: Kivy 2.2.1 + Python 3.10")
            
            print("\n📥 开始下载APK...")
            files.download(apk_path)
            print("\n🎉🎉🎉 下载完成！🎉🎉🎉")
            print("\n📌 安装步骤:")
            print("   1. 将APK传输到 iQOO Pad2 Pro")
            print("   2. 在平板上点击安装")
            print("   3. 允许未知来源")
            print("   4. 打开'Faction Game'全屏运行！")
    else:
        print("\n❌ bin 目录中没有APK文件")
        print("💡 构建可能失败，请重新运行脚本")
else:
    print("\n❌ bin 目录不存在，构建失败")
    print("💡 请重新运行此脚本")

print("\n" + "="*50)
print("如果遇到问题，请重新运行此脚本")
print("Buildozer 会自动从断点继续，不会重复下载")
print("="*50)



