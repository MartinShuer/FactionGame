# ========== 一键打包APK脚本 - 稳定版（自动重试） ==========
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

# 3. 切换到项目目录
import os
project_path = '/content/drive/MyDrive/FactionGame'  # ⚠️ 修改为您的Drive路径
os.chdir(project_path)
print(f"📁 当前目录: {os.getcwd()}")
print("\n📄 项目文件:")
!ls -lh *.py *.spec *.png *.mp4 2>/dev/null || ls -lh

# 4. 检查必需文件
required_files = ['main.py', 'buildozer.spec', 'hand.png', 'bg.png', 'rusher.mp4', 'defender.mp4']
missing_files = [f for f in required_files if not os.path.exists(f)]
if missing_files:
    print(f"\n❌ 缺少文件: {', '.join(missing_files)}")
    print("请确保所有6个文件都已上传到Drive!")
    raise FileNotFoundError(f"缺少必需文件")
else:
    print(f"\n✅ 所有必需文件都存在")

# 5. 配置 Git（避免子模块下载失败）
print("\n🔧 配置Git...")
!git config --global http.postBuffer 524288000
!git config --global http.lowSpeedLimit 0
!git config --global http.lowSpeedTime 999999

# 6. 清理旧构建（如果需要）
# 如果是第一次运行或者想完全重新构建，取消下面两行的注释
# !rm -rf .buildozer
# !rm -rf bin

# 7. 设置环境变量
os.environ['GRADLE_OPTS'] = '-Xmx2048m -Dorg.gradle.daemon=false'
os.environ['ANDROID_HOME'] = '/root/.buildozer/android/platform/android-sdk'

# 8. 开始构建APK（带重试机制）
print("\n🔨 开始构建APK...")
print("⏰ 首次构建需要 30-50 分钟")
print("💡 如果网络中断，会自动重试\n")

import subprocess
import time

max_retries = 3
retry_count = 0
build_success = False

while retry_count < max_retries and not build_success:
    if retry_count > 0:
        print(f"\n🔄 第 {retry_count + 1} 次尝试...")
        time.sleep(5)
    
    try:
        result = subprocess.run(
            ['buildozer', '-v', 'android', 'debug'],
            check=True,
            capture_output=False,
            text=True
        )
        build_success = True
        print("\n✅✅✅ 构建成功！✅✅✅")
    except subprocess.CalledProcessError as e:
        retry_count += 1
        if retry_count < max_retries:
            print(f"\n⚠️ 构建失败，准备重试... ({retry_count}/{max_retries})")
        else:
            print(f"\n❌ 构建失败，已达到最大重试次数")
            print("\n💡 这通常是网络问题，请稍后重新运行脚本")
            print("💡 或者运行以下命令清理后重试:")
            print("   !rm -rf .buildozer")

# 9. 查找并下载APK
print("\n🔍 查找生成的APK...")
import glob
from google.colab import files

# 检查 bin 目录
if os.path.exists('bin'):
    !ls -lh bin/
else:
    print("⚠️ bin 目录不存在")

apk_files = glob.glob('./bin/*.apk')
if apk_files:
    apk_path = apk_files[0]
    print(f"\n✅ 找到APK: {apk_path}")
    
    # 显示文件信息
    size_mb = os.path.getsize(apk_path) / (1024*1024)
    print(f"📦 文件大小: {size_mb:.1f} MB")
    
    if size_mb < 10:
        print("⚠️ APK文件太小，可能构建不完整")
    else:
        print(f"📱 目标设备: iQOO Pad2 Pro")
        print(f"🎮 分辨率: 自动适配 (3096×2064)")
        
        # 下载APK
        print("\n📥 开始下载APK...")
        files.download(apk_path)
        print("\n🎉🎉🎉 下载完成！🎉🎉🎉")
        print("\n📌 安装步骤:")
        print("   1. 将APK传输到iQOO Pad2 Pro（USB或QQ/微信）")
        print("   2. 在平板上点击APK文件安装")
        print("   3. 如提示'未知来源'，请到设置中允许安装")
        print("   4. 安装后打开'Faction Game'即可全屏运行！")
else:
    print("\n❌ 未找到APK文件")
    print("\n📋 构建可能失败，请检查上面的错误信息")
    print("\n💡 常见原因:")
    print("   1. 网络问题 - 重新运行此脚本")
    print("   2. 首次构建被中断 - 重新运行会继续下载")
    print("   3. 配置错误 - 检查 buildozer.spec 文件")
    print("\n🔍 手动检查所有APK:")
    !find . -name "*.apk" -type f 2>/dev/null || echo "未找到任何APK文件"



