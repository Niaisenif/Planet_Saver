import pygame


class MenuLoader:
    def __init__(self):
        self.button_list = pygame.sprite.Group()
        self.menu_list = {"main": ((500, 500, "assets/button/", "4"),)}

    def load_menu(self, menu_type):
        pygame.sprite.Group()
        for button in self.menu_list[menu_type]:
            self.button_list.add(Button(button[0], button[1], button[2], button[3]))

    def update_all_buttons(self):
        for button in self.button_list:
            button.update_state()


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite_path, effect):
        super().__init__()
        self.sprite_path = sprite_path
        self.image = pygame.image.load(self.sprite_path + "normal.png")
        self.rect = self.image.get_rect()
        self.x, self.y = x, y
        self.rect.center = (self.x, self.y)
        self.effect = effect
        self.clicked = False
        self.click_timer = 0

    def update_state(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and not self.clicked:
            self.clicked = True
            self.click_timer = 11
            self.image = pygame.image.load(self.sprite_path + "clicked.png")
            self.rect = self.image.get_rect()
            self.rect.center = (self.x, self.y)
        if self.clicked:
            self.click_timer -= 1
            if self.click_timer <= 0:
                self.clicked = False
        else:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.image = pygame.image.load(self.sprite_path + "hover.png")
                self.rect = self.image.get_rect()
                self.rect.center = (self.x, self.y)
            else:
                self.image = pygame.image.load(self.sprite_path + "normal.png")
                self.rect = self.image.get_rect()
                self.rect.center = (self.x, self.y)
