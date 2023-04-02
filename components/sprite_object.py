import pygame
from components.constants import *
from math import ceil, sin, cos, pi, tan, sqrt, floor, ceil, atan2, tau, hypot

class Sprite(pygame.sprite.Sprite):
    
    def __init__(self, screen, player, map, path='assets/default.png', pos=(302, 490)):
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
        
    def draw(self):
        if DEVMAP == 1:
            pygame.draw.rect(self.screen, "red", (self.rect.center, (10, 10)))
            self.screen.blit(self.image, self.rect)
            
        
        if self.i <= 3:
            self.i = 1
            flip *= -1
        else:
            self.i += 1
            
        #angle = 
        
        self.image = pygame.image.load('assets/walk/' + self.i + '.png', sep='')
        
        
    def move(self):
        
        pass
        
        #movement
        
        self.map.data
        
#line between sprite and player
#if there is an object between player and sprite do not render