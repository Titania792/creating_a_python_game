import pygame
import sys  # importing modules to use in the program
from pygame.locals import *
from random import randint

pygame.init()  # initializing pygame

# creating a window of size 800x800
window = pygame.display.set_mode((800, 800))
# setting the title of the window
pygame.display.set_caption("Key motion")
# setting the background color
bgcolor = (1, 150, 70)
figurecolor = (255, 255, 255)

# Variables
velocity = 10
direction = True
posX, posY = randint(1, 800), randint(1, 800)

while True:  # loop to keep the window open
    window.fill(bgcolor)  # filling the window with the background color
    pygame.draw.rect(window, figurecolor, (posX, posY, 80, 80))

    for event in pygame.event.get():  # getting the events from the window
        if event.type == QUIT:  # if the event is a quit event
            pygame.quit()  # closing the window
            sys.exit()  # closing the program
        # detecting the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                posX -= velocity
                if posX < 0:
                    posX = 0
            elif event.key == K_RIGHT:
                posX += velocity
                if posX > (800-80):
                    posX = 800-80
            elif event.key == K_UP:
                posY -= velocity
                if posY < 0:
                    posY = 0
            elif event.key == K_DOWN:
                posY += velocity
                if posY > (800-80):
                    posY = 800-80
    pygame.display.update()  # updating the window
