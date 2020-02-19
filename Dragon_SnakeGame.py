import pygame, sys
from pygame.locals import *
import random
from datetime import timedelta, datetime
import time

#뱀 클래스
class Snake:
    def __init__(self): # 뱀생성
        self.position = [[130,130]]
        self.direction = "under" # 자동으로 움직이는 방향
    # 시간의 흐름에 따른 기본적인 움직임과 마우스 클릭에 따른 움직임을 정해주는 함수
    def automove(self):
        X, Y = self.position[0]
        if self.direction == "right":
            self.position = [[X+10,Y]] + self.position[:-1]
        elif self.direction == "left":
            self.position = [[X-10,Y]] + self.position[:-1]
        elif self.direction == "over":
            self.position = [[X,Y+10]] + self.position[:-1]
        else :
            self.position = [[X,Y-10]] + self.position[:-1]
    # 마우스 클릭에 따라 어느 방향으로 얼마만큼 이동할지 판단해주는 함수.
    def movement(self, a,b):
        X, Y = self.position[0]
        if a >= X and abs(a - X) >= abs(b - Y):
            self.direction = "right"
        elif a <= X and abs(a - X) >= abs(b - Y):
            self.direction = "left"
        elif b >= Y and  abs(a - X) <= abs(b - Y):
            self.direction = "over"
        elif b <= Y and abs(a - X) <= abs(b - Y):
            self.direction = "under"
    # 먹이를 먹어 커지는 경우
    def grow(self):
        if (gameboard.feed.feed_X - 10 <= gameboard.snake.position[0][0] <= gameboard.feed.feed_X + 10 
        and gameboard.feed.feed_Y - 10 <= gameboard.snake.position[0][1] <= gameboard.feed.feed_Y + 10):
            gameboard.feed.change_position()
            X,Y = self.position[-1]
            if self.direction == "right":
                self.position.append([X-10,Y])
            elif self.direction == "left":
                self.position.append([X+10,Y])
            elif self.direction == "over":
                self.position.append([X,Y-10])
            else :
                self.position.append([X,Y+10])
    # 죽는 경우
    def die(self):
        if self.position[0] in self.position[1:] or (gameboard.snake.position[0][0] < 100 or gameboard.snake.position[0][0] > 350 
        or gameboard.snake.position[0][1] < 100 or gameboard.snake.position[0][1] > 350):
            return "die"
        else:
            return None
    
    def reset(self):
        self.position = [[130,130]]
        self.direction = "under"

class Feed:
    def __init__(self):
        self.feed_X = random.randint(100,350)
        self.feed_Y = random.randint(100,350)
    def change_position(self):
        self.feed_X = random.randint(100,350)
        self.feed_Y = random.randint(100,350)
        
class get_click:
    def __init__(self):
        self.X = 150
        self.Y = 140
    def getpoint(self):
        a, b = pygame.mouse.get_pos()
        self.X = a
        self.Y = b

class Game_board:

    def __init__(self):
        self.snake = Snake()
        self.feed = Feed()
        
    def die(self):
        global state_snake_die
        global state_feed_die
        if self.snake.die() is not None:
            if len(state_snake_die)==0:
                for X, Y in self.snake.position:
                    state_snake_die.append([X,Y])
                state_feed_die = [self.feed.feed_X,self.feed.feed_Y]
            return "die"
        else:
            return None

    
    def move(self, X, Y):
        self.snake.movement(X,Y)
        self.snake.automove()
    
    def grow(self):
        self.snake.grow()

    def Time(self,Interval,lasttime,sec, X, Y):
        if Interval < datetime.now() - lasttime:
            self.feed.feed_X, self.feed.feed_Y = random.randint(100,350), random.randint(100,350)
            lasttime = datetime.now()
        if datetime.now() - sec > sec_interval or Change_Flag:
            gameboard.move(X,Y)
            sec = datetime.now()
        return lasttime,sec
# 죽었을때와, 죽지 않았을때를 나눠서 출력하게 만듦.
    def draw(self,die_commend):
        global state_snake_die
        global state_feed_die
        if die_commend == None:
            screen.fill(white)
            pygame.draw.lines(screen, red, True,[(100,100),(100,350),(350,350),(350,100)],5)
            for X,Y in self.snake.position:
                pygame.draw.rect(screen, green, [X,Y,10,10])
            pygame.draw.rect(screen, black, [gameboard.feed.feed_X,gameboard.feed.feed_Y,10,10])
            pygame.display.flip()
        else:
            button = Button()
            screen.fill(white)
            pygame.draw.lines(screen, red, True,[(100,100),(100,350),(350,350),(350,100)],5)
            for X,Y in state_snake_die:
                pygame.draw.rect(screen, green, [X,Y,10,10])
            pygame.draw.rect(screen, black, [state_feed_die[0],state_feed_die[1],10,10])
            button.gameover()
            button.retry()
            pygame.display.flip()
    def Newgame(self):
        global state_feed_die
        global state_snake_die
        state_feed_die = []
        state_snake_die = []

# 게임에서 졋을때 나올 버튼들을 만드는 장소
class Button:
    
    def gameover(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        overtext = font.render('Game Over', True, green, blue)
        overtextRect = overtext.get_rect()
        overtextRect.center = (ScreenSize[0] // 2, ScreenSize[1] // 2)
        return screen.blit(overtext,overtextRect)
    def retry(self):
        font = pygame.font.Font('freesansbold.ttf', 16)
        retrytext = font.render('화면을 클릭하면 retry',True,green,blue)
        retrytextRect = retrytext.get_rect()
        retrytextRect.center = (ScreenSize[0] // 2 + 16, ScreenSize[1] // 2 + 64)
        return screen.blit(retrytext,retrytextRect)
    
    def click_retry(self,die_com,Change_Flag):
        if die_com != None and Change_Flag == True:
            global gameboard
            gameboard.Newgame()
            gameboard = Game_board()
                


pygame.init()   
ScreenSize = (800,800)
screen = pygame.display.set_mode(ScreenSize) # 화면크기 설정  
pygame.display.set_caption('Snake Game')         # 윈도우 타이틀 설정


black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#보드에 나올 객체 및 클릭좌표, 죽었을 때 인식할 좌표 저장공간.
gameboard = Game_board()
button = Button()
click = get_click()
state_snake_die = []
state_feed_die = []
die_com = None

#시간관리 영역
Interval = timedelta(seconds=10)
lasttime = datetime.now()
sec = datetime.now()
sec_interval = timedelta(seconds=1)



while True:
    Change_Flag = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click.getpoint()
            Change_Flag = True
    button.click_retry(die_com,Change_Flag)
    lasttime,sec = gameboard.Time(Interval,lasttime,sec,click.X,click.Y)
    gameboard.grow()
    die_com = gameboard.die()
    gameboard.draw(die_com)

    
    
    