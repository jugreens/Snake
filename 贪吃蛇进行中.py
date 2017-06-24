#coding:utf-8

#载入模块
import os
import pygame
import sys
import random
from pygame.locals import*

#窗口居中
os.environ["SDL_VIDEO_CENTERED"]="1"

#设置常数
CELL_SIZE=20
UP,DOWN,LEFT,RIGHT=(0,-CELL_SIZE),(0,CELL_SIZE),(-CELL_SIZE,0),(CELL_SIZE,0)

#pygame的初始化
pygame.init()
pygame.display.set_caption("贪吃蛇")

#Game
game_clock=pygame.time.Clock()
game_speed=60
game_screen_width,game_screen_height=640,480
game_screen=pygame.display.set_mode((game_screen_width,game_screen_height))
game_field=game_screen.get_rect()
game_background_color=0,0,0
game_linecolor=33,33,33
game_runing=True
game_playing=True

#Snake
snake_color=12,255,60
snake_color2=50,80,150
snake_color3=192,192,33
snake_color4=192,0,0
snake_rect=pygame.Rect(0,0,CELL_SIZE,CELL_SIZE)
snake_direction=RIGHT
snake_turn=RIGHT
snake_speed=5  #每秒走几个格子
snake_delay=1000 / snake_speed   #蛇每次运动的间隔
snake_time2move=pygame.time.get_ticks()+snake_delay
snake_body=[pygame.Rect(0,0,0,0)]*3   #蛇的身体

#Food
food_color=33,50,180
food_color2=192,192,192
food=pygame.Rect(20*random.randint(0,31),20*random.randint(0,23)
                 ,CELL_SIZE,CELL_SIZE)
#主循环
while game_runing:
    #1用户控制
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_runing=False
        elif event.type==pygame.KEYDOWN:
            if snake_direction in [LEFT,RIGHT]:
                if event.key==pygame.K_UP:
                    snake_turn=UP
                elif event.key==pygame.K_DOWN:
                    snake_turn=DOWN
            elif snake_direction in [UP,DOWN]:
                if event.key==pygame.K_LEFT:
                    snake_turn=LEFT
                elif event.key==pygame.K_RIGHT:
                    snake_turn=RIGHT
    #2更新数据
    #2.1 移动蛇
    if pygame.time.get_ticks()>=snake_time2move:
        snake_time2move=pygame.time.get_ticks()+snake_delay
        snake_body=[snake_rect]+snake_body  #增加一节身体
    #2.2判断是否吃到食物
        if snake_rect==food:
            snake_body+=[]
            food=pygame.Rect(20*random.randint(0,31),20*random.randint(0,23)
                             ,CELL_SIZE,CELL_SIZE)
        else:snake_body.pop()  #截去尾部
        snake_direction=snake_turn
        snake_rect=snake_rect.move(snake_direction)
    
    #2.3 判断是否gameover
    if game_playing:
        #撞墙
        if not game_field.contains(snake_rect):
            game_playing=False
        #撞身体
        for cell in snake_body:
            if snake_rect==cell:
                game_playing=False
        if not game_playing:
            print ("GAME OVER")
    
    #3更新画面
    if game_playing:
        
        #3.1 清除屏幕内容
        game_screen.fill(game_background_color)
        #3.2 画格子
        for i in range(CELL_SIZE,game_screen_width,CELL_SIZE):
            pygame.draw.line(game_screen,game_linecolor,(i,0),
                             (i,game_screen_height))
        for i in range(CELL_SIZE,game_screen_height,CELL_SIZE):
            pygame.draw.line(game_screen,game_linecolor,(0,i),
                             (game_screen_width,i))
        #3.3 画蛇
        #画身体
        for cell in snake_body:
            game_screen.fill(snake_color,cell)
            game_screen.fill(snake_color2,cell.inflate(-10,-10))
        #画头
        game_screen.fill(snake_color4,snake_rect)
        game_screen.fill(snake_color3,snake_rect.inflate(-10,-10))

        #画食物
        game_screen.fill(food_color,food)
        game_screen.fill(food_color2,food.inflate(-10,-10))

    #3.4 更新窗口内容
    pygame.display.flip()
    game_clock.tick(game_speed)

#退出pygame
pygame.quit()
sys.exit(0)
