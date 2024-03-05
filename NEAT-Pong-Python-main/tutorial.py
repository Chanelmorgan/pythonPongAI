import pygame
from pong import Game
import neat
import os
import pickle

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
    game.loop()
    game.draw()
    pygame.display.update()

pygame.quit()
