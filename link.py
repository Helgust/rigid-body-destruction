import matplotlib
import matplotlib.pyplot as plt
import math
from numpy import False_
import pygame
from pygame.math import Vector2 as V2
import pygame.gfxdraw as gfx
import parameters as P


class Links:

  def __init__(self, index0, index1, array):
    self.index0 = index0
    self.index1 = index1
    self.Linked = True
    array[index0].fixedRot = True
    array[index1].fixedRot = True
    delta = array[index0].cm - array[index1].cm
    self.restLength = delta.length()
        
  def update(self,array):
    delta = array[self.index0].cm - array[self.index1].cm
    deltaLength = delta.length()
    # if self.index0 == 3 and self.index1 == 4:
    #     print(deltaLength)
    diff = (deltaLength - self.restLength)/(deltaLength + 0.001)
    if(self.Linked):

      if(deltaLength > 18.1):
        self.Linked = False
        array[self.index0].fixedRot = False
        array[self.index1].fixedRot = False

      array[self.index0].set_pos(array[self.index0].cm - 0.5 * diff * delta)
      array[self.index1].set_pos(array[self.index1].cm + 0.5 * diff * delta)

    
  def draw_debug(self,array):
    x0 = array[self.index0].cm.x
    y0 = array[self.index0].cm.y
    x1 = array[self.index1].cm.x
    y1 = array[self.index1].cm.y
    if self.Linked:
      gfx.line(P.screen, int(x0), int(y0), int(x1), int(y1), (255,0,255))
    else:
      gfx.line(P.screen, int(x0), int(y0), int(x1), int(y1), (255,255,0))