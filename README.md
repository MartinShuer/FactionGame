# 阵营选择游戏 - 安卓版本

这是原始Pygame版本的安卓移植版，使用Kivy框架开发。

## 功能特性

- ✅ 随机抽取潜入者(Rusher)或保卫者(Defender)阵营
- ✅ 播放对应阵营的视频动画
- ✅ 支持安卓手机和平板设备
- ✅ 触摸屏友好的界面设计
- ✅ 全屏显示支持

## 文件结构

```
android_version/
├── main.py              # 主程序文件
├── buildozer.spec       # Buildozer打包配置
├── requirements.txt     # Python依赖
├── README.md           # 说明文档
├── rusher.mp4          # 潜入者视频（需要自行添加）
└── defender.mp4        # 保卫者视频（需要自行添加）
```

## 安装方法

### 方法1: 在电脑上测试运行（推荐先测试）

1. 安装Python 3.8+
2. 安装Kivy:
   ```bash
   pip install kivy
   ```
3. 将 `rusher.mp4` 和 `defender.mp4` 放在 `android_version` 目录中
4. 运行程序:
   ```bash
   python main.py
   ```

### 方法2: 打包为安卓APK

#### 在Linux系统上打包（推荐）

1. 安装Buildozer:
   ```bash
   pip install buildozer
   ```

2. 安装依赖（Ubuntu/Debian）:
   ```bash
   sudo apt update
   sudo apt install -y git zip unzip openjdk-11-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
   ```

3. 初始化Buildozer（如果需要）:
   ```bash
   buildozer init
   ```

4. 构建APK:
   ```bash
   buildozer -v android debug
   ```

5. APK文件将生成在 `bin/` 目录中

#### 使用WSL在Windows上打包

1. 安装WSL2 (Windows Subsystem for Linux)
2. 在WSL中安装Ubuntu
3. 按照Linux打包步骤操作

#### 使用在线服务打包

可以使用以下在线服务：
- [Kivy Buildozer Online](https://kivy.org/)
- [Google Colab](https://colab.research.google.com/) + Buildozer

## 将视频添加到APK中

将 `rusher.mp4` 和 `defender.mp4` 放在 `android_version/` 目录中，Buildozer会自动将它们打包到APK中。

**注意事项：**
- 视频文件不要太大（建议每个<20MB）
- 建议使用H.264编码的MP4格式
- 分辨率建议720p或1080p

## 在手机上安装

1. 将生成的APK文件传输到手机
2. 在手机上启用"未知来源应用安装"
3. 打开APK文件进行安装

## 使用说明

1. 打开应用
2. 点击"开始抽取阵营"按钮
3. 查看抽取结果和视频动画
4. 可以点击"重新抽取"继续游戏
5. 点击"返回主菜单"回到首页

## 自定义修改

### 修改阵营名称

在 `main.py` 中找到这些行：
```python
faction_text = '潜入者 (Rusher)'
faction_text = '保卫者 (Defender)'
```

### 修改颜色主题

修改颜色代码（RGBA格式，0-1范围）：
```python
faction_color = (1, 0.2, 0.2, 1)  # 红色
faction_color = (0.2, 0.6, 1, 1)  # 蓝色
```

### 添加更多阵营

在 `start_game` 方法中修改：
```python
self.current_faction = random.choice(['rusher', 'defender', 'new_faction'])
```

然后在 `show_result` 方法中添加对应的处理逻辑。

## 故障排除

### 视频无法播放
- 确认视频文件格式为MP4（H.264编码）
- 检查文件名是否正确（rusher.mp4, defender.mp4）
- 尝试减小视频文件大小

### APK安装失败
- 确保已启用"未知来源应用安装"
- 检查手机系统版本（需要Android 5.0+）
- 尝试卸载旧版本后重新安装

### 应用闪退
- 检查buildozer日志文件
- 确认所有依赖都已正确打包
- 尝试在模拟器中测试

## 技术栈

- **Kivy**: 跨平台Python GUI框架
- **Buildozer**: 安卓打包工具
- **Python 3**: 编程语言

## 与原版的区别

| 特性 | 原版(Pygame) | 安卓版(Kivy) |
|------|-------------|--------------|
| 平台 | Windows | Android/iOS/Windows/Linux |
| 界面 | 窗口模式/全屏 | 触摸屏友好 |
| 视频 | MoviePy | Kivy Video |
| 打包 | PyInstaller | Buildozer |

## 开发者信息

基于原始的Pygame版本重新开发，适配移动平台。

## 许可证

与原项目保持一致。
