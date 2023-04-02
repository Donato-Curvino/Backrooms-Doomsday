import pygame
import numpy
from math import ceil, sin, cos, pi, tan, sqrt, floor, ceil

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
        self.rect.center = (312, 500)
        self.speed = 25
        self.angle = 270 * DEG

        # graphics initialization
        self.screen = screen
        self.icon = pygame.image.load("assets/arrow.png")

        # helper class initialization
        self.map = map

    def collide(self, pos, r=True, d=True):
        xpos = int(int(pos[0]) / 25)
        ypos = int(int(pos[1]) / 25)
        # print(pos)
        return self.map.data[xpos][ypos] == CLR_WALL

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

        if keys[pygame.K_LEFT]:
            self.angle -= 2 * DEG
            if self.angle < 0: self.angle += 2*pi
            # self.image = pygame.transform.rotate(self.image, self.angle)
        if keys[pygame.K_RIGHT]:
            self.angle += 2 * DEG
            if self.angle >= (2*pi): self.angle -= 2*pi
            # self.image = pygame.transform.rotate(self.image, -self.angle)
        # print(self.angle)

    def raytrace(self, DEBUG=False):
        r = 500
        # tan = y/x => x = 25 cot
        lengths = []

        for i in numpy.linspace(-FOV_ANGLE, FOV_ANGLE, RES[0] // 2):
            theta = i*DEG + self.angle
            if theta >= (2*pi): theta -= 2*pi
            elif theta < 0: theta += 2*pi
            down = 0 < theta < pi
            right = theta < (pi / 2) or theta > ((3 * pi) / 2)
            ratio = tan(theta)

            dx = 25 * (1 / tan(theta)) * (1 if down else -1) if theta % pi != 0 else 0
            dy = 25 * tan(theta) * (1 if right else -1) if (theta - pi / 2) % pi != 0 else 0

            # check horizontal -----------------------------------------------------------------------------------------
            x = (self.rect.centerx // 25) * 25
            if right: x += 25
            y_end = (abs(self.rect.centerx - x) / 25) * dy + self.rect.centery if dx != 0 else 10000000

            while (0 <= y_end < (25 * len(self.map.data))) and (0 <= x < (25 * len(self.map.data[0]))) and (not self.collide((x - (0 if right else 25), y_end), right, down)):
                x = (x + 25) if right else (x - 25)
                y_end += dy

            # check vertical -------------------------------------------------------------------------------------------
            y = (self.rect.centery // 25) * 25
            if down: y += 25
            x_end = (abs(self.rect.centery - y) / 25) * dx + self.rect.centerx if dy != 0 else 10000000

            while 0 <= x_end < (25 * len(self.map.data[0])) and (0 <= y <= (25 * len(self.map.data))) and not self.collide((x_end, y - (0 if down else 25)), right, down):
                y = (y + 25) if down else (y - 25)
                x_end += dx

            # check lengths --------------------------------------------------------------------------------------------
            # ls.append((int(sqrt(x**2 + y_end**2)), int(sqrt(x_end**2 + y**2))))
            l1 = sqrt((x - self.rect.centerx)**2 + (y_end - self.rect.centery)**2)
            l2 = sqrt((x_end - self.rect.centerx)**2 + (y - self.rect.centery)**2)
            if l1 < l2:
                endpos = (x, y_end)
                lengths.append((l1 * cos(theta - self.angle), 0, int(y_end % len(self.map.texture))))
            else:
                endpos = (x_end, y)
                lengths.append((l2 * cos(theta - self.angle), 1, int(x_end % len(self.map.texture))))

            if DEBUG: pygame.draw.line(self.screen, "white", self.rect.center, endpos)
        # pygame.draw.line(self.screen, "black", self.rect.center, (self.rect.centerx + 50 * cos(self.angle), self.rect.centery + 50 * sin(self.angle)), width=1)
        return lengths

    def render(self, rays):
        for i in range(len(rays)):
            l = round(25 * RES[1] / (rays[i][0] + .0001))
            # pygame.draw.line(self.screen, (100 - 20*rays[i][1], 0, 0), (i, MIDPT[1] - l), (i, MIDPT[1] + l))
            y_pos = MIDPT[1] - l
            step = (2 * l) / len(self.map.texture[0])
            # print(rays[i][2])
            shading = 20 | (20 << 8) | (20 << 16)
            for px in range(len(self.map.texture[0])):
                pygame.draw.line(self.screen, int(self.map.texture[rays[i][2]][px] - (shading * rays[i][1])), (i * 2, int(y_pos)), (i * 2, int(y_pos + step)), width=2)
                y_pos += step

    def draw(self, DEBUG):
        if DEBUG:
            self.raytrace(DEBUG)
            self.screen.blit(self.image, self.rect)
        else:
            self.render(self.raytrace())
