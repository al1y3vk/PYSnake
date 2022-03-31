import pygame as pygame
import sys as system
import time as time
import random as random
from playsound import playsound

difficulty = 25
windowx = 1920
windowy = 1080

errorchecker = pygame.init()

if errorchecker[1] > 0:
    print(f'[!] Had {errorchecker[1]} errors when initialising game, exiting...')
    system.exit(-1)
else:
    print('[+] Game successfully initialised')
    
pygame.display.set_caption('Snake Dövlət')
gamewindow = pygame.display.set_mode((windowx, windowy))

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pseudofps = pygame.time.Clock()
direction = 'RIGHT'
changeto = direction
foodspawn = True
score = 0

foodposition = [random.randrange(1, (windowx // 10)) * 10, random.randrange(1, (windowy // 10)) * 10]
snakeposition = [100, 50]
snakebody = [[100, 50], [100 - 10, 50], [100 - (2 * 10), 50]]

def gameover():
    font = pygame.font.SysFont('consolas', 70)
    endgametext = font.render('Game Over', True, red)
    endgamerect = endgametext.get_rect()
    endgamerect.midtop = (windowx / 2, windowy / 4)
    
    gamewindow.fill(black)
    gamewindow.blit(endgametext, endgamerect)
    showscore(0, red, 'consolas', 20)
    
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    system.exit()
    
def showscore(choice, color, font, size):
    scorefont = pygame.font.SysFont(font, size)
    scoretext = scorefont.render('Score : ' + str(score), True, color)
    scorerect = scoretext.get_rect()
    
    if choice == 1:
        scorerect.midtop = (windowx / 10, 15)
        
    else:
        scorerect.midtop = (windowx / 2, windowy / 1.25)
        
    gamewindow.blit(scoretext, scorerect)
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            system.exit()
            
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
                
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
                
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
                
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
    
    if changeto == 'UP' and direction != 'DOWN':
        direction = 'UP'
        
    if changeto == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
        
    if changeto == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
        
    if changeto == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snakeposition[1] -= 10
        
    if direction == 'DOWN':
        snakeposition[1] += 10
        
    if direction == 'LEFT':
        snakeposition[0] -= 10
        
    if direction == 'RIGHT':
        snakeposition[0] += 10

    snakebody.insert(0, list(snakeposition))
    
    if snakeposition[0] == foodposition[0] and snakeposition[1] == foodposition[1]:
        playsound('apple-crunch.wav')
        score += 1
        foodspawn = False
        
    else:
        snakebody.pop()

    if not foodspawn:
        foodposition = [random.randrange(1, (windowx // 10)) * 10, random.randrange(1, (windowy // 10)) * 10]
        
    foodspawn = True
    gamewindow.fill(black)
    
    for pos in snakebody:
        pygame.draw.rect(gamewindow, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(gamewindow, white, pygame.Rect(foodposition[0], foodposition[1], 10, 10))

    if snakeposition[0] < 0 or snakeposition[0] > windowx - 10:
        gameover()
        
    if snakeposition[1] < 0 or snakeposition[1] > windowy - 10:
        gameover()
    
    for block in snakebody[1:]:
        if snakeposition[0] == block[0] and snakeposition[1] == block[1]:
            gameover()

    showscore(1, white, 'consolas', 20)
    pygame.display.update()
    pseudofps.tick(difficulty)