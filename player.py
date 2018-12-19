import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((GRID_SIZE, GRID_SIZE))
        self.image.fill(C_GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
    def move(self, dx = 0, dy = 0):
        self.x += dx
        self.y += dy
        print(self.x, ' ', self.y)
    def update(self):
        self.rect.x = self.x * GRID_SIZE
        self.rect.y = self.y * GRID_SIZE
