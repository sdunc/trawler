from os import path

# Map generation using CA + Averaging
# Good settings? 3:2 w/ 0.53 fill
STEPS = 3
STEPS2 = 2
FILL = 0.53 # % of map to fill with water.

# Map generation using Perlin noise
OCTAVES = 1
FREQ = 16 * OCTAVES

WATER_FILL = 0.6
SAND_LEVEL = 0.7
L2 = .75
L3 = .78
L4 = .81
L5 = .84
L6 = .87
L7 = .9
L8 = .95

# Colors (r,g,b)
WHITE = (255, 255, 255) 
ORANGE_FONT = (253,169,41) # text has a se 1px black border
BLACK = (255,255,255)

SHALLOW = (148,160,185)#94A0B9

# Island colors to be indexed into
OBLUE = (87, 106, 146)     #576a92 0
SAND = (186,167,87)        #baa757 1
GRASSBEACH = (182,171,65)  #b6ab41 2 
OLIVE = (150,157,56)       #969d38 3
LIGHTFOREST = (100,132,33) #648421 4
DARKFOREST = (91,121,30)   #5B791E 5
JGREEN = (90,96,14)        #5a600e 6
LIGHTBROWN =  (93,56,5)    #5d3805 7
DARKBROWN = (62,43,21)     #3e2b15 8
MT_BLACK = (25,20,17)      #191411 9

COLOR_DICT = {0: OBLUE,
              1: SAND, 
              2: GRASSBEACH,
              3: OLIVE,
              4: LIGHTFOREST,
              5: DARKFOREST,
              6: JGREEN,
              7: LIGHTBROWN,
              8: DARKBROWN,
              9: MT_BLACK}

              
# Game Settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  #32*16  # 16 * 48 or 32 * 24 or 64 * 12

FPS = 60
TITLE = "Trawler"
BGCOLOR = OBLUE

TILESIZE = 16
GRIDWIDTH = 256 # int(WIDTH / TILESIZE) 
GRIDHEIGHT = 256
#int(HEIGHT / TILESIZE)

# Player settings
PLAYER_SPEED = 250
KEY_DELAY = 500
KEY_REPEAT_DELAY = 100
