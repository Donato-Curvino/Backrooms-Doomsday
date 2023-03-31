from numpy import pi, array

RES = (1280, 720)
MIDPT = (RES[0] // 2, RES[1] // 2)
DEG = pi / 180
FOV_ANGLE = 30
CHECKS_PER_RAY = 25

# color constants   (r << 16) + (g << 8) + b
CLR_WALL = array([0, 255, 0])