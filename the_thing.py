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

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.health = 10
        self.images = []
        img = pygame.image.load(os.path.join('images', 'hero.png')).convert()
        img.convert_alpha()
        img.set_colorkey(ALPHA)
        self.images.append(img)
        self.images[0]
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    # with a walk cycle instead

    # def __init__(self):
    #     pygame.sprite.Sprite.__init__(self)
    #     self.images = []
    #     for i in range(1, 5):
            # img = pygame.image.load(os.path.join('images', 'hero' + str(i) + '.png')).convert()
            # img.convert_alpha()
            # img.set_colorkey(ALPHA)
            # self.images.append(img)
            # self.images[0]
            # self.image = self.images[0]
            # self.rect = self.image.get_rect()
        
    def control(self, x, y):
        self.movex += x
        self.movey += y

    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        hit_list = pygame.sprite.spritecollide(self, enemy_list, False)
        for enemy in hit_list:
            self.health -= 1
            print(self.health)

        # With the animations
        # if self.movex < 0:
        #     self.frame += 1
        #     if self.frame > 3 * anims_cycle:
        #         self.frame = 0
        #     self.image = self.images[self.frame//anims_cycle]

        # if self.movex > 0:
        #     self.frame += 1
        #     if self.frame > 3 * anims_cycle:
        #         self.frame = 0
        #     self.image = self.images[(self.frame//anims_cycle) + 4]

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', img))
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0

    # def __init__(self):
    #     pygame.sprite.Sprite.__init__(self)
    #     self.images = []
    #     for i in range(1, 5):
            # img = pygame.image.load(os.path.join('images', 'enemy' + str(i) + '.png')).convert()
            # img.convert_alpha()
            # img.set_colorkey(ALPHA)
            # self.images.append(img)
            # self.images[0]
            # self.image = self.images[0]
            # self.rect = self.image.get_rect()

    def move(self):
        distance = 80
        speed = 8

        if self.counter >= 0 and self.counter <= distance:
            self.rect.x += 1
        elif self.counter >= distance and self.counter <= 2*distance:
            self.rect.x -= 1
        else:
            self.counter = 0

        self.counter += 1

class Level():
    def bad(lvl, eloc):
        if lvl == 1:
            enemy = Enemy(eloc[0], eloc[1], 'enemy1.png')
            enemy_list = pygame.sprite.Group()
            enemy_list.add(enemy)

        if lvl == 2:
            print('Level ' + str(lvl))

        return enemy_list   

'''
setup
'''

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)

worldx = 960
worldy = 720
fps = 40
frame_per_sec = fps
anims_cycle = 4
clock = pygame.time.Clock()
pygame.init()

world = pygame.display.set_mode([worldx, worldy])
backdrop = pygame.image.load(os.path.join('images', 'stage.png').convert())
backdropbox = world.get_rect()

player = Player()
player.rect.x = 0
player.rect.y = 0

player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10

enemy = Enemy(10, 100, 'enemy1.png')
enemy_list = pygame.sprite.Group()
enemy_list.add(enemy)

eloc = []
eloc = [200, 20]
enemy_list = Level.bad(1, eloc)



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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('jump')
                        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps, 0)
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

    # world.blit(backdrop, backdropbox)
    world.fill(BLUE)
    player.update()
    player_list.draw(world)
    enemy_list.draw(world)
    for e in enemy_list:
        e.move()

    pygame.display.flip()
    clock.tick(fps)
