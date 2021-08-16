import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
from noise import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()
        self.map_data = []

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        
        # then open it
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
           for line in f:
                self.map_data.append(line)


    def make_new_map(self):
        return  get_map() #generate a new map quick


        
    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.LayeredUpdates()
        #self.walls = pg.sprite.Group()
        self.ocean = pg.sprite.LayeredUpdates()
        self.land =  pg.sprite.LayeredUpdates()
        #pg.sprite.Group()
        
        names = self.make_new_map()
        #Text(self, names[1],names[2],names[0])
        self.load_data()
        # iterate over the index value
        # TODO stephen: have tiles go into a lookup table to make
        # quick n robust maps
        for i in range(len(self.map_data)):
            for j in range(len(self.map_data[0])):
                tile = self.map_data[i][j]
                if tile == "1":
                    Land(self, i, j, 1)
                elif tile == '2':
                    Land(self,i,j,2)
                elif tile =='3':
                    Land(self,i,j,3)
                elif tile == '4':
                    Land(self,i,j,4)
                elif tile == '5':
                    Land(self,i,j,5)
                elif tile == '6':
                    Land(self,i,j,6)
                elif tile == '7':
                    Land(self,i,j,7)
                elif tile == '8':
                    Land(self,i,j,8)
                #elif tile == '0':
                #    Ocean(self,i,j)
                elif tile == 'P':
                    self.player = Player(self, i,j)
        
    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        # displayed at the right z level.
        # TODO: Add z levels for real
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(OBLUE)
        #self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_F5:
                    self.new()# add code for examine function here

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
