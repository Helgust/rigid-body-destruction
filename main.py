from __future__ import print_function, division
from ast import Constant
from chess import WHITE
import pygame
from pygame.math import Vector2 as V2
import pygame.gfxdraw as gfx
from pymunk import Constraint
import sys
import physics
import parameters #all physical quantities are defined here
import link

import pygame, sys, math

pygame.init()

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()
W, H = 400, 400 #size of the domain (and size of screen)
screen = pygame.display.set_mode((W, H), 0, 32)
parameters.screen = screen
pygame.display.set_caption('Rigid Body System')

def draw_meshes():
    for m in meshes:
        m.draw()

def refresh_physics():
    for m in meshes:
        m.refresh_physics()
    for l in  links1:
        l.update(rect1)
    for l in  links2:
        l.update(rect2)

NUM_X = 3
NUM_Y = 5
links1 = []
links2 = []

rect1 = []
for i in range(NUM_Y):
    for j in range(NUM_X):
        m1 = physics.get_polygon(4, 10)
        m1.rotate(45)
        m1.set_pos((50 + 18*j, -25 + H//2+18*i))
        rect1.append(m1)
      
rect2 = []
for i in range(1):
    for j in range(5):
        m2 = physics.get_polygon(4, 10)
        m2.rotate(45)
        m2.set_pos((150 + 15*j,H//2+15*i))
        m2.velocity = V2(-70, 0.)
        rect2.append(m2)

m3 = physics.get_polygon(4,250)
m3.rotate(45)
m3.set_pos((W//2,H//2))
m3.normal = -1. #invert normals
m3.fixed = True #object never moves


for j in range(NUM_Y):
    for i in range(NUM_X):
        if i < (NUM_X - 1):
            index0 = i + j * NUM_X
            index1 = (i + 1) + j * NUM_X
            c = link.Links(index0, index1, rect1)
            links1.append(c)
        if j < (NUM_Y - 1):
            index0 = i + j * NUM_X
            index1 = i + (j + 1) * NUM_X
            c = link.Links(index0, index1, rect1)
            links1.append(c)

for j in range(1):
    for i in range(5):
        if i < (5 - 1):
            index0 = i + j * 5
            index1 = (i + 1) + j * 5
            c = link.Links(index0, index1, rect2)
            links2.append(c)
        if j < (1 - 1):
            index0 = i + j * 5
            index1 = i + (j + 1) * 5
            c = link.Links(index0, index1, rect2)
            links2.append(c)

#Dense cells
# for j in range(NUM_Y):
#     for i in range(NUM_X):
#         if i < (NUM_X - 1):
#             index0 = i + j * NUM_X
#             index1 = (i + 1) + j * NUM_X
#             c = link.Links(index0, index1, rect1)
#             links.append(c)
#         if j < (NUM_Y - 1):
#             index0 = i + j * NUM_X
#             index1 = i + (j + 1) * NUM_X
#             c = link.Links(index0, index1, rect1)
#             links.append(c)

# for j in range(NUM_Y - 1):
#     for i in range(NUM_X - 1):
#         index0 = i + j * NUM_X
#         index1 = (i + 1) + (j + 1) * NUM_X
#         c = link.Links(index0, index1, rect1)
#         links.append(c)
#     for i in range(1, NUM_X):
#         index0 = i + j * NUM_X
#         index1 = (i - 1) + (j + 1) * NUM_X
#         c = link.Links(index0, index1, rect1)
#         links.append(c)



 

# m1.set_pos((W//2,H//2))
# m1.rotate(180)
# m2.set_pos(m1.cm + (0,-120)) #.cm denotes the center of mass

# m3 = physics.get_polygon(4,800)
# m3.rotate(45)
# m3.set_pos((W//2,H//2))
# m3.normal = -1. #invert normals
# m3.fixed = True #object never moves

# m4 = physics.get_polygon(3,20)
# m4.set_pos(m1.cm+(40,0))
# m5 = physics.get_polygon(3,20)
# m5.set_pos(m1.cm-(40,0))

meshes = [m3] + rect1 + rect2

#m1.ang_velocity = 1.


# ##############################################################################
iteration = 1
loop = True
# parameters.clock = pygame.time.Clock()
SHOWITER = 1



while loop:
    screen.fill((225,225,225))
    physics.add_forces(meshes)
    refresh_physics()
    # for m in meshes:
    #     m.draw_normals()
    for l in links1:
        l.draw_debug(rect1)
    for l in links2:
        l.draw_debug(rect2)
    draw_meshes()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    pygame.display.update()
    fpsClock.tick(FPS)
