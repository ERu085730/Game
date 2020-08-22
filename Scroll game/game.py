import pygame
import random
from character import *

#initial game
pygame.font.init()
pygame.init()

#set game screen width and height
screen_width = 1024
screen_height = 768

screen = pygame.display.set_mode((screen_width ,screen_height))

pygame.display.set_caption('LuckyGoGO')

#load element
bg = pygame.image.load('Ex/bg.jpg')
char = [pygame.image.load('Ex/'+str(t)+'.png') for t in range(5,13)]
tp = pygame.image.load('Ex/trap.png').convert()
tp.set_colorkey((255 ,255 ,255))

#Sound effect
hit_sound = pygame.mixer.Sound('Ex/hit.wav')
pygame.mixer.music.load('Ex/music.mp3')
pygame.mixer.music.play(-1)

man = character(char ,250 ,600 ,64 ,64)
traps = []
clock = pygame.time.Clock()

bx = 0
bx1 = 1024


def renew():
     global bx ,bx1,bones
     screen.blit(bg ,(bx ,0))
     screen.blit(bg ,(bx1,0))
     for bone in bones:
          screen.blit(bone ,(bones.index(bone) * 100 + 20 ,20))
     for t in traps:
          t.action(screen)
     man.action(screen)
     pygame.display.update()
    
def main(screen):
    global bones  
    bones =[pygame.image.load('Ex/bone1.jpg') for _ in range(3)]
    run = True
    nohurt = 0
    while run:
        clock.tick(32)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break

        if len(bones) == 0:
             screen.fill((0 ,0 ,0))
             menu_text(screen ,'Game Over' ,60 ,(255 ,255 ,255))
             pygame.display.update()
             traps.clear()
             i = 0
             while i < 200:
                 pygame.time.delay(5)
                 for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                     break
                 i+=1
             menu(screen)
             
             
        keys = pygame.key.get_pressed()
        global bx ,bx1
        
        if bx < -1024:
             bx +=1024
             bx1 += 1024
        elif bx1 > 1024:
             bx -= 1024
             bx1 -= 1024

        bx -= 10
        bx1 -= 10

        if len(traps) < 2:
             traps.append(trap(tp ,random.random() * 300 *(len(traps)+1) + 1024 ,600 ,50 ,50))
        if nohurt == 0:
             for t in traps:
                  if man.x + man.width > t.x and man.x < t.x + t.width:
                       if man.y + man.height > t.y and man.y < t.y +t.height:
                            hit_sound.play()
                            man.hit()
                            bones.pop(len(bones) - 1)
                            nohurt = 32
        else:
             nohurt -= 1

        for t in traps:
             if t.x + t.width > 0:
                  t.x -= 10
             else:
                  traps.pop(traps.index(t))
                  
        

        if not(man.jump):
             if keys[pygame.K_UP]:
                  man.jump = True
                  man.walkcount = 0
        else:
             if man.jumping >= -9:
                  neg = 1
                  if man.jumping < 0:
                       neg = -1
                  man.y -= (man.jumping ** 2) * 0.5 * neg
                  man.jumping -= 1
             else:
                  man.jump = False
                  man.jumping = 9
        renew()
          
def menu_text(screen ,text ,size ,color):
    font = pygame.font.SysFont('comicsans' ,size ,bold = True)
    label = font.render(text ,1 ,color)
    screen.blit(label ,(512-label.get_width()//2 ,384-label.get_height()//2))

def menu(screen):
    run  = True
    while run:
        screen.fill((0 ,0 ,0))
        menu_text(screen ,'Press Any Key To Play' ,60 ,(255 ,255 ,255))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main(screen)  
    pygame.display.quit()



menu(screen)
