import pygame


class Missile(pygame.sprite.Sprite):
    """ creating class for the missile """

    def __init__(self, posX, posY):
        """ initializing """
        pygame.sprite.Sprite.__init__(self)
        self.imageMissile = pygame.image.load("Meteorites/images/misil.png")
        self.rect = self.imageMissile.get_rect()
        self.shootingspeed = 6
        self.rect.top = posY
        self.rect.left = posX

    def route(self):
        """ movement of the missile """
        self.rect.top = self.rect.top - self.shootingspeed

    def draw(self, surfice):
        """ drawing the missile """
        surfice.blit(self.imageMissile, self.rect)
