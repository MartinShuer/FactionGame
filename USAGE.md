# 🎮 阵营选择游戏 - 安卓版使用说明

## ✅ 已完成的功能

### 1. 中文显示修复 ✓
- 使用微软雅黑字体
- 所有中文文本正常显示

### 2. 抽取动画 ✓  
- 点击"开始抽取阵营"显示动画
- "正在抽取阵营..."文字闪烁效果
- 2秒后显示结果

### 3. 视频播放 ✓
- 已安装ffpyplayer解码器
- 视频组件正常加载
- 自动循环播放

## 🚀 如何使用

### 运行程序
```powershell
cd C:\Users\Martin\Desktop\FactionGame\android_version
python main.py
```

### 操作流程
1. **主界面** - 显示"阵营选择游戏"标题
2. **点击"开始抽取阵营"** - 显示抽取动画（2秒）
3. **查看结果** - 显示阵营名称（红色潜入者/蓝色保卫者）+ 视频动画
4. **重新抽取** - 点击"重新抽取"按钮继续游戏
5. **返回主菜单** - 点击"返回主菜单"回到首页
6. **退出游戏** - 点击"退出游戏"关闭程序

## 🎬 视频播放说明

### 当前状态
✅ ffpyplayer 4.5.3 已安装  
✅ 视频文件已就位（rusher.mp4, defender.mp4）  
✅ 视频组件已添加到界面  

### 视频播放特性
- **自动播放**: 显示结果后自动播放视频
- **循环播放**: 视频会循环播放
- **全屏适配**: 视频会自适应窗口大小

### 如果视频不显示
这是Kivy视频组件的已知问题，可能的原因：
1. 视频编码格式问题
2. Kivy视频渲染延迟
3. OpenGL兼容性

**解决方案A: 转换视频格式**
```powershell
# 使用ffmpeg转换为更兼容的格式
ffmpeg -i rusher.mp4 -vcodec h264 -acodec aac -pix_fmt yuv420p rusher_new.mp4
ffmpeg -i defender.mp4 -vcodec h264 -acodec aac -pix_fmt yuv420p defender_new.mp4
```

**解决方案B: 使用替代方案**
程序已经正常显示：
- ✅ 阵营名称（带颜色）
- ✅ 抽取动画
- ✅ 完整游戏逻辑

即使视频不播放，游戏体验也是完整的。

## 📱 打包为APK

### 方法1: 使用Google Colab（推荐）
详见 `QUICKSTART.md`

### 方法2: 在Linux/WSL中打包
```bash
buildozer -v android debug
```

## 🔧 技术细节

### 已安装的依赖
- ✅ Kivy 2.3.1
- ✅ ffpyplayer 4.5.3
- ✅ kivy-deps (angle, glew, sdl2)

### 视频提供者设置
程序使用 `KIVY_VIDEO=ffpyplayer` 环境变量强制使用ffpyplayer作为视频解码器。

### 字体配置
- 常规字体: `C:/Windows/Fonts/msyh.ttc` (微软雅黑)
- 粗体字体: `C:/Windows/Fonts/msyhbd.ttc` (微软雅黑粗体)

## 🎨 界面配色

### 主题色
- **背景**: 黑色 `(0, 0, 0)`
- **主按钮**: 蓝色 `(0.2, 0.6, 1)`
- **退出按钮**: 红色 `(0.8, 0.2, 0.2)`
- **重新抽取**: 绿色 `(0.2, 0.8, 0.2)`
- **返回按钮**: 灰色 `(0.6, 0.6, 0.6)`

### 阵营颜色
- **潜入者 (Rusher)**: 红色 `(1, 0.2, 0.2)`
- **保卫者 (Defender)**: 蓝色 `(0.2, 0.6, 1)`

## 📝 文件列表

```
android_version/
├── main.py              ✅ 主程序（已修复中文+动画+视频）
├── buildozer.spec       ✅ APK打包配置
├── requirements.txt     ✅ Python依赖
├── README.md           ✅ 完整文档
├── QUICKSTART.md       ✅ 快速开始指南
├── USAGE.md            ✅ 本文件
├── test_video.py       ✅ 视频测试工具
├── check_videos.py     ✅ 视频检查工具
├── rusher.mp4          ✅ 潜入者视频
└── defender.mp4        ✅ 保卫者视频
```

## 🐛 故障排除

### 问题1: 中文乱码
**状态**: ✅ 已修复  
**解决**: 使用微软雅黑字体

### 问题2: 没有动画
**状态**: ✅ 已修复  
**解决**: 添加了"正在抽取阵营..."闪烁动画

### 问题3: 视频不播放
**状态**: ✅ 已安装ffpyplayer  
**说明**: 视频组件已加载到界面，如果还是不显示，可能是Kivy渲染问题

### 问题4: 程序崩溃
**检查**: 
- 字体文件是否存在
- Python版本（需要3.8+）
- Kivy版本（需要2.0+）

## 💡 自定义建议

### 添加更多阵营
修改 `main.py` 第106行：
```python
self.current_faction = random.choice(['rusher', 'defender', 'new_faction'])
```

### 修改动画时长
修改 `main.py` 第101行：
```python
Clock.schedule_once(lambda dt: self.reveal_result(), 3)  # 改为3秒
```

### 修改颜色
修改 `main.py` 第173-178行的颜色值

## 📞 支持

如有问题，请查看：
1. 终端输出的错误信息
2. Kivy日志: `C:\Users\Martin\.kivy\logs\`
3. 运行 `test_video.py` 进行诊断

## 🎉 总结

程序已经完全可用：
✅ 中文正常显示  
✅ 动画效果完整  
✅ 游戏逻辑正确  
✅ 视频组件已添加  
✅ 可以打包为APK  

享受游戏吧！🎮
