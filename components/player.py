import pygame
import numpy
from math import ceil, sin, cos, pi, tan, sqrt, floor, ceil

from components.map import *
from components.constants import *


class Player:
    def __init__(self, map, icon):
        # required initialization steps
        # pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.image.load("assets/arrow.png").convert_alpha()
        self.rect = icon.get_rect()

        # subclass initialization
        self.rect.center = (75, 75)
        self.speed = 15
        self.angle = 90 * DEG

        # graphics initialization
        # self.screen = screen
        # self.icon = pygame.image.load("assets/arrow.png")

        # helper class initialization
        self.map_data = map.data
        self.map_texture = map.texture

    def collide(self, pos, c=CLR_WALL):
        xpos = int(pos[0] // 25)
        ypos = int(pos[1] // 25)
        # print(pos)
        if c == CLR_WALL:
            # if (self.map_data[xpos][ypos] & 255) > 0 and (self.map_data[xpos][ypos] >> 8 == 255): print(self.map_data[xpos][ypos] & 255)
            return ((self.map_data[xpos][ypos]) >> 8) == 255, (self.map_data[xpos][ypos] & 255)
        else: return self.map_data[xpos][ypos] == c

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

        if self.collide((self.rect.centerx, oldpos[1]))[0]: self.rect.centerx = oldpos[0]
        if self.collide((oldpos[0], self.rect.centery))[0]: self.rect.centery = oldpos[1]

        if keys[pygame.K_LEFT]:
            self.angle -= 2 * DEG * spd * .35
            if self.angle < 0: self.angle += 2*pi
            # self.image = pygame.transform.rotate(self.image, self.angle)
        if keys[pygame.K_RIGHT]:
            self.angle += 2 * DEG * spd * .35
            if self.angle >= (2*pi): self.angle -= 2*pi
            # self.image = pygame.transform.rotate(self.image, -self.angle)
        # print(self.angle)

    def raytrace(self, a):
        """Casts """
        r = 500
        # tan = y/x => x = 25 cot
        # lengths = []

        # for i in numpy.linspace(-FOV_ANGLE, FOV_ANGLE, RES[0] // QUALITY):
        theta = a*DEG + self.angle
        if theta >= (2*pi): theta -= 2*pi
        elif theta < 0: theta += 2*pi
        down = 0 < theta < pi
        right = theta < (pi / 2) or theta > ((3 * pi) / 2)
        ratio = tan(theta)

        dx = 25 * (1 / tan(theta)) * (1 if down else -1) if theta % pi != 0 else None
        dy = 25 * tan(theta) * (1 if right else -1) if (theta - pi / 2) % pi != 0 else None

        # check horizontal -----------------------------------------------------------------------------------------
        x = (self.rect.centerx // 25) * 25
        if right: x += 25
        y_end = (abs(self.rect.centerx - x) / 25) * dy + self.rect.centery if not (dy is None) and dx != 0 else None
        c1 = (False, 0)
        while not (dy is None) and (0 <= y_end < (25 * len(self.map_data))) and (0 <= x < (25 * len(self.map_data[0]))) and not c1[0]:
            c1 = self.collide((x - (0 if right else 25), y_end))
            if c1[0]: break
            x = (x + 25) if right else (x - 25)
            y_end += dy

        # check vertical -------------------------------------------------------------------------------------------
        y = (self.rect.centery // 25) * 25
        if down: y += 25
        x_end = (abs(self.rect.centery - y) / 25) * dx + self.rect.centerx if not (dx is None) and dy != 0 else None
        c2 = (False, 0)
        while not (dx is None) and 0 <= x_end < (25 * len(self.map_data[0])) and (0 <= y <= (25 * len(self.map_data))) and not c2[0]:
            c2 = self.collide((x_end, y - (0 if down else 25)))
            if c2[0]: break
            y = (y + 25) if down else (y - 25)
            x_end += dx

        # check lengths (length of drawn line, shading constant, texture x-coord, texture picker) ------------------
        # ls.append((int(sqrt(x**2 + y_end**2)), int(sqrt(x_end**2 + y**2))))
        l1 = sqrt((x - self.rect.centerx)**2 + (y_end - self.rect.centery)**2) if not (y_end is None) else None
        l2 = sqrt((x_end - self.rect.centerx)**2 + (y - self.rect.centery)**2) if not (x_end is None) else None
        # print(c1[1], c2[1])
        if not (l1 is None) and (l2 is None or l1 < l2):
            endpos = (x, y_end)
            retval = l1 * cos(theta - self.angle), 0, int(y_end % len(self.map_texture[c1[1]])), c1[1]
        else:
            endpos = (x_end, y)
            retval = l2 * cos(theta - self.angle), 1, int(x_end % len(self.map_texture[c2[1]])), c2[1]

        # if DEBUG: pygame.draw.line(self.screen, "white", self.rect.center, endpos)
        # pygame.draw.line(self.screen, "black", self.rect.center, (self.rect.centerx + 50 * cos(self.angle), self.rect.centery + 50 * sin(self.angle)), width=1)
        return retval if not DEBUG else endpos

    def render(self, screen, rays):
        raycheck = []
        if DEBUG:
            for i in rays: pygame.draw.line(screen, "white", self.rect.center, i)
            return raycheck

        for i in range(len(rays)):
            l = round(25 * RES[1] / (rays[i][0] + .0001))
            # pygame.draw.line(screen, (100 - 20*rays[i][1], 0, 0), (i, MIDPT[1] - l), (i, MIDPT[1] + l))
            y_pos = MIDPT[1] - l
            # print(rays[i][3])
            tex = rays[i][3]
            step = (2 * l) / len(self.map_texture[tex][0])
            # print(rays[i][2])
            shading = 20 | (20 << 8) | (20 << 16)

            # temporary precalculated values
            iQ, shr = i * QUALITY, shading * rays[i][1]
            for px in range(len(self.map_texture[tex][0])):
                raycheck.append((i*2, rays[i][0]))
                pygame.draw.line(screen, int(self.map_texture[tex][rays[i][2]][px] - shr), (iQ, int(y_pos)), (iQ, int(y_pos + step)), width=QUALITY)
                y_pos += step
        return raycheck

    def draw(self, screen, rays, icon):
        r = self.render(screen, rays)
        if DEBUG: screen.blit(icon, self.rect)
        return r

    def win(self):
        return True if self.collide(self.rect.center, CLR_WIN) else False


# class MultiTracer(multiprocessing.Pool):
#     def __init__(self, p, *args, **kwargs):
#         multiprocessing.Pool.__init__(self, *args, **kwargs)
#         self.player = p


