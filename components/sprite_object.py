import pygame
from components.constants import *
from math import ceil, sin, cos, pi, tan, sqrt, floor, atan2, tau, hypot


class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, player, map, pos=(300, 350), path='assets/default.png'):
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        self.dx, self.dy = (5, 0)
        # self.mapx = self.x // 25
        # self.mapy = self.y // 25
        # self.mappos = self.mapx, self.map
        self.screen = screen
        self.map = map
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.pos = pos                  # Donato
        self.size = self.rect.size      # Donato
        self.i = 1
        self.flip = 1
        self.frames = 0
        self.mode = 3
        self.angle = 0
        self.rel_angle = 0
        self.speed = 0

        if not hasattr(Enemy, "sprites"):
            Enemy.sprites = self.load_assets()
            print("loading...")
        else:
            print("already loaded!")

    def draw(self):
        if DEVMAP == 1:
            pygame.draw.rect(self.screen, "red", (self.rect.center, (10, 10)))
            # self.rect.x = self.rect.centerx
            # self.rect.y = self.rect.centery
            self.screen.blit(self.image, self.rect)

        # self.move()

        if self.mode == 1:
            top = 20
            self.speed = 10
        if self.mode == 2:
            top = 10
            self.speed = 12
        if self.mode == 3:
            top = 5
            self.speed = 16
        else:
            top = 20

        if self.frames >= top:
            self.frames = 0
            if self.i >= 3:
                self.i = 1
                self.flip *= -1
            else:
                self.i += 1
        else:
            self.frames += 1

        self.rel_angle = (180 - ((self.angle - self.player.angle/DEG) + 90))
        while self.rel_angle >= 360:
            self.rel_angle -= 360
        while self.rel_angle < 0:
            self.rel_angle += 360

        if self.flip == 1:
            image_angle = self.rel_angle
        else:
            image_angle = 180 - self.rel_angle
            if image_angle < 0:
                image_angle += 360

        for i in range(0, 360+45, 45):
            if i-(45 / 2) <= image_angle <= i+(45 / 2):
                image_angle = i

        if image_angle >= 360:
            image_angle -= 360

        # pos = self.rect.center
        # self.image = pygame.image.load('assets/walk/' + str(image_angle) + '_' + str(self.i) + '.png')
        # self.rect = self.image.get_rect()
        # self.rect.center = pos
        self.image = Enemy.sprites[str(image_angle) + '_' + str(self.i)].copy()
        if self.flip == -1:
            self.image = pygame.transform.flip(self.image, True, False)
        # self.cp = self.image.copy()  # holds og for transformation

        # 3D rendering -------------------------------------------------------------------------------------------------

        if DEVMAP != 1:
            xo, yo = self.pos[0] - self.player.rect.centerx + self.dx, self.pos[1] - self.player.rect.centery + 20 + self.dy
            theta = atan2(yo, xo)
            if theta < 0: theta += 2 * pi
            if theta > (2*pi): theta %= 2*pi
            norm_dist = sqrt(xo**2 + yo**2) * cos(theta - self.player.angle)
            # print(self.player.angle - (pi / 6), theta, self.player.angle + (pi / 6))
            # print(self.rect.center)
            # if True:
            # if (not self.check_walls()) and (self.player.angle - (pi / 3)) < theta < (self.player.angle + (pi / 3)) and norm_dist > 0.25:
            fov_top, fov_bottom = self.player.angle + FOV_ANGLE*DEG, self.player.angle - FOV_ANGLE*DEG
            if fov_top > 2*pi: in_view = theta < fov_top % (2*pi) or theta >= fov_bottom
            elif fov_bottom < 0: in_view = theta >= fov_bottom % (2*pi) or theta < fov_top
            else: in_view = fov_bottom <= theta < fov_top

            if in_view and norm_dist > 0.25:

                l = round(25 * RES[1] / (norm_dist + .0001))
                step = (2 * l)
                self.image = pygame.transform.scale(self.image, (2 * round(self.size[0] * RES[1] / norm_dist), step))
                # print((2 * round(self.size[0] * RES[1] / norm_dist), step))

                # rectscreen = pygame.Rect(0, 0, 1, 1)
                self.rect.size = self.image.get_size()

                self.rect.x, self.rect.y = RES[0] * ((theta - (self.player.angle - pi/6)) % (2*pi)) / (pi / 3) - self.image.get_width()//2, MIDPT[1]-l
                # self.image.set_colorkey((255, 255, 255))
                # self.screen.blit(self.image, self.rect)
                # pygame.draw.rect(self.screen, "red", (self.rect.center, (20, 20)))

                on_screen = (self.rect.right > 0) and (self.rect.left <= RES[0])
                if on_screen:
                    # print("good", self.rect, theta, self.player.angle - pi/6)
                    prev_x, prev_y = self.rect.x, self.rect.y
                    # print(self.rect)
                    # self.rect.x, self.rect.y = max(0, self.rect.x), max(0, self.rect.y)
                    if 0 <= (RES[0] - self.rect.x) < self.rect.w:                   # right side off screen
                        self.rect.w = max(0, RES[0] - self.rect.x)
                        # print("right")
                    if self.rect.left < 0 and self.rect.right >= 0:                 # left side off screen
                        self.rect.w = self.rect.right
                        self.rect.left = 0
                        # print("left")
                    if self.rect.top < 0 and self.rect.bottom >= 0:                 # top side off screen
                        self.rect.h = self.rect.bottom
                        self.rect.top = 0
                    if self.rect.bottom >= RES[1] > self.rect.top:                  # bottom side off screen
                        self.rect.h = RES[1] - self.rect.top

                    if 0 <= (RES[1] - self.rect.y) < self.rect.h:
                        self.rect.h = max(0, RES[1] - self.rect.y)

                    x_offset, y_offset = self.rect.x - prev_x, self.rect.y - prev_y

                    # hgt_mask = self.map.heights[self.rect.x: self.rect.x + self.rect.w] > self.rect.y
                    # print(self.rect)
                    scr = pygame.surfarray.pixels2d(self.screen.subsurface(self.rect))
                    r = pygame.Rect((x_offset, y_offset), self.rect.size)
                    # print(r)
                    img = pygame.surfarray.pixels2d(self.image.subsurface(r))
                    hgt_mask = self.map.heights[self.rect.x: self.rect.right] > self.rect.y
                    sprite_mask = img != 0
                    # print(len(hgt_mask), len(sprite_mask))
                    for i, m in enumerate(hgt_mask):
                        if not m: sprite_mask[i] = False

                    scr[sprite_mask] = img[sprite_mask]
                # else:
                #     print("!!!", self.rect, theta, self.player.angle - pi/6, (theta - (self.player.angle - pi/6)))
            # else:
                # print(theta, self.player.angle)

                # if RES[0] - self.rect.x <= self.rect.w:
                #     scr = pygame.surfarray.pixels2d(self.screen.subsurface(self.rect))

                # scr = None
                # img = pygame.surfarray.pixels2d(self.image)

                # for x in range(max(self.rect.x, 0), min(self.rect.right, RES[0]) - 1):
                #     if True or self.rect.y <= heights[x]:
                #         mask = img != 0
                #         scr[mask] = img[mask]

                        # for y in range(max(self.rect.y, 0), min(self.rect.bottom, RES[1]) - 1):
                        #     if ((scr[x][y] >> 24) & 255) == 255:
                        #         scr[x][y] = img[x - self.rect.x][y - self.rect.y] & CLR_W

    def check_walls(self):
        if (self.pos[0] - self.player.rect.centerx) != 0:
            m = (self.pos[1] - self.player.rect.centery) / (self.pos[0] - self.player.rect.centerx)

            x0, y0 = self.pos
            # y = mx + b
            if self.pos[0] < self.player.rect.centerx:
                while x0 < self.player.rect.centerx and (m*x0 + self.pos[1]) < (25*(len(self.map.data[0]))):
                    if self.map.data[int(x0 // 25)][int((m*x0 + self.pos[1]) // 25)] == CLR_WALL:
                        return True         # Hit wall
                    x0 += 25
            else:
                while x0 > self.player.rect.centerx and (m*x0 + self.pos[1]) >= 0:
                    if self.map.data[int(x0 // 25)][int((m*x0 + self.pos[1]) // 25)] == CLR_WALL:
                        return True         # Hit wall
                    x0 -= 25

            # x = my + c
            if m == 0: return False         # avoids unnecessary division by 0
            m = (self.pos[0] - self.player.rect.centerx) / (self.pos[1] - self.player.rect.centery)
            if self.pos[1] < self.player.rect.centery:
                while y0 < self.player.rect.centery and (m*y0 + self.pos[0]) < (25*(len(self.map.data))):
                    if self.map.data[int((m*y0 + self.pos[0]) // 25)][int(y0 // 25)] == CLR_WALL:
                        return True
                    y0 += 25
            else:
                while y0 > self.player.rect.centery and (m*y0 + self.pos[0]) >= 0:
                    if self.map.data[int((m*y0 + self.pos[0]) // 25)][int(y0 // 25)] == CLR_WALL:
                        return True
                    y0 -= 25

            return False        # no walls hit

    def ray_trace(self):

        # TODO: 10 rays, which the monster uses to see
        # TODO: line, which connects monster and player. if line is unobstructed, monster in mode 1 slowly moves toward the player
        #      in mode 2, monster quickly moves toward player. in mode 3, monster wants to lengthen line and obstruct view
        # TODO: usage of rays:

        pass

# line between sprite and player
# if there is an object between player and sprite do not render

    @staticmethod
    def load_assets():
        sprites = dict()
        for i in range(0, 360, 45):
            for o in range(1, 4):
                sprites[str(i) + '_' + str(o)] = pygame.image.load("assets/walk/" + str(i) + "_" + str(o) + ".png").convert_alpha()

        if DEBUG:
            tst = pygame.surfarray.array2d((pygame.image.load("assets/walk/tst.png").convert_alpha()))
            print(tst.dtype)
            clr = tst[1][2]
            print((clr >> 24) & 255, "<< 24 |", (clr >> 16) & 255, "<< 16 |", (clr >> 8) & 255, "<< 8 |", clr & 255)
        return sprites
