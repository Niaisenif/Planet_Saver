import pygame
from game import Game
from menus import MenuLoader
pygame.init()

screen = pygame.display.set_mode((1000, 1000))

clock = pygame.time.Clock()
FPS = 60
game = Game(screen)
ML = MenuLoader()
ML.load_menu("main")

running = True
while running:
    screen.fill((0, 0, 0))
    if game.on:
        if game.pressed.get(pygame.K_d):
            game.player.move_right()

        elif game.pressed.get(pygame.K_q):
            game.player.move_left()

        elif game.pressed.get(pygame.K_s):
            game.player.move_down()

        elif game.pressed.get(pygame.K_z):
            game.player.move_up()

        game.update()

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.get_moy()
                else:
                    game.pressed[event.key] = True

            if event.type == pygame.KEYUP:
                game.pressed[event.key] = False

    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
            pygame.quit()

    ML.button_list.draw(screen)
    ML.update_all_buttons()

    pygame.display.flip()
    clock.tick(FPS)
