"""
阵营选择游戏 - Google Colab APK构建脚本
直接在 Google Colab 中运行此脚本即可构建APK

使用步骤：
1. 将 android_version 文件夹上传到 Google Drive
2. 打开 https://colab.research.google.com/
3. 创建新笔记本
4. 将下面的代码块逐个复制到Cell中运行
"""

# ============================================================
# Cell 1: 挂载Google Drive
# ============================================================
from google.colab import drive
drive.mount('/content/drive')


# ============================================================
# Cell 2: 安装系统依赖
# ============================================================
print("📦 Installing system dependencies...")
!apt-get update -qq
!apt-get install -y -qq \
    git zip unzip openjdk-11-jdk wget \
    autoconf libtool pkg-config \
    zlib1g-dev libncurses5-dev libncursesw5-dev \
    libtinfo5 cmake libffi-dev libssl-dev

print("✅ System dependencies installed!")


# ============================================================
# Cell 3: 安装Python依赖
# ============================================================
print("🐍 Installing Python dependencies...")
!pip install -q buildozer
!pip install -q cython==0.29.33

print("✅ Python dependencies installed!")


# ============================================================
# Cell 4: 切换到项目目录
# ============================================================
import os

# 修改这里的路径为您的项目路径
PROJECT_PATH = '/content/drive/MyDrive/android_version'

print(f"📂 Navigating to: {PROJECT_PATH}")
os.chdir(PROJECT_PATH)

# 显示当前目录和文件
print("\n📋 Current directory:")
!pwd
print("\n📄 Files in directory:")
!ls -la

# 检查必要文件
print("\n🔍 Checking required files...")
required_files = ['main.py', 'buildozer.spec', 'hand.mp4', 'rusher.mp4', 'defender.mp4']
for file in required_files:
    if os.path.exists(file):
        print(f"  ✅ {file}")
    else:
        print(f"  ❌ {file} - MISSING!")


# ============================================================
# Cell 5: 清理之前的构建（可选）
# ============================================================
print("🧹 Cleaning previous builds...")
!rm -rf .buildozer
!rm -rf bin

print("✅ Cleaned!")


# ============================================================
# Cell 6: 构建APK（这将需要30-60分钟）
# ============================================================
print("🔨 Building APK...")
print("⏱️  This will take 30-60 minutes for first build...")
print("☕ Time to grab some coffee!\n")

!buildozer -v android debug

print("\n✅ Build complete!")


# ============================================================
# Cell 7: 查找并下载APK
# ============================================================
from google.colab import files
import glob

print("🔍 Looking for APK files...")

# 查找所有APK文件
apk_files = glob.glob('bin/*.apk')

if apk_files:
    for apk in apk_files:
        file_size = os.path.getsize(apk) / (1024 * 1024)  # MB
        print(f"\n✅ Found APK: {apk}")
        print(f"📦 Size: {file_size:.2f} MB")
        
    # 下载第一个APK
    print(f"\n⬇️  Downloading: {apk_files[0]}")
    files.download(apk_files[0])
    print("✅ Download started!")
else:
    print("❌ No APK files found!")
    print("Check the build log above for errors.")


# ============================================================
# Cell 8: 显示构建日志（如果构建失败）
# ============================================================
print("📝 Last 50 lines of build log:")
!tail -50 .buildozer/android/platform/build-*/build.log 2>/dev/null || echo "No log file found"


# ============================================================
# 可选: Cell 9: 构建Release版本（需要密钥）
# ============================================================
# 如果需要构建正式版，运行这个Cell
# 注意: 需要先创建密钥文件

"""
# 创建密钥（仅首次需要）
!keytool -genkey -v -keystore my-release-key.keystore -alias my-key-alias -keyalg RSA -keysize 2048 -validity 10000

# 构建Release APK
!buildozer -v android release

# 下载Release APK
release_apk = glob.glob('bin/*-release.apk')
if release_apk:
    files.download(release_apk[0])
"""


# ============================================================
# 完成！
# ============================================================
print("\n" + "="*60)
print("🎉 BUILD COMPLETE!")
print("="*60)
print("\n📱 Next steps:")
print("1. Download the APK from your browser")
print("2. Transfer it to your iQOO Pad2 Pro")
print("3. Install and enjoy!")
print("\n💡 Tips:")
print("- Enable 'Unknown sources' in Android settings")
print("- Allow all permissions during installation")
print("- APK file is usually 20-50 MB")
print("="*60)
