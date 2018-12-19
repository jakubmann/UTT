import pygame as pg
from settings import *
from player import *
from wall import *

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('Up The Tower')
        pg.display.set_icon(LOGO)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(250, 100)
        self.running = True

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.player = Player(self, 1, 1)
        for x in range(0, GRID_SIZE):
            Wall(self, x, 0)
            Wall(self, x, 15)
        for y in range(0, GRID_SIZE):
            Wall(self, 0, y)
            Wall(self, 15, y)
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, GRID_SIZE):
            pg.draw.line(self.screen, C_BLACK, (x, 0), (x, WIDTH))
        for y in range(0, HEIGHT, GRID_SIZE):
            pg.draw.line(self.screen, C_BLACK, (0, y), (WIDTH, y))

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                key = event.key
                if key == pg.K_UP:
                    self.player.move(dy = -1)
                elif key == pg.K_DOWN:
                    self.player.move(dy = 1)
                elif key == pg.K_LEFT:
                    self.player.move(dx = -1)
                elif key == pg.K_RIGHT:
                    self.player.move(dx = 1)

    def draw(self):
        self.screen.fill(C_WHITE)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass
