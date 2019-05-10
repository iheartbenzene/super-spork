import numpy as np
import scipy as sp
import sklearn as sk 
import random


class Room(object):
    # length = 
    # width = 
    # point = 
    def  __init__(self, l, w, p):
        self.length, self.width, self.point = l, w, p

class Dungeon(object):
    tile = Tile()
    G = [[tile('X') for i in range(100)]for i in range(100)]
    def makeDungeon(nRooms):
      rooms = set(key, value, coded_value)
      for n in range(nRooms):
          r = room(randomDim(roomDim))
          rooms.add(room())

class Tile(object):
    image 
    def __init__(self, c):
        self.image = c

class Player(object):
    pass

class Enemy(object):
  pass

def randomDim(dimensions):
    # pass in (x0, x1, y0, y1)
    # initialize random integers for x0, x1, y0, y1
    pass