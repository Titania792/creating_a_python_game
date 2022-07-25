from turtle import circle
import pygame
import sys  # importing modules to use in the program
from pygame.locals import *

pygame.init()  # initializing pygame

# creating a window of size 800x800
window = pygame.display.set_mode((800, 800))  # (width, height)
# setting the title of the window
pygame.display.set_caption("Creating different figures")

# setting the background color
bgcolor = (191, 191, 191)
linecolor = (72, 129, 219)
circlecolor = (232, 46, 142)
figurecolor = (180, 104, 227)

# loop to keep the window open
while True:
    window.fill(bgcolor)  # filling the window with the background color

    # Lines
    pygame.draw.line(window, linecolor, (10, 100),
                     (100, 100), 40)  # (window, color, start, end, width)
    pygame.draw.line(window, linecolor, (100, 200),
                     (300, 200), 20)
    pygame.draw.line(window, linecolor, (400, 450),
                     (100, 700), 50)
    pygame.draw.line(window, linecolor, (700, 50),
                     (400, 350), 50)

    # Circles
    pygame.draw.circle(window, circlecolor, (350, 250),
                       65, 0)  # (x, y, radius, width)
    pygame.draw.circle(window, circlecolor, (500, 600),
                       5, 10)  # (x, y, radius, width)
    pygame.draw.circle(window, circlecolor, (500, 600),
                       20, 10)  # (x, y, radius, width)
    pygame.draw.circle(window, circlecolor, (500, 600),
                       35, 10)  # (x, y, radius, width)
    pygame.draw.circle(window, circlecolor, (500, 600),
                       50, 10)  # (x, y, radius, width)
    pygame.draw.circle(window, circlecolor, (500, 600),
                       65, 10)  # (x, y, radius, width)
    pygame.draw.circle(window, circlecolor, (500, 600),
                       80, 10)  # (x, y, radius, width)

    # Figures

    pygame.draw.rect(window, figurecolor, (100, 300, 100, 100))
    # (window, color, (x, y, width, height))
    pygame.draw.rect(window, figurecolor, (600, 450, 100, 300))
    pygame.draw.rect(window, figurecolor, (200, 650, 200, 100))

    pygame.draw.polygon(window, figurecolor, ((
        400, 400), (500, 400), (550, 500), (490, 500)))  # (window, color, points)
    pygame.draw.polygon(window, figurecolor, ((
        50, 20), (150, 20), (250, 100), (190, 190)))
    pygame.draw.polygon(window, figurecolor, ((
        300, 60), (380, 10), (560, 90), (490, 160), (360, 170)))

    for event in pygame.event.get():  # getting the events from the window
        if event.type == QUIT:  # if the event is a quit event
            pygame.quit()  # closing the window
            sys.exit()  # closing the program
        pygame.display.update()  # updating the window
