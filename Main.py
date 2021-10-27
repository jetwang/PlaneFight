import time

import pygame

from src.ObjectContext import ObjectContext
from src.EventCapture import *

# 全局变量
# 窗口
window_screen = None
window_height = 852
object_context = None

pygame.init()


def main():
    global window_screen
    global object_context
    # 背景色
    bg_color = (205, 205, 205)
    # 1. 创建窗口
    window_screen = pygame.display.set_mode((695, window_height), 0, 32)
    object_context = ObjectContext(window_screen)
    hero_plane = object_context.create_hero_plane(100, 300, ["hero1.png"], 1)
    enemy_plane = object_context.create_hero_plane(200, 500, ["hero1.png"], 1)
    pygame.display.set_caption('飞机大战')
    pygame.key.set_repeat(200,200)
    while True:
        window_screen.fill(bg_color)
        object_context.render_objects()
        # 更新图片
        capture_events(hero_plane)
        object_context.fire_hit_events()
        pygame.display.update()
        # 系统睡眠时间(电脑配置不同，影响游戏流畅运行度)
        time.sleep(0.04)


if __name__ == "__main__":
    main()
