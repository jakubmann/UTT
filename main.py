import pygame as pg
from game import *
from player import *

game = Game()

while game.running:
    game.new()
pg.quit()
