import pygame as pg
from settings import *

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x , y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((GRID_SIZE, GRID_SIZE))
        self.image.fill(C_BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * GRID_SIZE
        self.rect.y = y * GRID_SIZE
