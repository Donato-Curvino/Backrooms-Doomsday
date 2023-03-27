import pygame
from math import ceil, sin, cos


class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        # required initialization steps
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/arrow.png")
        self.rect = self.image.get_rect()

        # subclass initialization
        self.rect.x = 250
        self.rect.y = 250
        self.speed = 25
        self.angle = 0

        # graphics initialization
        self.screen = screen
        self.icon = pygame.image.load("assets/arrow.png")

    def move(self, dt):
        keys = pygame.key.get_pressed()
        spd = ceil(self.speed * dt * .01) if dt != 0 else 1
        if keys[pygame.K_w]:
            self.rect.y -= spd
        if keys[pygame.K_s]:
            self.rect.y += spd
        if keys[pygame.K_a]:
            self.rect.x -= spd
        if keys[pygame.K_d]:
            self.rect.x += spd

    def raytrace(self):
        pygame.draw.line(self.screen, (255, 255, 255), self.rect.center, (self.rect.centerx, 0), width=1)

    def draw(self):
        self.raytrace()
        self.screen.blit(self.image, self.rect)
