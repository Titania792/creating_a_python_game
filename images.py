import pygame
import sys  # importing modules to use in the program
from pygame.locals import *
from random import randint

pygame.init()  # initializing pygame

# creating a window of size 400x300
window = pygame.display.set_mode((800, 800))
# setting the title of the window
pygame.display.set_caption("Image and random motion")
# setting the background color
bgcolor = (209, 207, 205)
figurecolor = (255, 0, 255)
posX1, posY1 = 100, 200
# uploading the image
image = pygame.image.load("images/LogoA.png")
while True:  # loop to keep the window open
    window.fill(bgcolor)  # filling the window with the background color
    window.blit(image, (posX1, posY1))  # blitting the image
    for i in range(20):
        posX, posY = randint(1, 800), randint(
            1, 800)  # generating random coordinates
        r, g, b = randint(0, 255), randint(
            0, 255), randint(0, 255)  # random color
        figurecolor = (r, g, b)  # setting the color
        pygame.draw.circle(window, figurecolor, (posX, posY),
                           randint(1, 100))  # drawing multiple circles
    for event in pygame.event.get():  # getting the events from the window
        if event.type == QUIT:  # if the event is a quit event
            pygame.quit()  # closing the window
            sys.exit()  # closing the program
        pygame.display.update()  # updating the window
