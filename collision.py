import pygame
import sys  # importing modules to use in the program
from pygame.locals import *
from random import randint

pygame.init()  # initializing pygame

# creating a window of size 800x800
window = pygame.display.set_mode((800, 800))
# setting the title of the window
pygame.display.set_caption("Collision")
# setting the background color
bgcolor = (1, 150, 70)
figurecolor1 = (255, 255, 255)
figurecolor2 = (205, 0, 250)

# Variables
velocity = 10
direction = True
posX1, posY1 = randint(1, 800-80), randint(1, 800-80)
posX2, posY2 = randint(1, 800-80), randint(1, 800-80)
side = 80

while True:  # loop to keep the window open
    window.fill(bgcolor)  # filling the window with the background color
    square1 = pygame.draw.rect(
        window, figurecolor1, (posX1, posY1, 80, 80))  # drawing a square
    square2 = pygame.draw.rect(
        window, figurecolor2, (posX2, posY2, 80, 80))  # drawing a square
    # detecting collision
    if square1.colliderect(square2):  # if the two squares collide
        # printing the coordinates of the collision
        print(
            f"Collision!!! square1 in {posX1}, {posY1} and square2 {posX2}, {posY2}")
        # resetting the coordinates of the second square
        posX2, posY2 = randint(1, 800), randint(1, 800)
        square2.left = posX2 - (side / 2)
        square2.top = posY2 - (side / 2)
    # detecting the pointer motion
    posX1, posY1 = pygame.mouse.get_pos()  # getting the coordinates of the pointer
    posX1 = posX1 - (side / 2)
    posY1 = posY1 - (side / 2)
    for event in pygame.event.get():  # getting the events from the window
        if event.type == QUIT:  # if the event is a quit event
            pygame.quit()  # closing the window
            sys.exit()  # closing the program

    pygame.display.update()  # updating the window
