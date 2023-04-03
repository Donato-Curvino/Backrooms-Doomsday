import pygame
from components.player import *
from components.map import *
from components.constants import *
# from components.enemytst import *
# from components.sprite_object import *
import components.game_screen
import time

pygame.init()
screen = pygame.display.set_mode(RES, flags=pygame.RESIZABLE | pygame.SCALED)

running = True
clk = pygame.time.Clock()
dt = 1
# DEBUG = False


# unused in final build
def rainbow(clr, st, incr=1):
    r, g, b = clr
    if st == 1:
        if r > 0:
            r -= incr
            g += incr
        else:
            st = 2
    if st == 2:
        if g > 0:
            g -= incr
            b += incr
        else:
            st = 3
    if st == 3:
        if b > 0:
            b -= incr
            r += incr
        else:
            st = 1
            r -= incr
            g += incr
    return (r, g, b), st


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.dt = 1     # initialize time
        self.xyz = 1234


m = Map(screen)
p = Player(screen, m)
# enemy = Enemy(screen, p, m)


print(screen)
# print(m.pic[0][0] & (255 << 8), 255 << 8)

gs = components.game_screen
state = 0

while running:
    if state == 0 and gs.start_screen(screen):
        state = gs.start_screen(screen)
    elif state == 1 and gs.main_game(screen, p, m, clk, DEBUG, dt):
        state = gs.main_game(screen, p, m, clk, DEBUG, dt)
    elif state == 4 and gs.end_screen(screen):
        running = False


    for e in pygame.event.get():
        if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
            running = False
            pygame.quit()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            state = 4
            
    pygame.display.update()

pygame.quit()

