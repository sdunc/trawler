import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
#from noise import *
from mapgen import *
from tilemap import *

class Game:
    def __init__(self):
        # create the pygame game object with constants defined in
        # settings.py
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        # n_boat = pg.image.load('n_boat.png').convert_alpha()
        # s_boat = pg.image.load('s_boat.png').convert_alpha()
        # e_boat = pg.image.load('e_boat.png').convert_alpha()
        # w_boat = pg.image.load('w_boat.png').convert_alpha()
        self.clock = pg.time.Clock()
        pg.key.set_repeat(KEY_DELAY, KEY_REPEAT_DELAY)
        self.make_new_map()
        self.load_data() # load map.txt into self.map_data

    def load_data(self):
        # create a new map object
        game_folder = path.dirname(__file__)
        self.map = Map(path.join(game_folder, 'map.txt'))
        
    def make_new_map(self):
        # generate a new map
        #return  get_map() #generate a new map quick
        #get_pmap()
        get_map()

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
        for i in range(self.map.tileheight):
            for j in range(self.map.tilewidth):
                tile = self.map.data[i][j]
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
                elif tile == '9':
                    Land(self,i,j,9)
                elif tile == 'P':
                    self.player = Player(self, i,j)

            self.camera = Camera(self.map.width, self.map.height)

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
        self.camera.update(self.player)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

            
    def draw(self):
        self.screen.fill(OBLUE)
        #self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
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
