# 🎬 hand.mp4 视频说明

## 📹 视频要求

### 文件位置
将 `hand.mp4` 文件放在以下位置：
```
android_version/
├── main.py
├── rusher.mp4
├── defender.mp4
└── hand.mp4          ← 手掌引导视频
```

### 视频规格建议

#### 基本要求
- **格式**: MP4 (H.264编码)
- **分辨率**: 500×500 像素（正方形）
- **时长**: 2-5秒（会自动循环播放）
- **背景**: 透明或黑色背景
- **文件大小**: <5MB

#### 推荐参数
```
分辨率: 500×500 或 1000×1000 (高清)
帧率: 30fps
码率: 1000-2000 kbps
音频: 无需音频（或静音）
```

### 内容建议

手掌视频应该展示：
1. **手掌图形/动画** - 清晰的手掌轮廓
2. **引导动作** - 可以是：
   - 手掌从下方移入的动作
   - 手掌缓慢放大/缩小
   - 手掌发光效果
   - 手掌旋转
   - 手指点击动作

3. **视觉效果**
   - 建议使用蓝色或白色
   - 可以添加发光效果
   - 可以添加粒子效果

## 🎨 视频制作工具

### 在线工具
- **Canva** - https://www.canva.com/ (有手势图标)
- **Adobe Express** - 简单的视频编辑

### 专业软件
- **After Effects** - 专业动效制作
- **Blender** - 3D手掌动画
- **DaVinci Resolve** - 免费视频编辑

### AI生成
- **RunwayML** - AI视频生成
- **Stable Diffusion + AnimateDiff** - AI动画

## 🔄 程序逻辑

### 启动界面
```python
if hand.mp4 存在:
    显示 hand.mp4 视频（循环播放）
else:
    显示蓝色手掌图形（原有设计）
```

### 视频特性
- ✅ 自动循环播放
- ✅ 500×500 像素大小
- ✅ 居中显示
- ✅ 覆盖透明点击区域（600×600）

## 📱 显示效果

```
┌─────────────────────────────┐
│   将你的手放在屏幕上         │
│   开始抽取你的阵营           │
│                             │
│      [hand.mp4]             │
│    (500×500 循环播放)        │
│                             │
│      👆 触摸开始             │
└─────────────────────────────┘
```

## 🎯 使用FFmpeg转换视频

如果你有其他格式的视频，可以用FFmpeg转换：

```bash
# 转换为500×500正方形视频
ffmpeg -i input.mp4 -vf "scale=500:500:force_original_aspect_ratio=decrease,pad=500:500:(ow-iw)/2:(oh-ih)/2" -c:v libx264 -crf 23 -preset medium -an hand.mp4

# 如果需要循环短视频
ffmpeg -stream_loop 3 -i short.mp4 -c copy hand.mp4
```

## 🖼️ 如果没有hand.mp4

程序会自动使用备用方案：
- 显示蓝色手掌图形（HandButton类）
- 带脉动动画效果
- 功能完全一样

## ✨ 优化建议

### 高质量视频
```
分辨率: 1000×1000
码率: 3000 kbps
帧率: 60fps
```

### 标准质量
```
分辨率: 500×500
码率: 1500 kbps
帧率: 30fps
```

### 压缩版本
```
分辨率: 500×500
码率: 800 kbps
帧率: 24fps
```

## 📦 文件清单

完整的项目文件：
```
android_version/
├── main.py              ✅ 主程序
├── buildozer.spec       ✅ 打包配置
├── hand.mp4            📹 手掌引导视频
├── rusher.mp4          📹 潜入者视频
├── defender.mp4        📹 保卫者视频
└── README.md           📝 说明文档
```

## 🎬 示例脚本

### 创建简单的手掌动画（Python + PIL）

```python
from PIL import Image, ImageDraw
import os

# 创建500×500的图片序列
for i in range(30):
    img = Image.new('RGBA', (500, 500), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 计算缩放
    scale = 1.0 + 0.15 * (i / 30)
    
    # 绘制手掌圆形
    size = int(200 * scale)
    x = 250 - size // 2
    y = 250 - size // 2
    draw.ellipse([x, y, x + size, y + size], fill=(51, 153, 255, 230))
    
    img.save(f'frame_{i:03d}.png')

# 使用FFmpeg合成视频
os.system('ffmpeg -framerate 30 -i frame_%03d.png -c:v libx264 -pix_fmt yuv420p hand.mp4')
```

## 🚀 现在可以做的

1. ✅ 将 `hand.mp4` 放入 `android_version/` 目录
2. ✅ 运行程序测试效果
3. ✅ 如果满意，打包为APK
4. ✅ 在平板上安装使用

程序已经完全支持 `hand.mp4` 视频！🎉
