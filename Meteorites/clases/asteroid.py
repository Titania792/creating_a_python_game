import pygame


class Asteroid(pygame.sprite.Sprite):
    """ create class for the asteroid """

    def __init__(self, posX, posY):
        """ initializing """
        pygame.sprite.Sprite.__init__(self)
        self.imageAsteroid = pygame.image.load(
            "Meteorites/images/asteroide.png")
        self.rect = self.imageAsteroid.get_rect()
        self.asteroidspeed = 1
        self.rect.top = posY
        self.rect.left = posX
        self.asteroidlist = []

    def route(self):
        """ movement of the asteroid """
        self.rect.top = self.rect.top + self.asteroidspeed

    def draw(self, surfice):
        """ drawing the asteroid """
        surfice.blit(self.imageAsteroid, self.rect)
