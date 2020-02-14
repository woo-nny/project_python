import pygame
import time 
import random
from datetime import datetime
from datetime import timedelta

pygame.init() # pygame 초기화
SCREEN_WIDTH = 500 # 스크린 가로
SCREEN_HEIGHT = 500 # 스크린 세로
BLOCK_SIZE = 20
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT )) # 화면 크기
font = pygame.font.SysFont("consolas",20)
# RGB 색깔 기존 변수
BLACK= ( 0,  0,  0)
WHITE= (255,255,255)
BLUE = ( 0,  0,255)
GREEN= ( 0,255,  0)
RED  = (255,  0,  0)

pygame.display.set_caption("J-Dragon Snake") # 게임 제목
done =False
clock=pygame.time.Clock() # FPS 화면을 초당 몇 번 출력 하겠는가?
last_turn_time = datetime.now()
DIRECTION_ON_KEY = {
    pygame.K_UP : 'north',
    pygame.K_DOWN :'south',
    pygame.K_LEFT : 'west',
    pygame.K_RIGHT : 'east'
}
block_direction = 'east'


def draw_background(screen): #게임 배경 그린다
    background = pygame.Rect((0,0),(SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.draw.rect(screen,WHITE,background)
def draw_block(screen,color,position): #position 위치에 color 색깔의 블록 그린다
    block = pygame.Rect((position[1]*BLOCK_SIZE,position[0]*BLOCK_SIZE),(BLOCK_SIZE,BLOCK_SIZE)) # y,x좌표
    pygame.draw.rect(screen,color,block)
def printText(msg,color = 'BLACK', pos=(50,50)): #메시지 출력
    textSurface = font.render(msg,True,pygame.Color(color),None)
    textRect = textSurface.get_rect()
    textRect.topleft = pos
    screen.blit(textSurface,textRect)
class Snake: #뱀
    color = GREEN # 뱀 색
    def __init__(self):
        self.position = [(9,6),(9,7),(9,8),(9,9)]
        self.direction = 'north' #뱀 처음 방향
    def draw(self,screen): # 뱀 그리기
        for position in self.position:
            draw_block(screen,self.color,position)
    def move(self): # 뱀 움직임
        head_position = self.position[0] # 뱀 머리 위치
        y,x = head_position
        if self.direction == 'north': #방향 위쪽
            self.position = [(y - 1, x)] + self.position[:-1]
        elif self.direction == 'south': # 방향 아래쪽
            self.position = [(y + 1, x)] + self.position[:-1]
        elif self.direction == 'west': # 방향 왼쪽
            self.position = [(y, x - 1)] + self.position[:-1]
        elif self.direction == 'east': # 방향 오른쪽
            self.position = [(y, x + 1)] + self.position[:-1]
        # print(self.position[0])
    def turn(self,direction):
        self.direction= direction
    def grow(self): # 먹이 먹을시
        tail_positon = self.position[-1] #꼬리 위치
        y,x = tail_positon
        if self.direction == 'north':
            self.position.append((y - 1, x))
        elif self.direction == 'south':
            self.position.append((y + 1, x))
        elif self.direction == 'west':
            self.position.append((y, x - 1))
        elif self.direction == 'east':
            self.position.append((y, x + 1))
class food: # 먹이
    color = RED # 먹이 색
    def __init__(self,position=(5,5)):
        self.position = position # 먹이 위치
    def draw(self,screen): #먹이 그림
        draw_block(screen,self.color,self.position)
class GameBoard: # 게임판
    def __init__(self):
        self.Snake =Snake()
        self.food = food()
    def draw(self,screen): #게임판 그리기
        self.Snake.draw(screen)
        self.food.draw(screen)
    def process_turn(self): # 게임 한판
        self.Snake.move()
        a,b=self.Snake.position[0]
        if self.Snake.position[0] == self.food.position: # 뱀 머리가 먹이 위치와 같을 경우
            self.Snake.grow()
            self.put_new_food()
            return False
        if self.Snake.position[0] in self.Snake.position[1:]: #뱀 머리가 몸에 닫을 경우
            return True
        if a <= 0 or a >= 24 or b <= 0 or b >= 24: # 좌표 a,b 게임판을 벗어날 경우
            return True
    def put_new_food(self): # 새로운 먹이 놓는 것
        self.food = food((random.randint(0,20),random.randint(0,20)))
        for position in self.Snake.position:
            if self.food.position == position:
                self.put_new_food()
                break
game = GameBoard()
TURN_INTERVAL = timedelta(seconds=0.3)
while not done: # 무한 반복
    clock.tick(60) # 프레임 10,30,60 적당 높을 수록 cpu 사용량 증가
    for event in pygame.event.get(): # 게임 이벤트 발생 여부 확인
        if event.type == pygame.KEYDOWN: # 키를 누르면 flag TURE
            if event.key in DIRECTION_ON_KEY:
                game.Snake.turn(DIRECTION_ON_KEY[event.key])
        if event.type == pygame.QUIT: # 이벤트가 quit 클릭 시
            done = True # 무한반복 나감
    if TURN_INTERVAL < datetime.now() - last_turn_time:
        done=game.process_turn()
        last_turn_time = datetime.now()
    draw_background(screen)
    game.draw(screen)
    pygame.display.update()
printText("Game Over",BLACK,pos=(50,50))
pygame.QUIT

