import pygame
import numpy
from math import ceil, sin, cos, pi

DEG = pi / 180


class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        # required initialization steps
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/arrow.png").convert_alpha()
        self.rect = self.image.get_rect()

        # subclass initialization
        self.rect.x = 250
        self.rect.y = 250
        self.speed = 25
        self.angle = -90 * DEG

        # graphics initialization
        self.screen = screen
        self.icon = pygame.image.load("assets/arrow.png")

    def move(self, dt):
        keys = pygame.key.get_pressed()
        spd = ceil(self.speed * dt * .01) if dt != 0 else 1
        dx, dy = round(spd * cos(self.angle)), round(spd * sin(self.angle))
        if keys[pygame.K_w]:
            self.rect.x, self.rect.y = self.rect.x + dx, self.rect.y + dy
        if keys[pygame.K_s]:
            self.rect.x, self.rect.y = self.rect.x - dx, self.rect.y - dy
        if keys[pygame.K_a]:
            self.rect.x, self.rect.y = self.rect.x + dy, self.rect.y - dx
        if keys[pygame.K_d]:
            self.rect.x, self.rect.y = self.rect.x - dy, self.rect.y + dx

        if keys[pygame.K_LEFT]:
            self.angle -= 2 * DEG
            # self.image = pygame.transform.rotate(self.image, self.angle)
        if keys[pygame.K_RIGHT]:
            self.angle += 2 * DEG
            # self.image = pygame.transform.rotate(self.image, -self.angle)
        # print(self.angle)

    def raytrace(self):
        r = 500

        for i in numpy.arange(-45, 45, .25):
            pygame.draw.line(self.screen, "white", self.rect.center, (self.rect.centerx + r * cos(self.angle + i*DEG),
                             self.rect.centery + r * sin(self.angle + i*DEG)))
        pygame.draw.line(self.screen, "black", self.rect.center, (self.rect.centerx + r * cos(self.angle), self.rect.centery + r * sin(self.angle)), width=1)

    def draw(self):
        self.raytrace()
        self.screen.blit(self.image, self.rect)
