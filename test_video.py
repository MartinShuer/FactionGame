"""
测试视频播放功能
"""
import os
import sys

print("=" * 60)
print("视频播放测试工具")
print("=" * 60)

# 1. 检查视频文件
print("\n[1] 检查视频文件...")
current_dir = os.path.dirname(os.path.abspath(__file__))
rusher_path = os.path.join(current_dir, 'rusher.mp4')
defender_path = os.path.join(current_dir, 'defender.mp4')

rusher_exists = os.path.exists(rusher_path)
defender_exists = os.path.exists(defender_path)

if rusher_exists:
    size = os.path.getsize(rusher_path) / (1024 * 1024)
    print(f"✓ rusher.mp4 存在 ({size:.2f} MB)")
else:
    print(f"✗ rusher.mp4 不存在")

if defender_exists:
    size = os.path.getsize(defender_path) / (1024 * 1024)
    print(f"✓ defender.mp4 存在 ({size:.2f} MB)")
else:
    print(f"✗ defender.mp4 不存在")

# 2. 检查ffpyplayer
print("\n[2] 检查视频解码器...")
try:
    import ffpyplayer
    print(f"✓ ffpyplayer 已安装 (版本: {ffpyplayer.version})")
except ImportError:
    print("✗ ffpyplayer 未安装")
    print("  请运行: pip install ffpyplayer")

# 3. 测试Kivy视频支持
print("\n[3] 检查Kivy视频支持...")
try:
    from kivy.core.video import Video
    print("✓ Kivy Video 模块可用")
except ImportError as e:
    print(f"✗ Kivy Video 模块导入失败: {e}")

# 4. 检查视频提供者
print("\n[4] 检查视频提供者...")
try:
    os.environ['KIVY_VIDEO'] = 'ffpyplayer'
    from kivy import Logger
    Logger.setLevel(1)  # 只显示info及以上级别
    from kivy.app import App
    from kivy.uix.video import Video as VideoWidget
    
    print("✓ Kivy视频组件加载成功")
    print("  提示: 如果视频不播放，可能需要重启程序")
except Exception as e:
    print(f"✗ 视频组件加载失败: {e}")

print("\n" + "=" * 60)
print("测试完成！")
print("=" * 60)

if rusher_exists and defender_exists:
    print("\n建议: 重新运行 main.py 查看视频播放效果")
else:
    print("\n警告: 请确保视频文件在当前目录中")

print("=" * 60)
