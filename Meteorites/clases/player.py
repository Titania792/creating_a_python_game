import pygame
from clases import shoot


class Nave(pygame.sprite.Sprite):
    """ creating class for the player """

    def __init__(self):
        """ initializing """
        pygame.sprite.Sprite.__init__(
            self)  # calling the parent class constructor
        self.imageNave = pygame.image.load(
            "Meteorites/images/nave.png")  # loading the image
        self.imageexplode = pygame.image.load(
            "Meteorites/images/naveExplota.png")  # loading the image
        self.rect = self.imageNave.get_rect()  # getting the rectangle of the image
        # Initial position
        self.rect.centerx = 240
        self.rect.centery = 690
        self.velocity = 10
        self.life = True
        self.shootinglist = []
        self.shootsound = pygame.mixer.Sound(
            "Meteorites/sounds/meteoritos_sonidos_disparo.aiff")

    def movement(self):
        """ movement of the nave """
        if self.life == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right >= 490:
                self.rect.right = 490

    def shooting(self, x, y):
        """ shooting"""
        if self.life == True:
            missile = shoot.Missile(x, y)
            self.shootinglist.append(missile)
            self.shootsound.play()

    def draw(self, surfice):
        if self.life == True:
            surfice.blit(self.imageNave, self.rect)
        else:
            surfice.blit(self.imageexplode, self.rect)
        surfice.blit(self.imageNave, self.rect)
