import math
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.origin_image = pygame.image.load("assets/player.png")
        self.origin_image = pygame.transform.scale(self.origin_image, (60, 80))
        self.image = self.origin_image
        self.rect = self.image.get_rect()
        self.rect.center = (500, 390)
        self.real_center = [500, 390]

        self.angle = None
        self.relative_left = [-1, 0]
        self.relative_right = [1, 0]
        self.relative_up = [0, -1]
        self.relative_down = [0, 1]


    def gravity(self):
        self.angle = math.degrees(math.atan2(- self.rect.centery + self.game.asteroid.rect.centery,
                                             self.rect.centerx - self.game.asteroid.rect.centerx)) - 90
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

        self.relative_up = pygame.Vector2(self.real_center[0] - self.game.asteroid.rect.centerx,
                                          self.real_center[1] - self.game.asteroid.rect.centery).normalize()

        self.relative_down = pygame.Vector2(self.game.asteroid.rect.centerx - self.real_center[0],
                                            self.game.asteroid.rect.centery - self.real_center[1]).normalize()

        self.relative_right[0], self.relative_right[1] = self.relative_down[1], self.relative_down[0]

        self.relative_left[0], self.relative_left[1] = self.relative_up[1], self.relative_up[0]


    def move_left(self):
        self.real_center[0], self.real_center[1] = (self.real_center[0] + 10 * self.relative_left[0]), (
                    self.real_center[1] + 10 * self.relative_left[1])

    def move_right(self):
        self.real_center[0], self.real_center[1] = (self.real_center[0] + 10 * self.relative_right[0]), (
                    self.real_center[1] + 10 * self.relative_right[1])

    def move_down(self):
        self.real_center[0], self.real_center[1] = (self.real_center[0] + 10 * self.relative_down[0]), (
                    self.real_center[1] + 10 * self.relative_down[1])

    def move_up(self):
        self.real_center[0], self.real_center[1] = (self.real_center[0] + 10 * self.relative_up[0]), (
                    self.real_center[1] + 10 * self.relative_up[1])

    def fix_coordinates(self):
        self.rect.centerx, self.rect.centery = round(self.real_center[0]), round(self.real_center[1])
