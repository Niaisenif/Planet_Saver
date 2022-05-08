import pygame


class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("assets/asteroid.png"), (140, 140))
        self.rect = self.image.get_rect()
        self.rect.center = (500, 500)
