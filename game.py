import pygame, math
from player import Player
from asteroid import Asteroid


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.pressed = {}
        self.player = Player(self)
        self.asteroid = Asteroid()
        print(math.sqrt((self.asteroid.rect.centerx + self.player.rect.centerx)**2 + (self.asteroid.rect.centery + self.player.rect.centery)**2))

    def update(self):
        self.player.gravity()
        self.player.fix_coordinates()
        self.screen.blit(self.player.image, self.player.rect)
        self.screen.blit(self.asteroid.image, self.asteroid.rect)

    def distance_p_a(self):
        return math.sqrt((self.asteroid.rect.centerx + self.player.rect.centerx)**2 + (self.asteroid.rect.centery + self.player.rect.centery)**2)
