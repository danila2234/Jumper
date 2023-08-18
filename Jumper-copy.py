import pygame
from screeninfo import get_monitors
import math

# Подстраивание экрана игры под монитор игрока

for m in get_monitors():
    monitor_w = m.width
    monitor_h = m.height

size = 30

width_butt_levels = 392
width_butt_quit = 280
width_butt_start = 340
height_butt = 120
x_butt = 85
y_butt_start = 365
y_butt_levels = 527
y_butt_quit = 689
num = 0

print(monitor_w, monitor_h)
MOVE_SPEED = 7
JUMP_POWER = 10

for i in range(30):
    result_w = size * 34
    result_h = size * 30
    Reduction_Formula_w = float(result_w) / x_butt

    if (result_w <= monitor_w) and (result_h <= monitor_h):
        print("Успех наконец успех")
        print(result_w, result_h)
        print(size)
        break

    y_butt_start -= 12.1666666667
    y_butt_levels -= 17.5666666667
    y_butt_quit -= 22.9666666667
    x_butt -= 2.5
    size -= 1
    height_butt -= 4
    width_butt_start -= 11
    width_butt_levels -= Reduction_Formula_w
    width_butt_quit -= Reduction_Formula_w
    MOVE_SPEED -= 0.23333333333
    JUMP_POWER -= 0.33333333333

print(result_w, result_h)

# FPS и Ширина, Высота экрана:

pygame.init()
FPS = 70
WIDTH = result_w
HEIGHT = result_h

#Цвета

WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
GREEN = (0, 255, 0)
GREY = (194, 194, 194)
DARK_GREY = (34, 32, 52)
BLACK = (0, 0, 0)

# Инициализация pygame:

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Шрифт:

font = pygame.font.Font('ka1.ttf', 36)

# Создание уровня:

level = [
' bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb ',
'r                                l',
'r                                l',
'r             |        ||       Dl',
'r             -        --      --l',
'r                                l',
'r        --       --       --    l',
'r                                l',
'r          ||||||||||||||||||||||l',
'r      --------------------------l',
'r                                l',
'r|                               l',
'r--                             <l',
'r      |  |                     <l',
'r     <---->                    <l',
'r                               <l',
'r                |  |           <l',
'r               <---->          <l',
'r                               <l',
'r                               <l',
'r                          <-->  l',
'r                                l',
'r                                l',
'r                  <-->          l',
'r                                l',
'r--                              l',
'r          <-->                  l',
'r                                l',
'r P   --|||||||||||||||||||||||||l',
' tttttttttttttttttttttttttttttttt '
]
level_2 = [
' bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb ',
'r                                l',
'r                                l',
'r               |              PLl',
'r    ----------------------------l',
'r               -                l',
'r              <->               l',
'r                                l',
'r                                l',
'r                                l',
'r              <->               l',
'r    *    E    *-*    E    *     l',
'r----------------------------    l',
'r      -       v       -         l',
'r      v               v         l',
'r                                l',
'r                                l',
'r              -                 l',
'r      |   -   |   -   |         l',
'r      -*  E  *-*  E  *-         l',
'r    ----------------------------l',
'r     -vvv-vvv-vvv-vvv-          l',
'r     v   v   v   v   v          l',
'r                                l',
'r                                l',
'r                                l',
'r             -                  l',
'r     |   -   |   -   |          l',
'r     -*  E  *-*  E  *-      D   l',
' tttttttttttttttttttttttttttttttt '
]
level_3 = [
' bbbbbbbb4bbb4bbb4bbb4bbb4bbbbbbb ',
'r                                l',
'r                                l',
'r                                l',
'r                                l',
'r                                l',
'r                             D  l',
'r    ---------------------------4l',
'r                                l',
'r                                l',
'r                                l',
'r  --                            l',
'r                -               l',
'2           |3|* E *|3|          l',
'r--------------4------------     l',
'r                                l',
'r                                l',
'r                                l',
'r                                l',
'r                             <--l',
'r             <->                l',
'r          -|||-|||-||*   E   *||l',
'r   <----------------------------l',
'r             ---     ---        l',
'r             vvv     vvv        l',
'r                                l',
'r                                l',
'r  -                             l',
'2             |||     |||   -PL  l',
' tttttttttttttttttttttttttttttttt '

]

level_4 = [
' bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb ',
'r                                l',
'r                                l',
'r                                l',
'r                                l',
'r                                l',
'r                                l',
'r                                l',
'r                                l',
'r                                l',
'r                                l',
'r                                l',
'r                                l',
'r                                l',
'r                                l',
'r                                l',
'r                                l',
'r                                l',
'r                                l',
'r                                l',
'r                                l',
'r                                l',
'r                                l',
'r                                l',
'r                                l',
'r                                l',
'r                                l',
'r                                l',
'r                                l',
' tttttttttttttttttttttttttttttttt '

]

sprite_level1 = pygame.image.load('Sprite-button_Level1.png')
animation_button_level_1 = ['Sprite-button_Level1.png', 'Sprite-button_Level1_anim.png']
sprite_level2 = pygame.image.load('Sprite-button_Level2.png')
animation_button_level_2 = ['Sprite-button_Level2.png', 'Sprite-button_Level2_anim.png']
sprite_level3 = pygame.image.load('Sprite-button_Level3.png')
animation_button_level_3 = ['Sprite-button_Level3.png', 'Sprite-button_Level3_anim.png']
sprite_back = pygame.image.load('Sprite-Button_back.png')
animation_button_back = ['Sprite-Button_back.png', 'Sprite-Button_back_anim.png']
size_level1 = sprite_level1.get_size()
size_level2 = sprite_level2.get_size()
size_level3 = sprite_level3.get_size()
size_back = sprite_back.get_size()
levels = [level, level_2, level_3, level_4]
WhatLevel = True
x_p = 0
y_p = 0
Number = 1
level1_f = font.render('Level 1', True, BLACK)
level2_f = font.render('Level 2', True, BLACK)
level3_f = font.render('Level 3', True, BLACK)
level4_f = font.render('To be continued', True, BLACK)
WhatRestart = 0

# Создание турели:

Tutle = pygame.Rect(x_p, y_p, size, size)
Shot = pygame.Rect(x_p, y_p, size, size)
Tutles = []
sprite_tutle_d = pygame.image.load('Sprite-Turret_installation_down.png')
sprite_tutle_u = pygame.image.load('Sprite-Turret_installation_up.png')
sprite_tutle_l = pygame.image.load('Sprite-Turret_installation_left.png')
sprite_tutle_r = pygame.image.load('Sprite-Turret_installation_right.png')
sprite_shot = pygame.image.load('Sprite-Shot.png')
size_shot = sprite_shot.get_size()

# Создание бьющего врага:

Enemy = pygame.Rect(x_p, y_p, size, size)
enemyes = []
enemye_stop = pygame.Rect(x_p, y_p, size, size)
enemyes_stop = []
x_vel_e = 5
Right_e = True
Left_e = False
sprite_enemy_hit_r_anim = ['Sprite-Enemy_hit.png', 'Sprite-Enemy_hit_sit.png']
sprite_enemy_hit_l_anim = ['Sprite-Enemy_hit_left.png', 'Sprite-Enemy_hit_sit_left.png']
left_ground_e = pygame.Rect(Enemy.left, Enemy.top, x_vel_e, size)
right_ground_e = pygame.Rect(Enemy.right, Enemy.top, x_vel_e, size)

# Создание шипов:

spick_sprite = pygame.image.load('Sprite-Spike.png')
spick_sprite_l = pygame.image.load('Sprite-Spike_l.png')
spick_sprite_r = pygame.image.load('Sprite-Spike_r.png')
spick_sprite_b = pygame.image.load('Sprite-Spike_b.png')
Spikes = []

# Создание двери:

Door = pygame.Rect(x_p, y_p, size, size)
Doors = []
door_sprite = pygame.image.load('Sprite-door.png')
sprite_arrow = pygame.image.load('Sprite-Arrow.png')
locked_door_sprite = pygame.image.load('Sprite-locked_door.png')
level_point = 0
Enter = False

# Создание блоков:

platform = pygame.Rect(x_p, y_p, size, size)
platforms = []
block_sprite_r = pygame.image.load('Sprite-Block_r.png')
block_sprite_l = pygame.image.load('Sprite-Block_l.png')
block_sprite_t = pygame.image.load('Sprite-Block_t.png')
block_sprite_d = pygame.image.load('Sprite-Block_d.png')
block_sprite = pygame.image.load('Sprite-Block.png')

# Создание меню:

gamemode = 1
button_Start = pygame.image.load('Sprite-Button_Play.png')
button_Start_anim = ['Sprite-Button_Play.png', 'Sprite-Button_Play_anim.png']
button_Levels = pygame.image.load('Sprite-Button_Levels.png')
button_Levels_anim = ['Sprite-Button_Levels.png', 'Sprite-Button_Levels_anim.png']
button_Quit = pygame.image.load('Sprite-Button_Quit.png')
button_Quit_anim = ['Sprite-Button_Quit.png', 'Sprite-Button_Quit_anim.png']

# Создание главного героя:

y = result_h - 50
x = WIDTH / 2 - 300
Wigth = size
Height = size
Player = pygame.Rect(x, y, Wigth, Height)
left_ground = pygame.Rect(Player.left, Player.top, 1.1, Height)
right_ground = pygame.Rect(Player.right, Player.top, 1, Height)
bottom_ground = pygame.Rect(Player.left, Player.bottom, Wigth, 1)
top_ground = pygame.Rect(Player.left, Player.top, Wigth, 1)
player_anim_right = ['Sprite-Player.png', 'Sprite-Player_b.png']
player_anim_left = ['Sprite-Player_left.png', 'Sprite-Player_left_b.png']
player_anim_sleep = ['Sprite-Player_sleep.png', 'Sprite-Player_sleep_1.png']
player_anim_wake_up = ['Sprite-Player_wake_up1.png', 'Sprite-Player_wake_up2.png', 'Sprite-Player_wake_up3.png']
player_anim_right_run = ['Sprite-Player_right_run.png', 'Sprite-Player_right_b_run.png']
player_anim_left_run = ['Sprite-Player_left_run.png', 'Sprite-Player_left_b_run.png']
right_or_left = 2
index = 0
speed_index = 0
count = 30
count_speed = 15
Game_Over = font.render('r - restart', True, BLACK)
Cut_Scene = True
Scene1 = True
Dead = False
position = 1
Restart = False
restert_time = 2

# Добавление музыки в игру:

pygame.mixer.music.load("DendyContra.mp3")
start_music = 1

# Переменные для перемещения игрока:

x_vel = 0
Left = False
Right = False

# Падение и прыжок игрока:
Gravity = 0.35
y_vel = 0
onGround = False
Jump = False

# Добавление звуков:



running = True
while running:

    if gamemode == 1:

        events = pygame.event.get()

        comp_button_Start = pygame.transform.scale(button_Start, (int(width_butt_start), int(height_butt)))
        comp_button_Levels = pygame.transform.scale(button_Levels, (int(width_butt_levels), int(height_butt)))
        comp_button_Quit = pygame.transform.scale(button_Quit, (int(width_butt_quit), int(height_butt)))


        screen.fill(GREY)
        screen.blit(comp_button_Start, (x_butt, y_butt_start))
        screen.blit(comp_button_Levels, (x_butt, y_butt_levels))
        screen.blit(comp_button_Quit, (x_butt, y_butt_quit))

        for i in events:

            # Упровение дисплеем

            if i.type == pygame.QUIT:
                running = False

            if i.type == pygame.MOUSEBUTTONDOWN:
                if (x_butt <= i.pos[0] <= (x_butt + width_butt_start)) and (y_butt_start <= i.pos[1] <= (y_butt_start + height_butt)):
                    if i.button == 1:

                        button_Start = pygame.image.load(button_Start_anim[1])
                        screen.blit(comp_button_Start, (x_butt, y_butt_start))

                if (x_butt <= i.pos[0] <= (x_butt + width_butt_levels)) and (y_butt_levels <= i.pos[1] <= (y_butt_levels + height_butt)):
                    if i.button == 1:

                        button_Levels = pygame.image.load(button_Levels_anim[1])
                        screen.blit(comp_button_Levels, (x_butt, y_butt_levels))

                if (x_butt <= i.pos[0] <= (x_butt + width_butt_quit)) and (y_butt_quit <= i.pos[1] <= (y_butt_quit + height_butt)):
                    if i.button == 1:

                        button_Quit = pygame.image.load(button_Quit_anim[1])
                        screen.blit(comp_button_Quit, (x_butt, y_butt_quit))

            if i.type == pygame.MOUSEBUTTONUP:

                button_Start = pygame.image.load(button_Start_anim[0])
                screen.blit(comp_button_Start, (x_butt, y_butt_start))
                button_Levels = pygame.image.load(button_Levels_anim[0])
                screen.blit(comp_button_Levels, (x_butt, y_butt_levels))
                button_Quit = pygame.image.load(button_Quit_anim[0])
                screen.blit(comp_button_Quit, (x_butt, y_butt_quit))

                if (x_butt <= i.pos[0] <= (x_butt + width_butt_start)) and (y_butt_start <= i.pos[1] <= (y_butt_start + height_butt)):
                    if i.button == 1:

                        level_point = 0

                        gamemode = 2

                if (x_butt <= i.pos[0] <= (x_butt + width_butt_levels)) and (y_butt_levels <= i.pos[1] <= (y_butt_levels + height_butt)):
                    if i.button == 1:

                        gamemode = 3

                if (x_butt <= i.pos[0] <= (x_butt + width_butt_quit)) and (y_butt_quit <= i.pos[1] <= (y_butt_quit + height_butt)):
                    if i.button == 1:
                        running = False

    if gamemode == 3:

        screen.fill(GREY)

        pygame.draw.polygon(screen, WHITE, [(0, 0), (WIDTH - 1, 0), (WIDTH - 1, HEIGHT - 1), (0, HEIGHT - 1), (0, 0)], 70)
        pygame.draw.polygon(screen, DARK_GREY, [(0, 0), (WIDTH - 2, 0), (WIDTH - 2, HEIGHT - 2), (0, HEIGHT - 2), (0, 0)], 2)
        pygame.draw.polygon(screen, DARK_GREY, [(35, 35), (WIDTH - 35, 35), (WIDTH - 35, HEIGHT - 35), (35, HEIGHT - 35), (35, 35)], 2)

        screen.blit(sprite_level1, (45, 45))
        screen.blit(sprite_level2, (85, 45))
        screen.blit(sprite_level3, (125, 45))
        screen.blit(sprite_back, (5, 5))

        events = pygame.event.get()

        for i in events:

            # Упровение дисплеем

            if i.type == pygame.QUIT:
                running = False

            if i.type == pygame.MOUSEBUTTONDOWN:
                if (45 <= i.pos[0] <= (45 + size_level1[0])) and (45 <= i.pos[1] <= (45 + size_level1[1])):

                    if i.button == 1:

                        sprite_level1 = pygame.image.load(animation_button_level_1[1])
                        screen.blit(sprite_level1, (45, 45))

                if (85 <= i.pos[0] <= (85 + size_level2[0])) and (45 <= i.pos[1] <= (45 + size_level2[1])):

                    if i.button == 1:

                        sprite_level2 = pygame.image.load(animation_button_level_2[1])
                        screen.blit(sprite_level2, (85, 45))

                if (125 <= i.pos[0] <= (125 + size_level3[0])) and (45 <= i.pos[1] <= (45 + size_level1[1])):

                    if i.button == 1:

                        sprite_level3 = pygame.image.load(animation_button_level_3[1])
                        screen.blit(sprite_level3, (125, 45))

                if (5 <= i.pos[0] <= (5 + size_back[0])) and (5 <= i.pos[1] <= (5 + size_back[1])):

                    if i.button == 1:

                        sprite_back = pygame.image.load(animation_button_back[1])
                        screen.blit(sprite_back, (5, 5))

            if i.type == pygame.MOUSEBUTTONUP:

                sprite_level1 = pygame.image.load(animation_button_level_1[0])
                screen.blit(sprite_level1, (45, 45))
                sprite_level2 = pygame.image.load(animation_button_level_2[0])
                screen.blit(sprite_level2, (85, 45))
                sprite_level3 = pygame.image.load(animation_button_level_3[0])
                screen.blit(sprite_level3, (125, 45))
                sprite_back = pygame.image.load(animation_button_back[0])
                screen.blit(sprite_back, (5, 5))

                if (45 <= i.pos[0] <= (45 + size_level1[0])) and (45 <= i.pos[1] <= (45 + size_level1[1])):

                    if i.button == 1:
                        gamemode = 2
                        level_point = 0
                        x_vel = 0
                        y_vel = 0
                        Player.left = x
                        Player.top = y
                        Restart = True
                        Number = 1

                if (85 <= i.pos[0] <= (85 + size_level2[0])) and (45 <= i.pos[1] <= (45 + size_level2[1])):

                    if i.button == 1:
                        gamemode = 2
                        level_point = 1

                        x_vel = 0
                        y_vel = 0
                        Player.left = x
                        Player.top = y
                        Restart = True
                        Number = 1

                if (125 <= i.pos[0] <= (125 + size_level3[0])) and (45 <= i.pos[1] <= (45 + size_level1[1])):

                    if i.button == 1:
                        gamemode = 2
                        level_point = 2

                        x_vel = 0
                        y_vel = 0
                        Player.left = x
                        Player.top = y
                        Restart = True
                        Number = 1

                if (5 <= i.pos[0] <= (5 + size_back[0])) and (5 <= i.pos[1] <= (5 + size_back[1])):
                    
                    if i.button == 1:
                        gamemode = 1

            


    if gamemode == 2:

        if start_music == 1:
            pygame.mixer.music.play(-1)
            start_music += 1

        if Restart:
            restert_time -= 1
            if restert_time == 0:
                Restart = False
                restert_time = 2

        # Анимация игрока:

        sprite_player_right = pygame.image.load(player_anim_right[index])
        sprite_player_left = pygame.image.load(player_anim_left[index])
        sprite_player_right_run = pygame.image.load(player_anim_right_run[speed_index])
        sprite_player_left_run = pygame.image.load(player_anim_left_run[speed_index])

        # Редактирование размера спрайта враг:

        sprite_enemy_hit_run_r = pygame.image.load(sprite_enemy_hit_r_anim[speed_index])
        comp_sprite_enemy_hit_run_r = pygame.transform.scale(sprite_enemy_hit_run_r, (int(size), int(size)))
        sprite_enemy_hit_run_l = pygame.image.load(sprite_enemy_hit_l_anim[speed_index])
        comp_sprite_enemy_hit_run_l = pygame.transform.scale(sprite_enemy_hit_run_l, (int(size), int(size)))

        # Редактирование размера спрайта турели:

        comp_tutle_r = pygame.transform.scale(sprite_tutle_r, (int(size), int(size)))
        comp_tutle_l = pygame.transform.scale(sprite_tutle_l, (int(size), int(size)))
        comp_tutle_u = pygame.transform.scale(sprite_tutle_u, (int(size), int(size)))
        comp_tutle_d = pygame.transform.scale(sprite_tutle_d, (int(size), int(size)))
        comp_shot = pygame.transform.scale(sprite_shot, (int(size), int(size)))

        # Редактирование размера спрайта блока:

        comp_block_r = pygame.transform.scale(block_sprite_r, (int(size), int(size)))
        comp_block_l = pygame.transform.scale(block_sprite_l, (int(size), int(size)))
        comp_block_t = pygame.transform.scale(block_sprite_t, (int(size), int(size)))
        comp_block_d = pygame.transform.scale(block_sprite_d, (int(size), int(size)))
        comp_block = pygame.transform.scale(block_sprite, (int(size), int(size)))

        # Редактирование размера спрайта игрока:

        comp_player_r = pygame.transform.scale(sprite_player_right, (int(Wigth), int(Height)))
        comp_player_l = pygame.transform.scale(sprite_player_left, (int(Wigth), int(Height)))
        comp_player_r_run = pygame.transform.scale(sprite_player_right_run, (int(Wigth), int(Height)))
        comp_player_l_run = pygame.transform.scale(sprite_player_left_run, (int(Wigth), int(Height)))

        # Редактирование размера спрайта шипа:

        comp_spikes = pygame.transform.scale(spick_sprite, (int(size), int(size)))
        comp_spikes_l = pygame.transform.scale(spick_sprite_l, (int(size), int(size)))
        comp_spikes_r = pygame.transform.scale(spick_sprite_r, (int(size), int(size)))
        comp_spikes_b = pygame.transform.scale(spick_sprite_b, (int(size), int(size)))

        # Редактирование размера спрайта двери:

        comp_door = pygame.transform.scale(door_sprite, (int(size), int(size)))
        comp_locked_door = pygame.transform.scale(locked_door_sprite, (int(size), int(size)))
        comp_arrow = pygame.transform.scale(sprite_arrow, (int(size), int(size)))

        # Обьекты которые отвечают за проверку сталкновения:

        left_ground = pygame.Rect(Player.left - 1, Player.top, MOVE_SPEED, Height)
        right_ground = pygame.Rect(Player.right, Player.top, MOVE_SPEED, Height)
        bottom_ground = pygame.Rect(Player.left, Player.bottom, Wigth, 1)
        top_ground = pygame.Rect(Player.left, Player.top, Wigth, 1)
        screen.fill(WHITE)

        # Цикл событий:

        events = pygame.event.get()


        for i in events:

            # Упровение дисплеем

            if i.type == pygame.QUIT:
                running = False

            # Упровление главного героя

            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_d:
                    Right = True

                if i.key == pygame.K_a:
                    Left = True

                if i.key == pygame.K_SPACE:
                    Jump = True

                if i.key == pygame.K_r:
                    if Dead == True:
                        if level_point <= 3:
                            while len(platforms) > 0:
                                for p in platforms:
                                    platforms.remove(p)

                            while len(Spikes) > 0:
                                for s in Spikes:
                                    Spikes.remove(s)

                            while len(enemyes) > 0:
                                for e in enemyes:
                                    enemyes.remove(e)

                            while len(enemyes_stop) > 0:
                                for s in enemyes_stop:
                                    enemyes_stop.remove(s)

                            for d in Doors:
                                Doors.remove(d)

                            screen.fill(WHITE)
                            x_p = 0
                            y_p = 0


                        x_vel = 0
                        y_vel = 0
                        Player.left = x
                        Player.top = y
                        Dead = False
                        Restart = True
                        Number = 1

                        if level_point == 2:
                            for t in Tutles:
                                t[2].left = t[0].left
                                t[2].top = t[0].top


                if i.key == pygame.K_w:
                    if Enter == True:
                        level_point += 1

                        if level_point <= 3:
                            while len(platforms) > 0:
                                for p in platforms:
                                    platforms.remove(p)

                            while len(Spikes) > 0:
                                for s in Spikes:
                                    Spikes.remove(s)

                            while len(enemyes) > 0:
                                for e in enemyes:
                                    enemyes.remove(e)

                            while len(enemyes_stop) > 0:
                                for s in enemyes_stop:
                                    enemyes_stop.remove(s)

                            for d in Doors:
                                Doors.remove(d)

                            screen.fill(DARK_GREY)
                            x_p = 0
                            y_p = 0
                            Number = 1
                            WhatLevel = True

                if i.key == pygame.K_RETURN:
                    if WhatLevel == True:
                        WhatLevel = False
                        if level_point == 3:
                            running = False

            if i.type == pygame.KEYUP:
                if i.key == pygame.K_d:
                    Right = False
                    x_vel = 0

                if i.key == pygame.K_a:
                    Left = False
                    x_vel = 0

                if i.key == pygame.K_SPACE:
                    Jump = False
                    y_vel = 0
                    onGround = False

        # Передвижение и прыжок главного героя:
        if Left:
            x_vel = -MOVE_SPEED
            right_or_left = 1

        if Right:
            x_vel = MOVE_SPEED
            right_or_left = 2

        if Jump:
            if onGround:
                y_vel = -JUMP_POWER

        if not onGround:
            y_vel += Gravity

        onGround = False
        Player.bottom += y_vel
        top_ground.bottom += y_vel
        bottom_ground.bottom += y_vel
        left_ground.bottom += y_vel
        right_ground.bottom += y_vel

        Player.right += x_vel
        left_ground.right += x_vel
        right_ground.right += x_vel
        top_ground.right += x_vel
        bottom_ground.right += x_vel

        # Создание обьектов:

        platform = pygame.Rect(x_p, y_p, size, size)

        count -= 1
        count_speed -= 1

        if count == 0:
            count = 30
            index += 1
            if index > 1:
                index = 0

        if count_speed == 0:
            count_speed = 15
            speed_index += 1
            if speed_index > 1:
                speed_index = 0

        # Создание блоков по списку level и добавление их в список:

        if Number == 1:
            for i in range(30):
                if i >= 1:
                    y_p += size
                x_p = 0
                Number += 1
                for j in range(34):
                    if j >= 1:
                        x_p += size
                    if levels[level_point][i][j] == '-':
                        platform = pygame.Rect(x_p, y_p, size, size)
                        platforms.append(platform)
                    if levels[level_point][i][j] == 't':
                        platform = pygame.Rect(x_p, y_p, size, size)
                        platforms.append(platform)
                    if levels[level_point][i][j] == 'r':
                        platform = pygame.Rect(x_p, y_p, size, size)
                        platforms.append(platform)
                    if levels[level_point][i][j] == 'b':
                        platform = pygame.Rect(x_p, y_p, size, size)
                        platforms.append(platform)
                    if levels[level_point][i][j] == 'l':
                        platform = pygame.Rect(x_p, y_p, size, size)
                        platforms.append(platform)
                    if levels[level_point][i][j] == '|':
                        Spike = pygame.Rect(x_p, y_p, size - 10, size - 10)
                        Spikes.append(Spike)
                    if levels[level_point][i][j] == 'v':
                        Spike = pygame.Rect(x_p, y_p, size - 10, size - 10)
                        Spikes.append(Spike)
                    if levels[level_point][i][j] == '>':
                        Spike = pygame.Rect(x_p, y_p, size - 10, size - 10)
                        Spikes.append(Spike)
                    if levels[level_point][i][j] == '<':
                        Spike = pygame.Rect(x_p, y_p, size - 10, size - 10)
                        Spikes.append(Spike)
                    if levels[level_point][i][j] == 'P':
                        x = x_p
                        y = y_p
                        Player = pygame.Rect(x, y, Wigth, Height)
                    if levels[level_point][i][j] == 'D':
                        Door = pygame.Rect(x_p, y_p, size, size)
                        Doors.append(Door)
                    if levels[level_point][i][j] == 'E':
                        Enemy = pygame.Rect(x_p, y_p, Wigth, Height)
                        left_ground_e = pygame.Rect(Enemy.left, Enemy.top, x_vel_e, size)
                        right_ground_e = pygame.Rect(Enemy.right, Enemy.top, x_vel_e, size)
                        Right_e = True
                        Left_e = False
                        enemyes.append([Enemy, left_ground_e, right_ground_e, Right_e, Left_e])
                    if levels[level_point][i][j] == '*':
                        enemye_stop = pygame.Rect(x_p, y_p, size, size)
                        enemyes_stop.append(enemye_stop)
                    if levels[level_point][i][j] == '1':
                        Motion = 'Left'
                        x_shot = x_p
                        y_shot = y_p
                        Tutle = pygame.Rect(x_p, y_p, size, size)
                        Shot = pygame.Rect(Tutle.left, Tutle.top, size, size)
                        Tutles.append([Tutle, Motion, Shot])

                    if levels[level_point][i][j] == '2':
                        Motion = 'Right'
                        x_shot = x_p
                        y_shot = y_p
                        Tutle = pygame.Rect(x_p, y_p, size, size)
                        Shot = pygame.Rect(Tutle.left, Tutle.top, size, size)
                        Tutles.append([Tutle, Motion, Shot])

                    if levels[level_point][i][j] == '3':
                        Motion = 'Up'
                        x_shot = x_p
                        y_shot = y_p
                        Tutle = pygame.Rect(x_p, y_p, size, size)
                        Shot = pygame.Rect(Tutle.left, Tutle.top, size, size)
                        Tutles.append([Tutle, Motion, Shot])

                    if levels[level_point][i][j] == '4':
                        Motion = 'Down'
                        x_shot = x_p
                        y_shot = y_p
                        Tutle = pygame.Rect(x_p, y_p, size, size)
                        Shot = pygame.Rect(Tutle.left, Tutle.top, size, size)
                        Tutles.append([Tutle, Motion, Shot])

        # Колайдеры врага:
        for e in enemyes:
            if e[3] == True:
                e[0].right += x_vel_e
                e[1].right += x_vel_e
                e[2].right += x_vel_e

            if e[4] == True:
                e[0].left -= x_vel_e
                e[1].left -= x_vel_e
                e[2].left -= x_vel_e

        # Выстреливание турели:

        for t in Tutles:
            if t[1] == 'Left':
                t[2].left -= x_vel_e

            if t[1] == 'Right':
                t[2].right += x_vel_e

            if t[1] == 'Up':
                t[2].top -= x_vel_e

            if t[1] == 'Down':
                t[2].bottom += x_vel_e


        # Отрисовка обьектов:

        x_p = 0
        y_p = 0

        for i in range(30):
            if i >= 1:
                y_p += size
            x_p = 0
            for j in range(34):
                if j >= 1:
                    x_p += size
                if levels[level_point][i][j] == '-':
                    screen.blit(comp_block, (x_p, y_p))
                if levels[level_point][i][j] == 't':
                    screen.blit(comp_block_t, (x_p, y_p))
                if levels[level_point][i][j] == 'r':
                    screen.blit(comp_block_r, (x_p, y_p))
                if levels[level_point][i][j] == 'b':
                    screen.blit(comp_block_d, (x_p, y_p))
                if levels[level_point][i][j] == 'l':
                    screen.blit(comp_block_l, (x_p, y_p))
                if levels[level_point][i][j] == '|':
                    screen.blit(comp_spikes, (x_p, y_p))
                if levels[level_point][i][j] == 'v':
                    screen.blit(comp_spikes_b, (x_p, y_p))
                if levels[level_point][i][j] == '>':
                    screen.blit(comp_spikes_r, (x_p, y_p))
                if levels[level_point][i][j] == '<':
                    screen.blit(comp_spikes_l, (x_p, y_p))
                if levels[level_point][i][j] == 'D':
                    screen.blit(comp_door, (Door.left, Door.top))
                if levels[level_point][i][j] == 'L':
                    screen.blit(comp_locked_door, (x_p, y_p))
                    x = x_p
                    y = y_p

        for t in Tutles:
            if t[1] == 'Left':
                screen.blit(comp_shot, (t[2].left, t[2].top))
                screen.blit(comp_tutle_l, (t[0].left, t[0].top))
            if t[1] == 'Right':
                screen.blit(comp_shot, (t[2].left, t[2].top))
                screen.blit(comp_tutle_r, (t[0].left, t[0].top))
            if t[1] == 'Up':
                screen.blit(comp_shot, (t[2].left, t[2].top))
                screen.blit(comp_tutle_u, (t[0].left, t[0].top))
            if t[1] == 'Down':
                screen.blit(comp_shot, (t[2].left, t[2].top))
                screen.blit(comp_tutle_d, (t[0].left, t[0].top))



        for e in enemyes:
            if e[3] == True:
                sprite_enemy_hit_run_r = pygame.image.load(sprite_enemy_hit_r_anim[speed_index])
                screen.blit(comp_sprite_enemy_hit_run_r, (e[0].left, e[0].top))

            if e[4] == True:
                sprite_enemy_hit_run_l = pygame.image.load(sprite_enemy_hit_l_anim[speed_index])
                screen.blit(comp_sprite_enemy_hit_run_l, (e[0].left, e[0].top))

        sprite_player_right = pygame.image.load(player_anim_right[index])
        sprite_player_left = pygame.image.load(player_anim_left[index])
        sprite_player_right_run = pygame.image.load(player_anim_right_run[speed_index])
        sprite_player_left_run = pygame.image.load(player_anim_left_run[speed_index])



        if right_or_left == 1:
            if not Left:
                screen.blit(comp_player_l, (Player.left, Player.top))
            if Left:
                screen.blit(comp_player_l_run, (Player.left, Player.top))
        if right_or_left == 2:
            if not Right:
                screen.blit(comp_player_r, (Player.left, Player.top))
            if Right:
                screen.blit(comp_player_r_run, (Player.left, Player.top))

        if Enter == True:
            screen.blit(comp_arrow, (Player.left, Player.top - 30))

        # Столкновение между обьектами:

        for d in Doors:
            if Player.colliderect(d):
                Enter = True

            if not Player.colliderect(d):
                Enter = False

        if not Restart:
            for p in platforms:

                if right_ground.colliderect(p):
                    if x_vel > 0:
                        Player.right = p.left
                        if Right == True:
                            Player.left -= x_vel
                if left_ground.colliderect(p):
                    if x_vel < 0:
                        Player.left = p.right
                        if Left == True:
                            Player.right += x_vel * -1
                if bottom_ground.colliderect(p):
                    if y_vel > 0:
                        Player.bottom = p.top
                        onGround = True
                        y_vel = 0
                if top_ground.colliderect(p):
                    if y_vel < 0:
                        Player.top = p.bottom
                        y_vel = 0

        # Сотолкновение между шипом и игроком:

        for s in Spikes:
            if Player.colliderect(s):
                Dead = True

        if Dead == True:
            screen.fill(WHITE)
            screen.blit(Game_Over, (result_w / 2 - 100, result_h / 2))

        if WhatLevel == True:
            screen.fill(WHITE)
            if level_point == 0:
                screen.blit(level1_f, (result_w / 2 - 100, result_h / 2))
            if level_point == 1:
                screen.blit(level2_f, (result_w / 2 - 100, result_h / 2))
            if level_point == 2:
                screen.blit(level3_f, (result_w / 2 - 100, result_h / 2))
            if level_point == 3:
                screen.blit(level4_f, (result_w / 2 - 150, result_h / 2))

        # Столкновение врага с невидемым пространством:

        for e in enemyes:
            for s in enemyes_stop:
                if e[1].colliderect(s):
                    e[3] = True
                    e[4] = False
                if e[2].colliderect(s):
                    e[3] = False
                    e[4] = True

        # Столкновение врага с игроком:

        for e in enemyes:
            if e[0].colliderect(Player):
                Dead = True

        for t in Tutles:

            if right_ground.colliderect(t[0]):
                if x_vel > 0:
                    Player.right = t[0].left
                    if Right == True:
                        Player.left -= x_vel
            if left_ground.colliderect(t[0]):
                if x_vel < 0:
                    Player.left = t[0].right
                    if Left == True:
                        Player.right += x_vel * -1
            if bottom_ground.colliderect(t[0]):
                if y_vel > 0:
                    Player.bottom = t[0].top
                    onGround = True
                    y_vel = 0
            if top_ground.colliderect(t[0]):
                if y_vel < 0:
                    Player.top = t[0].bottom
                    y_vel = 0

        # Столкновение пули с блоком:

        for p in platforms:
            for t in Tutles:
                if t[2].colliderect(p):
                    t[2].left = t[0].left
                    t[2].top = t[0].top

        # Столкновение игрока пулей:
        for t in Tutles:
            if t[2].colliderect(Player):
                Dead = True

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()