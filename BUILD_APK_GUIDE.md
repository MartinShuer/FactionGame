# 🚀 打包APK完整指南

## 方法1: Google Colab（最简单，推荐）

### 步骤1: 准备文件

将以下文件上传到Google Drive：
```
android_version/
├── main.py
├── buildozer.spec
├── hand.mp4
├── rusher.mp4
└── defender.mp4
```

### 步骤2: 在Colab中运行

1. 打开 Google Colab: https://colab.research.google.com/
2. 创建新笔记本
3. 运行以下代码：

```python
# ========== Cell 1: 挂载Google Drive ==========
from google.colab import drive
drive.mount('/content/drive')

# ========== Cell 2: 安装依赖 ==========
!apt-get update
!apt-get install -y git zip unzip openjdk-11-jdk wget
!apt-get install -y autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
!pip install buildozer
!pip install cython==0.29.33

# ========== Cell 3: 切换到项目目录 ==========
import os
os.chdir('/content/drive/MyDrive/android_version')
!pwd
!ls -la

# ========== Cell 4: 初始化Buildozer（首次） ==========
!buildozer init

# ========== Cell 5: 构建APK ==========
!buildozer -v android debug

# ========== Cell 6: 查找并下载APK ==========
!find . -name "*.apk"
from google.colab import files

# 下载APK（找到生成的APK文件路径）
apk_path = !find . -name "*.apk" | head -1
if apk_path:
    print(f"Found APK: {apk_path[0]}")
    files.download(apk_path[0])
else:
    print("APK not found!")
```

### 预计时间
- 首次构建: 30-60分钟（需要下载Android SDK和NDK）
- 后续构建: 5-10分钟

---

## 方法2: 使用WSL（Windows子系统）

### 步骤1: 安装WSL

在PowerShell（管理员）中运行：
```powershell
wsl --install
```

重启电脑后，打开Ubuntu。

### 步骤2: 在WSL中安装依赖

```bash
# 更新系统
sudo apt update && sudo apt upgrade -y

# 安装Python和pip
sudo apt install python3 python3-pip -y

# 安装Java
sudo apt install openjdk-11-jdk -y

# 安装构建工具
sudo apt install -y git zip unzip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

# 安装Buildozer
pip3 install buildozer
pip3 install cython==0.29.33
```

### 步骤3: 复制项目到WSL

```bash
# 在WSL中访问Windows文件
cd ~
mkdir projects
cd projects

# 从Windows复制文件
cp -r /mnt/c/Users/Martin/Desktop/FactionGame/android_version ./
cd android_version
```

### 步骤4: 构建APK

```bash
# 构建debug版本
buildozer -v android debug

# APK将生成在 bin/ 目录
ls -lh bin/
```

### 步骤5: 复制APK到Windows

```bash
# 复制到Windows桌面
cp bin/*.apk /mnt/c/Users/Martin/Desktop/
```

---

## 方法3: 使用Linux虚拟机

### 使用VirtualBox或VMware
1. 安装Ubuntu虚拟机
2. 按照WSL的步骤安装依赖
3. 使用共享文件夹传输APK

---

## 📋 buildozer.spec 配置检查

确保您的 `buildozer.spec` 包含以下配置：

```ini
[app]
title = Faction Game
package.name = factiongame
package.domain = org.factiongame
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp4
version = 1.0

# 包含视频文件
source.include_patterns = *.mp4

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.archs = arm64-v8a, armeabi-v7a
android.api = 31
android.minapi = 21
android.ndk = 25b

# 全屏设置
android.theme = @android:style/Theme.NoTitleBar.Fullscreen
orientation = portrait
fullscreen = 1

# Python版本和依赖
requirements = python3,kivy==2.2.1,ffpyplayer

[buildozer]
log_level = 2
warn_on_root = 1
```

---

## 🎯 快速打包脚本（Google Colab）

复制整个脚本到Colab一个Cell中：

```python
# 完整的一键打包脚本
from google.colab import drive, files
import os

# 1. 挂载Drive
drive.mount('/content/drive')

# 2. 安装依赖
print("📦 Installing dependencies...")
!apt-get update -qq
!apt-get install -y -qq git zip unzip openjdk-11-jdk wget autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
!pip install -q buildozer cython==0.29.33

# 3. 切换到项目目录
print("\n📂 Navigating to project...")
os.chdir('/content/drive/MyDrive/android_version')

# 4. 构建APK
print("\n🔨 Building APK...")
!buildozer -v android debug

# 5. 下载APK
print("\n⬇️ Downloading APK...")
apk_files = !find bin -name "*.apk"
if apk_files:
    print(f"✅ Found: {apk_files[0]}")
    files.download(apk_files[0])
else:
    print("❌ APK not found!")
```

---

## 📱 安装到平板

### 方法1: USB传输
1. 用USB线连接平板和电脑
2. 将APK复制到平板
3. 在平板上找到APK文件并安装

### 方法2: 云盘传输
1. 上传APK到百度云盘/Google Drive
2. 在平板上下载
3. 安装

### 方法3: 微信/QQ传输
1. 将APK发送给自己
2. 在平板上接收
3. 安装

### 方法4: ADB安装
```powershell
# 启用平板开发者模式和USB调试
adb connect <平板IP>
adb install -r FactionGame.apk
```

---

## ⚙️ 安装前准备（平板设置）

### 1. 启用开发者选项
- 设置 → 关于平板 → 连续点击"版本号"7次

### 2. 允许安装未知应用
- 设置 → 安全 → 未知来源 → 开启

### 3. 文件权限
- 安装时允许所有权限请求

---

## 🐛 常见问题

### Q: Buildozer下载太慢
A: 使用国内镜像或VPN

### Q: 构建失败
A: 查看详细日志
```bash
buildozer -v android debug 2>&1 | tee build.log
```

### Q: APK太大
A: 压缩视频文件
```bash
ffmpeg -i hand.mp4 -vcodec h264 -b:v 1000k hand_compressed.mp4
```

### Q: 平板无法安装
A: 检查：
- Android版本 >= 5.0
- 存储空间 >= 100MB
- 已允许未知来源

---

## 📊 构建时间估算

| 环境 | 首次构建 | 后续构建 |
|------|----------|----------|
| Google Colab | 40-60分钟 | 5-10分钟 |
| WSL | 50-70分钟 | 5-10分钟 |
| Linux VM | 60-90分钟 | 10-15分钟 |

---

## ✅ 成功标志

构建成功会看到：
```
# BUILD SUCCESSFUL
# APK location: bin/factiongame-1.0-arm64-v8a-debug.apk
```

---

## 🎉 完成后

1. ✅ 下载APK文件
2. ✅ 传输到iQOO Pad2 Pro
3. ✅ 安装并测试
4. ✅ 享受游戏！

建议使用 **Google Colab**，最简单快速！
