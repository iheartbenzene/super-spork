# import numpy as np
# import scipy as sp
# import sklearn as sk 
# import random


# class Room(object):
#     # length = 
#     # width = 
#     # point = 
#     def  __init__(self, l, w, p):
#         self.length, self.width, self.point = l, w, p

# class Dungeon(object):
#     tile = Tile()
#     G = [[tile('X') for i in range(100)]for i in range(100)]
#     def makeDungeon(nRooms):
#       rooms = set(key, value, coded_value)
#       for n in range(nRooms):
#           r = room(randomDim(roomDim))
#           rooms.add(room())

# class Tile(object):
#     image 
#     def __init__(self, c):
#         self.image = c

# class Player(object):
#     pass

# class Enemy(object):
#   pass

# def randomDim(dimensions):
#     # pass in (x0, x1, y0, y1)
#     # initialize random integers for x0, x1, y0, y1
#     pass


import pygame
import sys
import os

'''
objects
'''



'''
setup
'''

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)

worldx = 960
worldy = 720
fps = 40
anims_cycle = 4
clock = pygame.time.Clock()
pygame.init()

world = pygame.display.set_mode([worldx, worldy])
backdrop = pygame.image.load(os.path.join('images', 'stage.png').convert())
backdropbox = world.get_rect()


'''
main loop
'''
main = True

while main == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            pygame.quit()
            sys.exit()
            main = False

        elif event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

    # world.blit(backdrop, backdropbox)
    world.fill(BLUE)

    pygame.display.flip()
    clock.tick(fps)
