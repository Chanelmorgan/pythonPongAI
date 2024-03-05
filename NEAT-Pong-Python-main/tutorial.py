import pygame
from pong import Game
import neat
import os
import pickle


class PongGame:
    def __init__(self, window, width, height):
        self.game = Game(window, width, height)
        self.left_paddle = self.game_left_paddle
        self.right_paddle = self.game_right_paddle
        self.ball = self.game.ball





# setting up the game
WIDTH, HEIGHT = 700, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))

game = Game(window, WIDTH, HEIGHT)
run = True
clock = pygame.time.Clock()
while run:
    clock.tick(60) # limits how fast the game goes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    # allows us to move the left paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        game.move_paddle(left=True, up=True)
    if keys[pygame.K_s]:
        game.move_paddle(left=True, up=False)

    game_info = game.loop()
    print(game_info.left_score, game_info.right_score)
    game.draw(False, True) # shows the combined hits
    pygame.display.update()

pygame.quit()
