import pygame
import numpy
from math import ceil, sin, cos, pi

from components.map import *
from components.constants import *


class Player(pygame.sprite.Sprite):
    def __init__(self, screen, map):
        # required initialization steps
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/arrow.png").convert_alpha()
        self.rect = self.image.get_rect()

        # subclass initialization
        # self.rect.x = 250
        # self.rect.y = 250
        self.rect.center = (500, 400)
        self.speed = 25
        self.angle = -90 * DEG

        # graphics initialization
        self.screen = screen
        self.icon = pygame.image.load("assets/arrow.png")

        # helper class initialization
        self.map = map

    def collide(self, pos):
        b = pygame.surfarray.pixels3d(self.map.image)[pos[0]][pos[1]]
        # print(b, CLR_WALL, pygame.surfarray.pixels3d(self.map.image)[pos[0]][pos[1]], 255 << 8)
        # print(b == CLR_WALL)
        return all(b == CLR_WALL)

    def move(self, dt):
        keys = pygame.key.get_pressed()
        spd = ceil(self.speed * dt * .01) if dt != 0 else 1
        dx, dy = round(spd * cos(self.angle)), round(spd * sin(self.angle))
        oldpos = self.rect.center
        if keys[pygame.K_w]:
            self.rect.center = self.rect.centerx + dx, self.rect.centery + dy
        if keys[pygame.K_s]:
            self.rect.center = self.rect.centerx - dx, self.rect.centery - dy
        if keys[pygame.K_a]:
            self.rect.center = self.rect.centerx + dy, self.rect.centery - dx
        if keys[pygame.K_d]:
            self.rect.center = self.rect.centerx - dy, self.rect.centery + dx

        if self.collide((self.rect.centerx, oldpos[1])): self.rect.centerx = oldpos[0]
        if self.collide((oldpos[0], self.rect.centery)): self.rect.centery = oldpos[1]
        # print(self.collide(newpos))

        if keys[pygame.K_LEFT]:
            self.angle -= 2 * DEG
            # self.image = pygame.transform.rotate(self.image, self.angle)
        if keys[pygame.K_RIGHT]:
            self.angle += 2 * DEG
            # self.image = pygame.transform.rotate(self.image, -self.angle)
        # print(self.angle)

    def raytrace(self):
        r = 500

        for i in numpy.arange(-FOV_ANGLE, FOV_ANGLE, .25):
            endpt = self.rect.center
            for o in range(25):
                endpt = (int(self.rect.centerx + (o * 20) * cos(self.angle + i*DEG)), int(self.rect.centery + (o * 20) * sin(self.angle + i*DEG)))
                # print(endpt)
                if self.collide(endpt):
                    # endpt = (endpt[0] - endpt[0] % 25, endpt[1] - endpt[1] % 25)
                    break

            pygame.draw.line(self.screen, "white", self.rect.center, endpt)
        pygame.draw.line(self.screen, "black", self.rect.center,
                         (self.rect.centerx + r * cos(self.angle), self.rect.centery + r * sin(self.angle)), width=1)

    def draw(self):
        self.raytrace()
        self.screen.blit(self.image, self.rect)
