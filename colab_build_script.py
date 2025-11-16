# ========== 完整一键打包脚本 ==========
# 复制这个文件的全部内容到 Google Colab

# 1. 挂载Google Drive
from google.colab import drive
drive.mount('/content/drive')

# 2. 安装所有依赖（需要5-10分钟）
print("📦 正在安装打包工具...")
!apt-get update -qq
!apt-get install -y -qq git zip unzip openjdk-17-jdk wget autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
!pip install -q buildozer cython==0.29.33

# 3. 切换到项目目录（修改成您的实际路径）
import os
project_path = '/content/drive/MyDrive/FactionGame'
os.chdir(project_path)
print(f"📁 当前目录: {os.getcwd()}")
print("📄 项目文件:")
!ls -lh

# 4. 清理之前的构建（如果有）
!rm -rf .buildozer
!rm -rf bin

# 5. 开始构建APK（需要20-40分钟，首次会更久）
print("\n🔨 开始构建APK...")
print("⏰ 预计需要 20-40 分钟，请耐心等待...")
!buildozer -v android debug

# 6. 查找生成的APK
print("\n🔍 查找生成的APK文件...")
!find . -name "*.apk" -type f

# 7. 下载APK到本地
import glob
apk_files = glob.glob('./bin/*.apk')
if apk_files:
    apk_path = apk_files[0]
    print(f"\n✅ 找到APK: {apk_path}")
    from google.colab import files
    files.download(apk_path)
    print("📥 APK下载完成！请在浏览器下载目录中查找")
else:
    print("\n❌ 未找到APK文件，请检查构建日志")
