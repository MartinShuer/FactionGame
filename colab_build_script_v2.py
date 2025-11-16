# ========== 稳定版 APK 打包脚本 (解决网络错误) ==========

# 1. 挂载Google Drive
from google.colab import drive
drive.mount('/content/drive')

# 2. 安装依赖（使用国内源加速）
print("📦 正在安装打包工具...")
!apt-get update -qq
!apt-get install -y -qq git zip unzip openjdk-17-jdk wget autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
!pip install -q --upgrade pip
!pip install -q buildozer cython==0.29.33

# 3. 切换到项目目录
import os
project_path = '/content/drive/MyDrive/FactionGame'
os.chdir(project_path)
print(f"📁 当前目录: {os.getcwd()}")
print("📄 项目文件:")
!ls -lh

# 4. 备份并修改 buildozer.spec（使用更稳定的配置）
print("\n🔧 优化构建配置...")
!cp buildozer.spec buildozer.spec.backup

spec_content = """
[app]
title = Faction Game
package.name = factiongame
package.domain = org.factiongame
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp4
source.include_patterns = *.mp4,*.png
version = 1.0
requirements = python3,kivy==2.3.0,ffpyplayer
orientation = portrait
fullscreen = 1
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a
android.skip_update = False
android.release_artifact = apk
android.logcat_filters = *:S python:D

[buildozer]
log_level = 2
warn_on_root = 0
"""

with open('buildozer.spec', 'w') as f:
    f.write(spec_content.strip())

print("✅ 配置已优化（仅构建 arm64-v8a 以加速）")

# 5. 完全清理（重要！）
print("\n🧹 清理旧文件...")
!rm -rf .buildozer
!rm -rf bin

# 6. 设置环境变量（避免网络超时）
import os
os.environ['GRADLE_OPTS'] = '-Xmx2048m -Dorg.gradle.daemon=false'
os.environ['ANDROID_HOME'] = '/root/.buildozer/android/platform/android-sdk'

# 7. 开始构建（使用单线程避免下载冲突）
print("\n🔨 开始构建 APK...")
print("⏰ 首次构建需要 30-50 分钟")
print("💡 如果下载失败，请重新运行此脚本\n")

try:
    !buildozer -v android debug
    print("\n✅ 构建成功！")
except Exception as e:
    print(f"\n⚠️ 构建过程出现问题: {e}")
    print("💡 这可能是网络问题，请重新运行脚本")

# 8. 查找并下载 APK
print("\n🔍 查找生成的 APK...")
import glob
from google.colab import files

apk_files = glob.glob('./bin/*.apk')
if apk_files:
    apk_path = apk_files[0]
    print(f"✅ 找到 APK: {apk_path}")
    
    # 显示文件大小
    import os
    size_mb = os.path.getsize(apk_path) / (1024*1024)
    print(f"📦 文件大小: {size_mb:.1f} MB")
    
    # 下载
    print("📥 开始下载...")
    files.download(apk_path)
    print("✅ 下载完成！")
else:
    print("\n❌ 未找到 APK 文件")
    print("\n🔍 检查构建目录:")
    !find . -name "*.apk" -type f
    print("\n📋 检查 bin 目录:")
    !ls -la bin/ || echo "bin 目录不存在"
