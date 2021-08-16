

from os import path# define some colors (R, G, B)
STEPS = 3
STEPS2 = 2
FILL = 0.53# water fill or


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# colors increasing from 0 ->
OBLUE = (87, 106, 146)
SAND = (182,162,91)
BEACH1 = (172,169,70)
LIGHTGREEN = (144,161,52)
GREEN = (81,120,29)
DARKGREEN = (62,102,23)
MUDDY = (97,82,16)
VOLCANO_BOTTOM = (82,49,13)
PEAKS = (39,31,20)
MT_TOP = (12,12,10) # top of karamja volcano


ORANGE_FONT = (253,169,41)
# with a black outline 1 px -> and down

# define a dictionary to hold our colors depending on the perlin noise value
COLOR_DICT = {0: OBLUE,
              1: SAND, 
              2: BEACH1,
              3: LIGHTGREEN,
              4: GREEN,
              5: DARKGREEN,
              6: MUDDY,
              7: VOLCANO_BOTTOM,
              8: PEAKS,
              9: MT_TOP}
              

# game settings
WIDTH = 800   # 16 * 64 or 32 * 32 or 64 * 16
# WIDTH is x and [WIDTH][HEIGHT]
HEIGHT = 600#32*16  # 16 * 48 or 32 * 24 or 64 * 12



FPS = 60
TITLE = "Trawler"
BGCOLOR = OBLUE

TILESIZE = 16
GRIDWIDTH = int(WIDTH / TILESIZE) 
GRIDHEIGHT = int(HEIGHT / TILESIZE)

# Player settings
PLAYER_SPEED = 200


