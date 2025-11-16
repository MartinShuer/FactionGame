# 安卓版本快速开始指南

## 第一步：在电脑上测试

### Windows系统测试

1. **安装Kivy**
   ```powershell
   pip install kivy
   ```

2. **复制视频文件**
   - 将 `rusher.mp4` 复制到 `android_version/` 目录
   - 将 `defender.mp4` 复制到 `android_version/` 目录

3. **运行程序**
   ```powershell
   cd C:\Users\Martin\Desktop\FactionGame\android_version
   python main.py
   ```

## 第二步：打包为安卓APK

### 选项A: 使用Google Colab（最简单，推荐）

1. 打开 Google Colab: https://colab.research.google.com/
2. 创建新笔记本
3. 运行以下代码：

```python
# 安装Buildozer
!pip install buildozer
!pip install cython==0.29.33

# 安装系统依赖
!sudo apt-get update
!sudo apt-get install -y git zip unzip openjdk-11-jdk wget
!sudo apt-get install -y autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

# 克隆或上传你的项目文件
# 上传 main.py, buildozer.spec, rusher.mp4, defender.mp4

# 构建APK
!buildozer -v android debug

# 下载生成的APK
from google.colab import files
files.download('bin/factiongame-1.0-arm64-v8a-debug.apk')
```

### 选项B: 使用WSL（Windows用户）

1. **安装WSL2**
   ```powershell
   wsl --install
   ```

2. **在WSL中安装Ubuntu**
   ```bash
   # 更新系统
   sudo apt update && sudo apt upgrade -y
   
   # 安装Python和pip
   sudo apt install python3 python3-pip -y
   
   # 安装Buildozer
   pip3 install buildozer
   
   # 安装依赖
   sudo apt install -y git zip unzip openjdk-11-jdk autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
   ```

3. **复制文件到WSL**
   ```bash
   # 在WSL中访问Windows文件
   cd /mnt/c/Users/Martin/Desktop/FactionGame/android_version
   
   # 构建APK
   buildozer -v android debug
   ```

### 选项C: 使用Linux虚拟机

1. 安装VirtualBox或VMware
2. 安装Ubuntu虚拟机
3. 按照WSL步骤操作

## 第三步：安装到手机

1. **启用开发者选项**
   - 设置 → 关于手机 → 连续点击版本号7次

2. **启用未知来源安装**
   - 设置 → 安全 → 允许安装未知应用

3. **传输APK到手机**
   - 通过USB数据线传输
   - 或通过微信/QQ发送给自己
   - 或通过云盘下载

4. **安装APK**
   - 在手机上打开APK文件
   - 点击安装
   - 授予必要权限

## 常见问题

### Q: 视频文件太大，APK体积太大怎么办？
A: 使用视频压缩工具压缩视频：
- 在线工具: https://www.freeconvert.com/video-compressor
- 桌面工具: HandBrake, FFmpeg
- 建议参数: 720p分辨率，H.264编码，比特率2000kbps

### Q: 能不能不打包视频到APK中？
A: 可以，修改代码从网络下载视频或从SD卡读取

### Q: 打包时间太长怎么办？
A: 首次打包需要下载Android SDK和NDK，大约需要30-60分钟。后续打包会快很多。

### Q: 如何调试APK？
A: 使用 `buildozer android debug deploy run logcat` 命令连接手机调试

## 视频压缩命令（使用FFmpeg）

```bash
# 安装FFmpeg
# Windows: 从 https://ffmpeg.org/download.html 下载

# 压缩视频到适合移动设备的大小
ffmpeg -i rusher.mp4 -vcodec h264 -acodec aac -vf scale=720:-2 -b:v 2000k rusher_compressed.mp4
ffmpeg -i defender.mp4 -vcodec h264 -acodec aac -vf scale=720:-2 -b:v 2000k defender_compressed.mp4
```

## 进阶修改

### 添加声音效果
```python
from kivy.core.audio import SoundLoader
sound = SoundLoader.load('click.wav')
if sound:
    sound.play()
```

### 添加震动反馈
```python
from jnius import autoclass
PythonActivity = autoclass('org.kivy.android.PythonActivity')
activity = PythonActivity.mActivity
Context = autoclass('android.content.Context')
vibrator = activity.getSystemService(Context.VIBRATOR_SERVICE)
vibrator.vibrate(100)  # 震动100毫秒
```

### 保存历史记录
```python
import json
from kivy.storage.jsonstore import JsonStore
store = JsonStore('faction_history.json')
store.put('last_game', faction=self.current_faction)
```

## 支持

如有问题，请检查：
1. README.md - 完整文档
2. Kivy官方文档: https://kivy.org/doc/stable/
3. Buildozer文档: https://buildozer.readthedocs.io/
