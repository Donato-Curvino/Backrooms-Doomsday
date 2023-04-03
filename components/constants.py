from numpy import pi, array
from math import tan

RES = (1280, 720)
MIDPT = (RES[0] // 2, RES[1] // 2)
DEG = pi / 180
FOV_ANGLE = 30
CHECKS_PER_RAY = 25
QUALITY = 4
SCREEN_DIST = (RES[0]/2) / tan((FOV_ANGLE * DEG)/2)
DEBUG = False

# color constants   (r << 16) + (g << 8) + b
CLR_WALL = 255 << 8
