import pygame, sys
from pygame.locals import *
import random
from datetime import timedelta, datetime
import time

#뱀 클래스
class Snake:
    def __init__(self): # 뱀생성
        self.position = [[130,130]]
        self.direction = "under" # 기본 
    
    def automove(self): # 시간의 흐름에 따른 기본적인 움직임과 마우스 클릭에 따른 움직임을 정해주는 함수
        X, Y = self.position[0]
        if self.direction == "right":
            self.position = [[X+10,Y]] + self.position[:-1]
        elif self.direction == "left":
            self.position = [[X-10,Y]] + self.position[:-1]
        elif self.direction == "over":
            self.position = [[X,Y+10]] + self.position[:-1]
        else :
            self.position = [[X,Y-10]] + self.position[:-1]
    
    def grow(self):
        X,Y = self.position[-1]
        self.position.append([X,Y])

    def die(self):
        if self.position[0] in self.position[1:] or (snake.position[0][0] < 100 or snake.position[0][0] > 350 
        or snake.position[0][1] < 100 or snake.position[0][1] > 350):
            textRect = text.get_rect()
            textRect.center = (ScreenSize[0] // 2, ScreenSize[1] // 2)
            return screen.blit(text,textRect)

class Feed:
    def __init__(self):
        self.feed_X = feed_X
        self.feed_Y = feed_Y
        

# 마우스 클릭에 따라 어느 방향으로 얼마만큼 이동할지 판단해주는 함수.
def movement(X,Y,a,b):
    if a >= X and abs(a - X) >= abs(b - Y):
        return "right"
    elif a <= X and abs(a - X) >= abs(b - Y):
        return "left"
    elif b >= Y and  abs(a - X) <= abs(b - Y):
        return "over"
    elif b <= Y and abs(a - X) <= abs(b - Y):
        return "under"



pygame.init()   
ScreenSize = (800,800)
screen = pygame.display.set_mode(ScreenSize) # 화면크기 설정  
pygame.display.set_caption('Snake Game')         # 윈도우 타이틀 설정


black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Game Over', True, green, blue)

snake = Snake()
feed_X = random.randint(100,350)
feed_Y = random.randint(100,350)
cha_direction = "under"

Interval = timedelta(seconds=10)
lasttime = datetime.now()
sec = datetime.now()
sec_interval = timedelta(seconds=1)



while snake.die() == None:  
    Change_Flag = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            a,b = pygame.mouse.get_pos()
            cha_direction = movement(snake.position[0][0],snake.position[0][1],a,b)
            Change_Flag = True
    

    if Interval < datetime.now() - lasttime:
        feed_X = random.randint(100,350)
        feed_Y = random.randint(100,350)
        lasttime = datetime.now()
    if datetime.now() - sec > sec_interval or Change_Flag:
        snake.direction = cha_direction
        snake.automove()
        sec = datetime.now()
        
    if feed_X - 10 <= snake.position[0][0] <= feed_X + 10 and feed_Y - 10 <= snake.position[0][1] <= feed_Y + 10:
        feed_X = random.randint(100,350)
        feed_Y = random.randint(100,350)
        snake.grow()

    

    screen.fill(white)
    pygame.draw.lines(screen, red, True,[(100,100),(100,350),(350,350),(350,100)],5)
    for X,Y in snake.position:
        pygame.draw.rect(screen, green, [X,Y,10,10])
    pygame.draw.rect(screen, black, [feed_X,feed_Y,10,10])
    snake.die()
    
            
    pygame.display.flip()