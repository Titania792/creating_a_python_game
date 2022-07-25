import pygame
import sys  # importing modules to use in the program
from pygame.locals import *

pygame.init()  # initializing pygame

# creating a window of size 400x300
window = pygame.display.set_mode((400, 300))
# setting the title of the window
pygame.display.set_caption("Titulo de la ventana")
# setting the background color
bgcolor = (1, 150, 70)
while True:  # loop to keep the window open
    window.fill(bgcolor)  # filling the window with the background color
    for event in pygame.event.get():  # getting the events from the window
        if event.type == QUIT:  # if the event is a quit event
            pygame.quit()  # closing the window
            sys.exit()  # closing the program
        pygame.display.update()  # updating the window
