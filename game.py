import pygame, math
from player import Player
from asteroid import Asteroid


class Game:
    def __init__(self, screen):
        self.on = False
        self.screen = screen
        self.pressed = {}
        self.player = Player(self)
        self.asteroid = Asteroid()
        self.font = pygame.font.SysFont('monospace', 50)
        self.moy = False
        self.moy_list = []
        self.moy_result = 0

    def update(self):
        score_text = self.font.render(f'Distance : {self.get_distance_p_a()}', 1, (255, 255, 255))
        self.screen.blit(score_text, (20, 20))

        self.player.angle_()
        self.player.fix_coordinates()
        self.screen.blit(self.player.image, self.player.rect)
        self.screen.blit(self.asteroid.image, self.asteroid.rect)
        if self.moy:
            self.moy_list.append(self.get_distance_p_a())

    def get_distance_p_a(self):
        return math.sqrt(((self.asteroid.rect.centerx - self.player.real_center[0])**2) + ((self.asteroid.rect.centery - self.player.real_center[1])**2))

    def get_moy(self):
        if not self.moy:
            self.moy = True
        else:
            for i in self.moy_list:
                self.moy_result += i
            self.moy_result /= len(self.moy_list)
            print(self.moy_result)
            self.moy = False