import pygame
import sys
from pygame.locals import *
# importing modules to use in the program
from clases import player
from clases import asteroid
from random import randint
from time import time


# Variables
Width = 480
Height = 700
shootinglist = []
asteroidlist = []
points = 0
fontcolor = (120, 200, 40)
# Boolean to control the game loop
playing = True

# Asteroids


def chargeasteroids(x, y):
    meteoro = asteroid.Asteroid(x, y)
    asteroidlist.append(meteoro)

# Game over


def gameOver():
    global playing
    playing = False
    for asteroid in asteroidlist:
        asteroidlist.remove(asteroid)

# Principal Function


def meteorites():
    pygame.init()
    window = pygame.display.set_mode((Width, Height))  # creating a window
    # Background image
    background = pygame.image.load(
        "Meteorites/images/fondo.png")  # loading the image

    # Title
    pygame.display.set_caption("Meteorites")  # setting the title
    # creating object player
    nave = player.Nave()
    counter = 0

    # sounds
    pygame.mixer.music.load("Meteorites/sounds/meteoritos_sonidos_fondo.wav")
    pygame.mixer.music.play(3)
    collisionsound = pygame.mixer.Sound(
        "Meteorites/sounds/meteoritos_sonidos_colision.aiff")

    # Font marker
    fontmarker = pygame.font.SysFont("timesnewroman", 15)

    # Game loop
    while True:

        window.blit(background, (0, 0))  # blitting the image
        nave.draw(window)  # drawing the player

        # Time
        timee = time()

        # points
        global points
        textmarker = fontmarker.render("Points: " + str(points), 0, fontcolor)
        window.blit(textmarker, (0, 0))

        # creating asteroids
        if timee - counter > 1:
            counter = timee
            posX = randint(0, 478)
            chargeasteroids(posX, 0)

        # checking asteroidlist
        if len(asteroidlist) > 0:
            for asteroid in asteroidlist:
                if playing == True:
                    asteroid.draw(window)
                    asteroid.route()
                if asteroid.rect.top > Height:
                    asteroidlist.remove(asteroid)
                else:
                    if asteroid.rect.colliderect(nave.rect):
                        asteroidlist.remove(asteroid)
                        collisionsound.play()
                        nave.life = False
                        gameOver()

        # missile shooting
        if len(nave.shootinglist) > 0:  # if the list is not empty
            for missile in nave.shootinglist:  # for each missile in the list
                missile.draw(window)
                missile.route()
                if missile.rect.top > 700:  # if the missile is out of the screen
                    shootinglist.remove(missile)
                else:
                    for asteroid in asteroidlist:
                        if missile.rect.colliderect(asteroid.rect):
                            nave.shootinglist.remove(missile)
                            points += 1
                            asteroidlist.remove(asteroid)

        nave.movement()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if playing == True:
                    if event.key == pygame.K_LEFT:
                        nave.rect.left -= nave.velocity
                    elif event.key == pygame.K_RIGHT:
                        nave.rect.right += nave.velocity
                    elif event.key == pygame.K_SPACE:
                        x, y = nave.rect.centerx, nave.rect.centery
                        nave.shooting(x, y)

        if playing == False:
            fontGO = pygame.font.SysFont("timesnewroman", 50)
            textGO = fontGO.render("Game Over", 0, (fontcolor))
            window.blit(textGO, (130, 300))
            pygame.mixer.music.fadeout(3000)
        pygame.display.update()


# Calling the function
meteorites()
