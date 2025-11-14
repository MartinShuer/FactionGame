[app]

# 应用名称
title = Faction Game

# 包名
package.name = factiongame

# 包域名
package.domain = org.factiongame

# 源代码目录
source.dir = .

# 源代码包含的文件扩展名
source.include_exts = py,png,jpg,kv,atlas,mp4

# 包含所有视频文件和图片文件
source.include_patterns = *.mp4,*.png

# 应用版本
version = 1.0

# 应用要求的权限
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# 支持的Android架构（仅arm64，适合现代平板，构建更快）
android.archs = arm64-v8a

# Android API版本
android.api = 31

# 最小API版本
android.minapi = 21

# Android NDK版本
android.ndk = 25b

# 是否接受SDK许可
android.accept_sdk_license = True

# 图标路径（如果有的话）
# icon.filename = %(source.dir)s/icon.png

# 启动画面（如果有的话）
# presplash.filename = %(source.dir)s/presplash.png

# Android主题 - 全屏无标题栏（专为平板优化）
android.theme = @android:style/Theme.NoTitleBar.Fullscreen

# 方向设置 (landscape横屏, portrait竖屏, sensor自动)
orientation = portrait

# 全屏显示（隐藏状态栏和导航栏）
fullscreen = 1

# 启用沉浸式全屏模式（iQOO Pad2 Pro优化）
android.manifest.intent_filters = 

# 窗口标志（保持屏幕常亮，全屏显示）
android.add_src = 

# 启用硬件加速
android.manifest.application = android:hardwareAccelerated="true"

# Python版本
python.version = 3

# 要求的Python模块 - 包含ffpyplayer用于视频播放（使用稳定版Kivy）
requirements = python3,kivy==2.3.0,ffpyplayer

# 优化日志
android.logcat_filters = *:S python:D

# 日志等级
log_level = 2

# 警告
warn_on_root = 0


[buildozer]

# 日志等级 (0 = error only, 1 = info, 2 = debug)
log_level = 2

# 警告显示
warn_on_root = 0
