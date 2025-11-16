# 📱 打包APK到iQOO Pad2 Pro - 完整指南

## 🎯 准备工作（5分钟）

### 第一步：上传文件到Google Drive

1. **打开Google Drive**：https://drive.google.com
2. **创建文件夹**：在"我的云端硬盘"中创建名为 `FactionGame` 的文件夹
3. **上传这6个文件**：
   - ✅ `main.py` （主程序）
   - ✅ `buildozer.spec` （打包配置）
   - ✅ `hand.png` （手型图片）
   - ✅ `bg.png` （背景图片）
   - ✅ `rusher.mp4` （进攻方视频）
   - ✅ `defender.mp4` （防守方视频）

---

## 🔨 打包APK（30-50分钟，全自动）

### 第二步：使用Google Colab打包

1. **打开Google Colab**：
   - 访问：https://colab.research.google.com/
   - 点击"新建笔记本"

2. **复制打包脚本**：
   - 打开项目中的 `一键打包APK.py` 文件（用记事本打开）
   - **全选复制所有内容**（Ctrl+A，然后Ctrl+C）
   - **粘贴到Colab代码单元格**（Ctrl+V）

3. **修改Drive路径**（重要！）：
   在代码中找到这一行：
   ```python
   project_path = '/content/drive/MyDrive/FactionGame'
   ```
   
   如果您的文件夹路径不同，请修改为实际路径，例如：
   ```python
   project_path = '/content/drive/MyDrive/我的项目/FactionGame'
   ```

4. **运行脚本**：
   - 点击代码单元格左侧的▶️播放按钮（或按Shift+Enter）
   - 会弹出授权窗口，点击"连接到Google云端硬盘"
   - 选择您的Google账号并授权

5. **等待构建完成**：
   - ⏰ **首次构建**：30-50分钟（需要下载Android SDK、NDK等，约3-4GB）
   - ⏰ **后续构建**：10-20分钟
   - 💡 可以最小化窗口去做其他事，不影响构建

6. **下载APK**：
   - 构建完成后，浏览器会自动下载APK文件
   - 文件名类似：`factiongame-1.0-arm64-v8a-debug.apk`
   - 大小约：40-60 MB

---

## 📲 安装到iQOO Pad2 Pro（5分钟）

### 第三步：传输APK到平板

**方法1：USB传输**（推荐）
1. 用USB线连接电脑和平板
2. 在电脑上找到下载的APK文件
3. 复制到平板的"下载"文件夹

**方法2：无线传输**
1. 通过QQ、微信、钉钉等发送给自己
2. 在平板上接收文件

### 第四步：安装APK

1. **允许未知来源**：
   - 打开平板 **设置 → 安全与隐私 → 更多安全设置**
   - 找到"安装未知应用"
   - 允许文件管理器或浏览器安装应用

2. **安装APK**：
   - 在平板上打开"文件管理"
   - 找到下载的APK文件
   - 点击安装
   - 等待安装完成

3. **运行测试**：
   - 在桌面找到"Faction Game"图标
   - 点击打开
   - 应该会全屏显示！

---

## 🎮 iQOO Pad2 Pro专属优化

您的APK已针对iQOO Pad2 Pro进行优化：

✅ **全屏显示**：无状态栏、无导航栏
✅ **分辨率适配**：自动适配 3096×2064 分辨率
✅ **竖屏锁定**：始终竖屏显示
✅ **硬件加速**：启用GPU加速，流畅运行
✅ **架构优化**：arm64-v8a（完美兼容骁龙8 Gen3）

---

## 🐛 常见问题解决

### Q1: Colab构建失败，提示"Command failed"或下载错误
**解决方法**：
- 这是网络问题，直接**重新运行脚本**即可
- Buildozer会从断点继续，不会重新下载
- 如果多次失败，在Colab中运行：
  ```python
  !rm -rf /content/drive/MyDrive/FactionGame/.buildozer
  ```
  然后重新运行脚本

### Q2: 找不到APK文件
**检查方法**：
在Colab中运行：
```python
!find /content/drive/MyDrive/FactionGame -name "*.apk"
```

### Q3: 平板安装时提示"解析包错误"
**原因**：APK下载不完整
**解决**：
- 检查APK文件大小（应该40MB以上）
- 重新下载APK

### Q4: 应用安装后闪退
**检查清单**：
- ✅ 所有6个文件都上传了吗？
- ✅ 视频文件是MP4格式吗？
- ✅ 图片文件是PNG格式吗？

**查看日志**：
在平板上使用ADB查看日志：
```bash
adb logcat | grep python
```

### Q5: 应用不是全屏，还能看到状态栏
**解决方法**：
- 在iQOO设置中：**设置 → 显示 → 全屏显示**
- 找到"Faction Game"，选择"全屏显示"

---

## ⚡ 快速重新打包（修改代码后）

如果您修改了代码，想快速重新打包：

1. 更新Google Drive中的 `main.py` 文件
2. 在Colab中运行：

```python
from google.colab import drive
drive.mount('/content/drive')

import os
os.chdir('/content/drive/MyDrive/FactionGame')

# 清理并重建
!rm -rf .buildozer/android/platform/build-arm64-v8a/dists/factiongame
!buildozer android debug

# 下载新APK
from google.colab import files
import glob
apk = glob.glob('./bin/*.apk')[0]
files.download(apk)
```

只需10-15分钟即可完成！

---

## 📊 技术规格

| 项目 | 配置 |
|------|------|
| 包名 | org.factiongame.factiongame |
| 版本 | 1.0 |
| 分辨率 | 自动适配（支持3096×2064） |
| 方向 | 竖屏锁定 |
| 全屏 | 是（无状态栏、无导航栏） |
| 架构 | arm64-v8a（骁龙8 Gen3原生支持） |
| Android版本 | 最低5.0，目标12.0 |
| 视频播放 | ffpyplayer（硬件解码） |

---

## 🎉 完成！

按照以上步骤，您将获得一个专为iQOO Pad2 Pro优化的APK，可以完美全屏运行！

有任何问题，请检查上面的"常见问题解决"部分。



