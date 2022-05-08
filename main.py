import pygame
from game import Game
pygame.init()

screen = pygame.display.set_mode((1000, 1000))
pygame.display.init()

clock = pygame.time.Clock()
FPS = 60
game = Game(screen)
running = True

while running:
    screen.fill((0, 0, 0))
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
            game.pressed[event.key] = True

        if event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        if event.type == pygame.QUIT:
            running = False
            pygame.quit

    pygame.display.flip()
    clock.tick(FPS)
