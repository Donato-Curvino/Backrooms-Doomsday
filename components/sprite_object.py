import pygame
from components.constants import *
from math import ceil, sin, cos, pi, tan, sqrt, floor, ceil, atan2, tau, hypot

class Sprite(pygame.sprite.Sprite):
    
    def __init__(self, screen, player, map, path='assets/default.png', pos=(300, 300)):
        self.player = player
        #self.x, self.y = pos
        #self.mapx = self.x // 25
        #self.mapy = self.y // 25
        #self.mappos = self.mapx, self.map
        self.screen = screen
        self.map = map
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.i = 1
        self.flip = 1
        self.frames = 0
        self.mode = 3
        self.angle = 0
        self.rel_angle = 0
        self.aitest = 20
        
    def draw(self):
        if DEVMAP == 1:
            pygame.draw.rect(self.screen, "red", (self.rect.center, (10, 10)))
            #self.rect.x = self.rect.centerx
            #self.rect.y = self.rect.centery
            self.screen.blit(self.image, self.rect)
            
        #self.move()
        
        if self.mode == 1:
            top = 20
            speed = 10
        if self.mode == 2:
            top = 10
            speed = 12
        if self.mode == 3:
            top = 5
            speed = 16
        
        if self.frames >= top:
            self.frames = 0
            if self.i >= 3:
                self.i = 1
                self.flip *= -1
            else:
                self.i += 1
        else:
            self.frames += 1
            
        self.rel_angle = -(180 - ((self.angle - self.player.angle/DEG) + 90))
        while self.rel_angle >= 360:
            self.rel_angle -= 360
        while self.rel_angle < 0:
            self.rel_angle += 360
            
        if self.flip == 1:
            image_angle = self.rel_angle
        else:
            image_angle = 180 - self.rel_angle
            if image_angle < 0:
                image_angle += 360
        
        for i in range(0, 360+45, 45):
            if image_angle >= i-(45/2) and image_angle <= i+(45/2):
                image_angle = i
        
        if(image_angle >= 360):
            image_angle -= 360
        
        pos = self.rect.center
        self.image = pygame.image.load('assets/walk/' + str(image_angle) + '_' + str(self.i) + '.png')
        self.rect = self.image.get_rect()
        self.rect.center = pos
        if self.flip == -1:
            self.image = pygame.transform.flip(self.image, True, False)
        
        
    def ray_trace(self):
        
        #TODO: 10 rays, which the monster uses to see
        #TODO: line, which connects monster and player. if line is unobstructed, monster in mode 1 slowly moves toward the player
        #      in mode 2, monster quickly moves toward player. in mode 3, monster wants to lengthen line and obstruct view
        #TODO: usage of rays: 
        
        pass
        
#line between sprite and player
#if there is an object between player and sprite do not render