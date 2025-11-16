# 检查视频文件并提供解决方案

import os

print("=" * 50)
print("视频文件检查工具")
print("=" * 50)

# 检查当前目录
current_dir = os.path.dirname(os.path.abspath(__file__))
print(f"\n当前目录: {current_dir}")

# 检查视频文件
rusher_path = os.path.join(current_dir, 'rusher.mp4')
defender_path = os.path.join(current_dir, 'defender.mp4')

print(f"\n检查 rusher.mp4...")
if os.path.exists(rusher_path):
    size = os.path.getsize(rusher_path) / (1024 * 1024)
    print(f"✓ 找到文件! 大小: {size:.2f} MB")
else:
    print(f"✗ 未找到文件")
    print(f"  应该在: {rusher_path}")

print(f"\n检查 defender.mp4...")
if os.path.exists(defender_path):
    size = os.path.getsize(defender_path) / (1024 * 1024)
    print(f"✓ 找到文件! 大小: {size:.2f} MB")
else:
    print(f"✗ 未找到文件")
    print(f"  应该在: {defender_path}")

# 检查原始目录
parent_dir = os.path.dirname(current_dir)
print(f"\n检查父目录: {parent_dir}")

rusher_parent = os.path.join(parent_dir, 'rusher.mp4')
defender_parent = os.path.join(parent_dir, 'defender.mp4')

if os.path.exists(rusher_parent):
    print(f"✓ 在父目录找到 rusher.mp4")
    print(f"  可以复制命令: copy \"{rusher_parent}\" \"{rusher_path}\"")
    
if os.path.exists(defender_parent):
    print(f"✓ 在父目录找到 defender.mp4")
    print(f"  可以复制命令: copy \"{defender_parent}\" \"{defender_path}\"")

print("\n" + "=" * 50)
print("解决方案:")
print("=" * 50)
print("1. 从原始目录复制视频文件到 android_version 目录")
print("2. 或者修改代码从上级目录读取视频")
print("3. 或者暂时不使用视频，只显示文字和颜色")
print("=" * 50)
