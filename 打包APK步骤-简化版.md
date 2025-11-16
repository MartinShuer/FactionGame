# 📱 打包APK到iQOO Pad2 Pro - 最简单方法

## 🎯 方法：使用Google Colab（免费，无需安装任何软件）

### 第一步：准备文件

将这些文件上传到您的Google Drive（创建一个名为 `FactionGame` 的文件夹）：

```
必需文件（6个）：
✓ main.py              （主程序）
✓ buildozer.spec       （打包配置）
✓ hand.png            （手型图片）
✓ bg.png              （背景图片）
✓ rusher.mp4          （进攻方视频）
✓ defender.mp4        （防守方视频）
```

### 第二步：打开Google Colab并运行

**⚠️ 重要：不要复制 markdown 代码块标记（```python 和 ```）**

1. **打开网址**：https://colab.research.google.com/
2. **创建新笔记本**：点击 "新建笔记本"
3. **打开准备好的脚本**：
   - 在项目文件夹中找到 `colab_build_script.py`
   - 用记事本打开，全选复制（Ctrl+A, Ctrl+C）
   - 粘贴到 Colab 的代码单元格中
   
   **或者直接复制下面的代码（从 # 开始，不要复制 ```）：**

# ========== 完整一键打包脚本 ==========

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


4. **点击运行按钮**（或按 Shift+Enter）

   **✅ 正确示例**：代码单元格应该像这样开始
   ```
   # ========== 完整一键打包脚本 ==========
   from google.colab import drive
   ```

   **❌ 错误示例**：不要包含这些
   ```
   ```python          ← 不要这行
   ```               ← 不要这行
   ```

5. **授权Google Drive**：
   - 会弹出授权窗口
   - 点击 "连接到Google云端硬盘"
   - 选择您的Google账号并授权

6. **等待构建完成**：
   - 首次构建需要 30-50 分钟（会下载Android SDK等）
   - 后续构建只需 10-20 分钟
   - 可以看到构建进度

7. **下载APK**：
   - 构建完成后会自动下载 `factiongame-1.0-arm64-v8a_armeabi-v7a-debug.apk`
   - 如果自动下载失败，在左侧文件浏览器中找到 `bin/*.apk` 手动下载

### 第三步：安装到iQOO Pad2 Pro

1. **传输APK**：
   - 通过USB连接电脑和平板
   - 或者通过QQ/微信发送给自己

2. **安装APK**：
   - 在平板上找到APK文件
   - 点击安装
   - 如果提示"未知来源"，去设置中允许安装未知应用

3. **运行测试**：
   - 打开 "Faction Game" 应用
   - 测试手型动画和阵营选择

---

## 🐛 常见问题

### Q: 构建失败，提示 "Command failed" 或下载子模块错误
**A:** 这是网络问题！解决方法：

**方案1：使用稳定版脚本（推荐）**
使用项目中的 `colab_build_script_v2.py`：
- 只构建 arm64-v8a（更快，兼容所有现代设备）
- 使用 Kivy 2.3.0（更稳定）
- 优化了网络超时设置

**方案2：重新运行原脚本**
直接重新运行即可，Buildozer 会从断点继续下载。

**方案3：如果多次失败**
在 Colab 中运行这个命令清理后重试：
```python
!rm -rf /content/drive/MyDrive/FactionGame/.buildozer
```
然后重新运行构建脚本。

### Q: 找不到APK文件
**A:** 检查 `bin` 目录（在Colab中运行）：

!ls -la bin/


### Q: 首次构建太慢
**A:** 正常现象，需要下载：
- Android SDK (2-3 GB)
- NDK (1-2 GB)
- Python-for-Android 工具链
后续构建会快很多。

### Q: 平板上无法安装
**A:** 
1. 检查平板设置 → 安全 → 允许未知来源
2. 确保APK文件完整（不小于 30MB）

### Q: 应用闪退
**A:** 
1. 检查所有文件都已包含（6个文件）
2. 视频格式是否正确（MP4，H.264编码）
3. 查看Logcat日志排查错误

---

## ⚡ 快速重新打包

如果修改了代码，只需运行（不要复制 ```python 标记）：

# 挂载Drive
from google.colab import drive
drive.mount('/content/drive')

# 切换目录
import os
os.chdir('/content/drive/MyDrive/FactionGame')

# 清理并重新构建
!rm -rf .buildozer/android/platform/build-arm64-v8a_armeabi-v7a/dists/factiongame
!buildozer android debug

# 下载新APK
from google.colab import files
import glob
apk = glob.glob('./bin/*.apk')[0]
files.download(apk)


---

## 📊 当前项目配置

- **包名**: org.factiongame.factiongame
- **版本**: 1.0
- **方向**: 竖屏全屏
- **分辨率**: 自动适配 iQOO Pad2 Pro (3096×2064)
- **架构**: arm64-v8a, armeabi-v7a
- **API**: 31 (Android 12)，最低21 (Android 5.0)

---

## 🎉 完成！

构建成功后，您会得到一个可以直接安装到平板的APK文件！
