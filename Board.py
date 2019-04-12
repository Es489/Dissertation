import sys
from Tiles import choose_points, create_grid
import pygame
import numpy as np
from pygame.locals import *



BLACK = (0,0,0)
GREEN = (0,255,0)
BROWN = (153,76,0)

TILESIZE = 40
WIDTH = 15
HEIGHT = 15


grid = np.array(create_grid(15, 15))
choose_points(3,grid,2,0)
for j in grid:
    print(j)

tilemap = []
for row in grid:
    l = []
    for column in row:
        if column == '*':
            l.append('PERIMETER')
        elif column == ' ':
            l.append('OTHER')
        else:
            l.append('POINT')
    tilemap.append(l)



colors = { 'PERIMETER':BROWN,
           'OTHER':BLACK,
           'POINT':GREEN}




pygame.init()
DISPLAY = pygame.display.set_mode((WIDTH*TILESIZE, HEIGHT*TILESIZE))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    for row in range(HEIGHT):
        for column in range(WIDTH):
            pygame.draw.rect(DISPLAY, colors[tilemap[row][column]],(column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
    pygame.display.update()