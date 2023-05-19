from numpy import pi, array
from math import tan
import numpy

RES = (800, 600)
MIDPT = (RES[0] // 2, RES[1] // 2)
DEG = pi / 180
FOV_ANGLE = 30
CHECKS_PER_RAY = 25
QUALITY = 1
SCREEN_DIST = (RES[0]/2) / tan((FOV_ANGLE * DEG)/2)
DEBUG = False
DEVMAP = 1 if DEBUG else 0

# color constants   (r << 16) + (g << 8) + b
CLR_WALL = 255 << 8
CLR_WIN = (255 << 16) + (255 << 8)
CLR_BACKGROUND = (230 << 16) | (230 << 8) | 155

ANGLES = numpy.linspace(-FOV_ANGLE, FOV_ANGLE, RES[0] // QUALITY)
