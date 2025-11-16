"""
阵营选择游戏 - 安卓版本
使用 Kivy 框架开发，支持安卓平台
"""

import os
# 设置视频提供者为ffpyplayer（必须在导入kivy之前）
os.environ['KIVY_VIDEO'] = 'ffpyplayer'

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.video import Video
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle, Ellipse, Line
from kivy.core.text import LabelBase
from kivy.uix.widget import Widget
import random

# 注册中文字体（解决中文乱码问题）
# Windows系统使用微软雅黑
LabelBase.register(name='CustomFont',
                  fn_regular='C:/Windows/Fonts/msyh.ttc')  # 微软雅黑
# 如果需要粗体
LabelBase.register(name='CustomFontBold',
                  fn_regular='C:/Windows/Fonts/msyhbd.ttc')  # 微软雅黑粗体


class GlowingHandWidget(FloatLayout):
    """带流光效果的手型图片组件"""
    def __init__(self, hand_image_path, **kwargs):
        super().__init__(**kwargs)
        
        # 获取窗口尺寸
        win_width = Window.width
        win_height = Window.height
        hand_size = min(win_width, win_height) * 1.2  # 手型占屏幕120%（适中大小，有呼吸空间）
        
        print(f"✓ 窗口尺寸: {win_width}x{win_height}, 手型尺寸: {hand_size}")
        
        # 背景发光层（外圈光晕）
        self.glow_layer1 = Image(
            source=hand_image_path,
            size_hint=(None, None),
            size=(hand_size * 1.2, hand_size * 1.2),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            opacity=0.3,
            color=(0.3, 0.8, 1, 1)  # 蓝色光晕
        )
        self.add_widget(self.glow_layer1)
        
        # 中间发光层
        self.glow_layer2 = Image(
            source=hand_image_path,
            size_hint=(None, None),
            size=(hand_size * 1.1, hand_size * 1.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            opacity=0.5,
            color=(0.5, 0.9, 1, 1)  # 浅蓝色光晕
        )
        self.add_widget(self.glow_layer2)
        
        # 主手型图片
        self.hand_image = Image(
            source=hand_image_path,
            size_hint=(None, None),
            size=(hand_size, hand_size),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.add_widget(self.hand_image)
        
        # 保存基础尺寸用于动画
        self.base_size = hand_size
        
        # 启动呼吸脉冲动画
        Clock.schedule_once(lambda dt: self.start_breathing_animation(), 0.1)
        
        # 启动流光动画
        self.glow_phase = 0
        Clock.schedule_interval(self.update_glow, 0.05)
        
        print("✓ GlowingHandWidget 初始化完成")
    
    def start_breathing_animation(self):
        """呼吸感脉冲动画"""
        from kivy.animation import Animation
        
        print("✓ 启动呼吸脉冲动画")
        print(f"  基础尺寸: {self.base_size}")
        print(f"  动画范围: {self.base_size} → {self.base_size * 1.3}")
        
        # 主图片的呼吸效果（更明显的幅度：30%）
        breath_anim = (
            Animation(size=(self.base_size * 1.3, self.base_size * 1.3), duration=1.0, t='in_out_quad') +
            Animation(size=(self.base_size, self.base_size), duration=1.0, t='in_out_quad')
        )
        breath_anim.repeat = True
        
        # 添加动画开始和完成的回调，用于调试
        def on_anim_start(animation, widget):
            print("→ 动画开始放大")
        
        def on_anim_complete(animation, widget):
            print("← 动画缩小完成")
        
        breath_anim.bind(on_start=on_anim_start)
        breath_anim.bind(on_complete=on_anim_complete)
        breath_anim.start(self.hand_image)
        
        # 外层光晕的呼吸效果（更大幅度：40%）
        glow1_anim = (
            Animation(size=(self.base_size * 1.4, self.base_size * 1.4), opacity=0.6, duration=1.2, t='in_out_quad') +
            Animation(size=(self.base_size * 1.2, self.base_size * 1.2), opacity=0.2, duration=1.2, t='in_out_quad')
        )
        glow1_anim.repeat = True
        glow1_anim.start(self.glow_layer1)
        
        # 中层光晕的呼吸效果（35%幅度）
        glow2_anim = (
            Animation(size=(self.base_size * 1.35, self.base_size * 1.35), opacity=0.8, duration=1.1, t='in_out_quad') +
            Animation(size=(self.base_size * 1.1, self.base_size * 1.1), opacity=0.3, duration=1.1, t='in_out_quad')
        )
        glow2_anim.repeat = True
        glow2_anim.start(self.glow_layer2)
    
    def update_glow(self, dt):
        """更新流光效果"""
        import math
        self.glow_phase += 0.1
        
        # 使用正弦波产生颜色渐变效果
        r = 0.3 + 0.4 * math.sin(self.glow_phase)
        g = 0.7 + 0.3 * math.sin(self.glow_phase + 2.0)
        b = 1.0
        
        self.glow_layer1.color = (r, g, b, 1)
        self.glow_layer2.color = (r * 1.2, g * 1.1, b, 1)


class HandButton(Widget):
    """手掌形状的按钮"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            # 绘制手掌
            Color(0.2, 0.6, 1, 0.9)  # 蓝色半透明
            
            # 手掌主体（圆形）
            self.palm = Ellipse(pos=(0, 0), size=(300, 300))
            
            # 五个手指（矩形，圆角效果）
            # 拇指
            self.thumb = Ellipse(pos=(0, 0), size=(60, 120))
            # 食指
            self.index = Ellipse(pos=(0, 0), size=(55, 180))
            # 中指
            self.middle = Ellipse(pos=(0, 0), size=(55, 200))
            # 无名指
            self.ring = Ellipse(pos=(0, 0), size=(55, 175))
            # 小指
            self.pinky = Ellipse(pos=(0, 0), size=(45, 140))
            
            # 添加发光效果
            Color(0.3, 0.7, 1, 0.3)
            self.glow = Ellipse(pos=(0, 0), size=(350, 350))
        
        self.bind(pos=self.update_hand, size=self.update_hand)
        
        # 添加脉动动画
        self.pulse_anim = Clock.schedule_interval(self.pulse, 0.8)
        self.pulse_scale = 1.0
    
    def update_hand(self, *args):
        """更新手掌位置"""
        center_x = self.center_x
        center_y = self.center_y
        base_size = 300
        
        # 脉动效果
        palm_size = base_size * self.pulse_scale
        glow_size = (base_size + 50) * self.pulse_scale
        
        # 发光外圈
        self.glow.pos = (center_x - glow_size/2, center_y - glow_size/2)
        self.glow.size = (glow_size, glow_size)
        
        # 手掌主体
        self.palm.pos = (center_x - palm_size/2, center_y - palm_size/2)
        self.palm.size = (palm_size, palm_size)
        
        # 拇指（左侧）
        self.thumb.pos = (center_x - 180, center_y - 30)
        self.thumb.size = (60, 120)
        
        # 食指（上方偏左）
        self.index.pos = (center_x - 90, center_y + 120)
        self.index.size = (55, 180)
        
        # 中指（上方中间）
        self.middle.pos = (center_x - 27, center_y + 140)
        self.middle.size = (55, 200)
        
        # 无名指（上方偏右）
        self.ring.pos = (center_x + 38, center_y + 120)
        self.ring.size = (55, 175)
        
        # 小指（上方右侧）
        self.pinky.pos = (center_x + 100, center_y + 100)
        self.pinky.size = (45, 140)
    
    def pulse(self, dt):
        """脉动动画效果"""
        if self.pulse_scale >= 1.15:
            self.pulse_scale = 1.0
        else:
            self.pulse_scale += 0.015
        self.update_hand()


class FactionGameApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_faction = None
        self.video_player = None
        
        # 阵营历史记录（最多保留100次）
        self.faction_history = []
        self.max_history = 100
        
    def get_balanced_faction(self):
        """智能选择阵营，保持5:5平衡，最多不超过4:6"""
        # 如果历史记录少于2次，随机选择
        if len(self.faction_history) < 2:
            faction = random.choice(['rusher', 'defender'])
            self.faction_history.append(faction)
            if len(self.faction_history) > self.max_history:
                self.faction_history.pop(0)
            return faction
        
        # 统计当前100次内的分布
        recent_history = self.faction_history[-self.max_history:]
        rusher_count = recent_history.count('rusher')
        defender_count = recent_history.count('defender')
        total_count = len(recent_history)
        
        rusher_ratio = rusher_count / total_count if total_count > 0 else 0.5
        defender_ratio = defender_count / total_count if total_count > 0 else 0.5
        
        print(f"📊 阵营统计（最近{total_count}次）: Rusher={rusher_count} ({rusher_ratio*100:.1f}%), Defender={defender_count} ({defender_ratio*100:.1f}%)")
        
        # 动态调整概率
        # 如果某方超过60%，强制选择另一方
        if rusher_ratio > 0.6:
            faction = 'defender'
            print("⚖️ Rusher过多，强制选择Defender")
        elif defender_ratio > 0.6:
            faction = 'rusher'
            print("⚖️ Defender过多，强制选择Rusher")
        # 如果某方超过55%，大幅提高另一方概率（80%）
        elif rusher_ratio > 0.55:
            faction = 'defender' if random.random() < 0.8 else 'rusher'
            print("⚖️ Rusher偏多，80%概率选择Defender")
        elif defender_ratio > 0.55:
            faction = 'rusher' if random.random() < 0.8 else 'defender'
            print("⚖️ Defender偏多，80%概率选择Rusher")
        # 如果在45%-55%之间，正常随机
        else:
            faction = random.choice(['rusher', 'defender'])
            print("✅ 平衡良好，随机选择")
        
        # 记录到历史
        self.faction_history.append(faction)
        if len(self.faction_history) > self.max_history:
            self.faction_history.pop(0)
        
        return faction
        
    def build(self):
        # 设置窗口背景色为黑色
        Window.clearcolor = (0, 0, 0, 1)
        
        # 主布局
        self.main_layout = FloatLayout()
        
        # 创建开始界面
        self.create_start_screen()
        
        return self.main_layout
    
    def create_start_screen(self):
        """创建开始界面"""
        # 清空布局
        self.main_layout.clear_widgets()
        
        # 添加背景图片
        bg_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bg.png')
        if os.path.exists(bg_path):
            bg_image = Image(
                source=bg_path,
                size_hint=(1, 1),
                pos_hint={'center_x': 0.5, 'center_y': 0.5},
                fit_mode='fill'  # 拉伸填充整个区域
            )
            self.main_layout.add_widget(bg_image)
        
        # 手掌图片（全屏显示，放大6倍，带透明通道和流光效果）
        hand_image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hand.png')
        if os.path.exists(hand_image_path):
            # 使用带流光效果的手型组件
            glowing_hand = GlowingHandWidget(
                hand_image_path=hand_image_path,
                size_hint=(1, 1)
            )
            self.main_layout.add_widget(glowing_hand)
        else:
            # 如果图片不存在，使用原来的手掌图形（也放大6倍）
            hand_button = HandButton(
                size_hint=(None, None),
                size=(3000, 3000),  # 放大6倍
                pos_hint={'center_x': 0.5, 'center_y': 0.5}
            )
            self.main_layout.add_widget(hand_button)
        
        # 透明的全屏点击区域
        click_area = Button(
            text='',
            background_color=(0, 0, 0, 0),  # 完全透明
            size_hint=(1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            border=(0, 0, 0, 0)
        )
        click_area.bind(on_press=self.start_game)
        self.main_layout.add_widget(click_area)
    
    def start_game(self, instance):
        """开始游戏 - 智能平衡选择阵营"""
        # 使用智能平衡算法选择阵营
        self.current_faction = self.get_balanced_faction()
        
        # 立刻显示阵营动画
        self.show_result()
    
    def show_result(self):
        """显示抽取结果"""
        # 清空布局
        self.main_layout.clear_widgets()
        
        # 根据阵营设置颜色和文本
        if self.current_faction == 'rusher':
            faction_text = '潜入者 (Rusher)'
            faction_color = (1, 0.2, 0.2, 1)  # 红色
            video_file = 'rusher.mp4'
        else:
            faction_text = '保卫者 (Defender)'
            faction_color = (0.2, 0.6, 1, 1)  # 蓝色
            video_file = 'defender.mp4'
        
        # 尝试播放视频（全屏）
        video_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), video_file)
        print(f"\n尝试加载视频: {video_path}")
        print(f"文件是否存在: {os.path.exists(video_path)}")
        
        if os.path.exists(video_path):
            try:
                # 创建全屏视频播放器（强制拉伸填充）
                self.video_player = Video(
                    source=video_path,
                    state='play',
                    options={'eos': 'pause'},  # 播放一次后暂停
                    size_hint=(1, 1),  # 全屏大小
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                    fit_mode='fill'  # 拉伸填充整个区域
                )
                
                # 绑定加载事件
                def on_load(instance):
                    print(f"✓ 视频加载成功: {video_file}")
                    instance.state = 'play'
                
                self.video_player.bind(on_load=on_load)
                
                # 直接添加到主布局（全屏显示）
                self.main_layout.add_widget(self.video_player)
                print(f"✓ 视频全屏显示")
                
            except Exception as e:
                print(f"✗ 视频加载失败: {e}")
                # 如果失败，显示错误信息
                self.show_result_with_text(faction_text, faction_color, f'视频加载失败\n{str(e)}')
        else:
            # 如果视频不存在，显示文字结果
            self.show_result_with_text(faction_text, faction_color, f'视频文件未找到')
        
        # 添加透明的全屏点击区域（返回首页）
        click_area = Button(
            text='',
            background_color=(0, 0, 0, 0),  # 完全透明
            size_hint=(1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            border=(0, 0, 0, 0)
        )
        click_area.bind(on_press=self.back_to_menu)
        self.main_layout.add_widget(click_area)
    
    def show_result_with_text(self, faction_text, faction_color, error_msg):
        """显示文字结果（当视频不可用时）"""
        result_layout = BoxLayout(
            orientation='vertical',
            spacing=20,
            padding=20
        )
        
        result_label = Label(
            text=f'你的阵营是:\n{faction_text}',
            font_name='CustomFontBold',
            font_size='32sp',
            color=faction_color
        )
        
        error_label = Label(
            text=error_msg,
            font_name='CustomFont',
            font_size='18sp',
            color=(0.8, 0.8, 0.8, 1)
        )
        
        result_layout.add_widget(result_label)
        result_layout.add_widget(error_label)
        self.main_layout.add_widget(result_layout)
        
        # 添加透明的全屏点击区域（返回首页）
        click_area = Button(
            text='',
            background_color=(0, 0, 0, 0),  # 完全透明
            size_hint=(1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            border=(0, 0, 0, 0)
        )
        click_area.bind(on_press=self.back_to_menu)
        self.main_layout.add_widget(click_area)
    
    def show_white_transition(self):
        """显示白场过渡动画（0.6秒）"""
        from kivy.animation import Animation
        from kivy.graphics import Color, Rectangle
        
        # 清空布局
        self.main_layout.clear_widgets()
        
        # 创建白色背景 Widget
        white_bg = Widget()
        with white_bg.canvas:
            Color(1, 1, 1, 1)  # 白色
            Rectangle(pos=(0, 0), size=(10000, 10000))  # 超大尺寸确保全屏
        
        self.main_layout.add_widget(white_bg)
        
        # 0.6秒后显示阵营图片
        Clock.schedule_once(lambda dt: self.show_faction_image(), 0.6)
        print(f"✓ 白场过渡开始（0.6秒）")
    
    def show_faction_image(self):
        """显示阵营图片"""
        # 清空布局
        self.main_layout.clear_widgets()
        
        # 根据阵营选择对应的图片
        if self.current_faction == 'rusher':
            image_file = 'rusher.png'
        else:
            image_file = 'defender.png'
        
        image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), image_file)
        
        if os.path.exists(image_path):
            # 显示阵营图片（全屏）
            faction_image = Image(
                source=image_path,
                size_hint=(1, 1),
                pos_hint={'center_x': 0.5, 'center_y': 0.5},
                fit_mode='fill'
            )
            self.main_layout.add_widget(faction_image)
            print(f"✓ 显示阵营图片: {image_file}")
        else:
            print(f"✗ 阵营图片未找到: {image_path}")
        
        # 添加透明的全屏点击区域（返回首页）
        click_area = Button(
            text='',
            background_color=(0, 0, 0, 0),  # 完全透明
            size_hint=(1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            border=(0, 0, 0, 0)
        )
        click_area.bind(on_press=self.back_to_menu)
        self.main_layout.add_widget(click_area)
    
    def back_to_menu(self, instance):
        """返回主菜单"""
        if self.video_player:
            self.video_player.state = 'stop'
            self.video_player = None
        self.create_start_screen()
    
    def exit_game(self, instance):
        """退出游戏"""
        App.get_running_app().stop()


if __name__ == '__main__':
    FactionGameApp().run()
