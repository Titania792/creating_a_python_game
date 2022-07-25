import pygame
import sys  # importing modules to use in the program
from pygame.locals import *
from random import randint

pygame.init()  # initializing pygame

# creating a window of size 800x800
window = pygame.display.set_mode((800, 800))
# setting the title of the window
pygame.display.set_caption("Mouse motion")
# setting the background color
bgcolor = (1, 150, 70)
figurecolor = (255, 255, 255)

# Variables
velocity = 10
direction = True
posX, posY = randint(1, 800), randint(1, 800)
side = 80

while True:  # loop to keep the window open
    window.fill(bgcolor)  # filling the window with the background color
    pygame.draw.rect(window, figurecolor, (posX, posY, 80, 80))
    # detecting the pointer motion
    posX, posY = pygame.mouse.get_pos()  # getting the coordinates of the pointer
    posX = posX - (side / 2)
    posY = posY - (side / 2)
    for event in pygame.event.get():  # getting the events from the window
        if event.type == QUIT:  # if the event is a quit event
            pygame.quit()  # closing the window
            sys.exit()  # closing the program

    pygame.display.update()  # updating the window
