from numpy import pi, array
from math import tan
import numpy as np

RES = (800, 600)
MIDPT = (RES[0] // 2, RES[1] // 2)
DEG = pi / 180
FOV_ANGLE = 30
CHECKS_PER_RAY = 25
QUALITY = 1
SCREEN_DIST = (RES[0]/2) / tan((FOV_ANGLE * DEG)/2)
DEBUG = False
DEVMAP = 1 if DEBUG else 0

# color constants   (r << 16) + (g << 8) + b, now in hex
CLR_WALL = 0xff00
CLR_WIN = 0xffff00
CLR_BACKGROUND = 0xe6e69b
CLR_W = 0xffffff

ANGLES = np.linspace(-FOV_ANGLE, FOV_ANGLE, RES[0] // QUALITY)
A_TO_PX = dict(zip(ANGLES, range(RES[0])))
# print(A_TO_PX)
