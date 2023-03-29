import pygame
from components.player import *
from components.map import *

pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True
clk = pygame.time.Clock()
dt = 1


def rainbow(rgb, state, chng=1):
    r, g, b = rgb
    if state == 1:
        if r > 0:
            r -= chng
            g += chng
        else:
            state = 2
    if state == 2:
        if g > 0:
            g -= chng
            b += chng
        else:
            state = 3
    if state == 3:
        if b > 0:
            b -= chng
            r += chng
        else:
            state = 1
            r -= chng
            g += chng
    return (r, g, b), state


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.dt = 1     # initialize time
        self.xyz = 1234


m = Map(screen, "tst1")
p = Player(screen, m)

rgb, state = (255, 0, 0), 1
chng = 0

print(screen)

while running:
    rgb, state = rainbow(rgb, state, chng)
    # print(rgb)
    screen.fill(rgb)

    p.move(dt)
    # screen.blit(p.image, p.rect)
    m.draw()
    p.draw()

    dt = clk.tick(60)
    # print(dt)
    pygame.display.flip()

    for e in pygame.event.get():
        if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
            running = False
            pygame.quit()

# pygame.quit()

