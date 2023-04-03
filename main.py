import pygame
from components.player import *
from components.map import *
from components.constants import *
from components.enemytst import *
from components.sprite_object import *

pygame.init()
screen = pygame.display.set_mode(RES, flags=pygame.RESIZABLE | pygame.SCALED)
running = True
clk = pygame.time.Clock()
dt = 1
# DEBUG = False


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
enemy = Sprite(screen, p, m)

rgb, state = (255, 0, 0), 1
chng = 0

print(screen)
# print(m.pic[0][0] & (255 << 8), 255 << 8)


while running:
    rgb, state = rainbow(rgb, state, chng)
    # print(rgb)
    screen.fill((230, 230, 155))

    p.move(dt)
    # screen.blit(p.image, p.rect)
    m.draw(DEBUG)
    raycheck = p.draw(DEBUG)
    enemy.draw(raycheck)

    dt = clk.tick(60)
    # print(dt)
    pygame.display.flip()
    # print(p.angle)

    for e in pygame.event.get():
        if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
            running = False
            pygame.quit()

# pygame.quit()

