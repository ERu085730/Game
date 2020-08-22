import pygame

class character(object):
    def __init__(self ,char ,x ,y ,width ,height):
        self.char = char
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.step = 5
        self.walkcount = 0
        self.jump = False
        self.jumping = 9
        self.hitbox =(self.x+5, self.y+10 ,50 ,40)
        self.health = 3

    def action(self ,screen):
        if self.walkcount +1 >= 12:
            self.walkcount = 0

        screen.blit(self.char[(self.walkcount//3)+4] ,(round(self.x) ,round(self.y)))
        self.walkcount +=1        
        self.hitbox = (round(self.x+5), round(self.y+10) ,50 ,40)
        #pygame.draw.rect(screen ,(255 ,0 ,0) ,self.hitbox ,2)
    def hit(self):
        self.health -= 1
        print('bark!')
        

class trap(object):
    def __init__(self ,trap ,x ,y ,width ,height):
        self.trap = trap
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x ,self.y ,self.width ,self.height)

    def action(self ,screen):
        screen.blit(self.trap ,(self.x ,self.y))
        self.hitbox = (self.x ,self.y+5 ,self.width , self.height)
        #pygame.draw.rect(screen ,(255 ,0 ,0) ,self.hitbox ,2)

    
