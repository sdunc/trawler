import pygame as pg
from settings import *
from tmath import *



def rot_center(image, angle, x, y):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

    return rotated_image, new_rect

def blitRotateCenter(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect)


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = 2 # fg 
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.groups = game.all_sprites
        self.n_boat = pg.image.load('n_boat.png').convert_alpha()
        self.s_boat = pg.image.load('s_boat.png').convert_alpha()
        self.e_boat = pg.image.load('e_boat.png').convert_alpha()
        self.w_boat = pg.image.load('w_boat.png').convert_alpha()
        self.image = self.n_boat
        self.rect = self.image.get_rect(center=(x,y))
        self.rect = pg.Rect(self.rect.left/2, self.rect.top/2, \
                                self.rect.width/2, self.rect.height/2)

        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        # self.image = pg.Surface((TILESIZE, TILESIZE))
        # self.image.fill(WHITE)
        # self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0

        self.on_ocean = False

    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.image = self.w_boat
            self.vx = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.image = self.e_boat
            self.vx = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.image = self.n_boat
            self.vy = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.image = self.s_boat
            self.vy = PLAYER_SPEED
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071

    def collide_with_tiles(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.land, False)
            if hits:
                self.on_ocean = True
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.land, False)
            if hits:
                self.on_ocean = True
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y

    def update(self):
        self.get_keys()
        # TODO: turn sprite based on angle
        #print(self.vx,self.vy)
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collide_with_tiles('x')
        self.rect.y = self.y
        self.collide_with_tiles('y')

# class Wall(pg.sprite.Sprite):
#     def __init__(self, game, x, y):
#         self.groups = game.all_sprites, game.walls
#         pg.sprite.Sprite.__init__(self, self.groups)
#         self.game = game
#         self.image = pg.Surface((TILESIZE, TILESIZE))
#         self.image.fill(GREEN)
#         self.rect = self.image.get_rect()
#         self.x = x
#         self.y = y
#         self.rect.x = x * TILESIZE
#         self.rect.y = y * TILESIZE

class Ocean(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = 1 # bg 
        self.groups = game.all_sprites, game.ocean
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(OBLUE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Text(pg.sprite.Sprite):
    def __init__(self, game, x, y, txt):
        self._layer = 3
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        font = pg.font.SysFont(None, 24)
        img = font.render(txt, True, ORANGE_FONT)
        #self.image = pg.Surface((TILESIZE, TILESIZE))
        #self.image.fill(COLOR_DICT[val]) # lookup into dict for color see settings
        #self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        #self.rect.x = x * TILESIZE
        #self.rect.y = y * TILESIZE
        


class Land(pg.sprite.Sprite):
    def __init__(self, game, x, y, val=0):

        self._layer = 1 # bg 
        self.groups = game.all_sprites, game.land
        pg.sprite.Sprite.__init__(self, self.groups)

        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(COLOR_DICT[val]) # lookup into dict for color see settings
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        
