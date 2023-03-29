import pygame
# import numpy
from components.constants import *


class Map(pygame.sprite.Sprite):
    def __init__(self, screen, level):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/" + level + ".png").convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = (0, 0)
        # self.px_arr = pygame.surfarray.pixels2d(self.image)

        self.screen = screen

    def load(self, src):
        pass

    def draw(self):
        self.screen.blit(self.image, self.rect)
