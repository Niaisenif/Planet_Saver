import pygame


class MenuLoader:
    def __init__(self):
        self.button_list = pygame.sprite.Group()
        self.menu_list = {"main": ((500, 500, "assets/button.png", "4"),)}

    def load_menu(self, menu_type):
        pygame.sprite.Group()
        for button in self.menu_list[menu_type]:
            self.button_list.add(Button(button[0], button[1], button[2], button[3]))


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite_path, effect):
        super().__init__()
        self.image = pygame.image.load(sprite_path)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.effect = effect
