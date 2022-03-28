from pygame.math import Vector2 as V2

# DT = 2.e-4
DT = 0.01
FRICTION_COEFF = -0.01
COLL_TOL = 1
TOL_DEL = COLL_TOL
SPRING_CONSTANT = -1000.
GRAVITY = V2(0, 0)
X_LIM = 10
Y_LIM = 10
screen = None
