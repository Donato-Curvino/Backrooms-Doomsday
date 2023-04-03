import pygame
from components.constants import *
from math import atan2, pi, sqrt, cos


class Entity(pygame.sprite.Sprite):
    def __init__(self, s, p):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/walk/270_2.png")
        self.rect = self.image.get_rect()
        self.og_pic = self.image.copy()

        self.screen = s
        self.player = p

        self.pos = (312, 250)
        self.size = self.rect.size

    def draw(self):
        xo, yo = self.pos[0] - self.player.rect.centerx, self.pos[1] - self.player.rect.centery
        angle = atan2(yo, xo)
        if angle < 0: angle += 2*pi
        dist = sqrt(xo**2 + yo**2) * cos(angle - self.player.angle)
        # print(self.player.angle - (pi / 6), angle, self.player.angle + (pi / 6))
        if (self.player.angle - (pi/6)) < angle < (self.player.angle + (pi/6)):
            self.image = pygame.transform.scale(self.og_pic, (round(self.size[0] * RES[1] / dist) , round(self.size[1] * RES[1] / dist)))

            self.rect.midbottom = (RES[0] * (angle - (self.player.angle - (pi/6))) / (pi/3), MIDPT[1] + round(25 * RES[1] / dist))
            self.screen.blit(self.image, self.rect)

