from settings import *
import random

def random_nxn(n):
    noise_grid = []
    for rows in range(n):
        t = []
        for cols in range(n):
            t.append(random.randint(0,9)) # random 0,1,2,3,4,...,9
                     
        noise_grid.append(t)
    return noise_grid

#print(random_nxn(5))

def flip(p):
    return True if random.random() < p else False


def fill_bools(n,m,fill=FILL):
    # fill an nxn matrix will True and False
    # maintn close to fill as a ratio
    bools = []

    for rows in range(n):
        t = []
        for cols in range(m):
            t.append(flip(fill))
        bools.append(t)

    return bools


def count_neighbors_equal(neighbors,arr,val):
    total = 0
    for tindex in neighbors:
        if arr[tindex[0]][tindex[1]] == val:
            total +=1
    return total


def find_spawn(arr):
    # pass in a nearly finished map
    # edit the array so that an ideal location
    # has the 'P' for player spawn tile
    cmax = 0 # all land 8 squares
    # nxm n rows (y) and m cols (x)
    ci = 0
    cj = 0
    cmax = 0
    n = len(arr)-1
    m = len(arr[0])-1
    for i in range(n):
        for j in range(m):
            neighbors = moore_neighbors(i,j,n,m)
            T = count_neighbors_equal(neighbors,arr,0)
            print("T=",T, end=' ')
            if T == 8:
                arr[i][j] = 'P' # place the player into the map
                return arr
            elif T > cmax:
                ci = i
                cj = j
                cmin = T
            else:
                pass # not all water or less than current min
        print('\n')
    arr[ci][cj] = 'P' # place the player into the map
    return arr

def raw_map(boolarr):
    # takes an array of booleans and defines them and 0 water if true
    # or a random int between [1,9] otherwise this will then be
    # discretely averaged to make the terrain look nice
    # make a map without a player P on it
    map = []
    for row in boolarr:
        t = []
        for col_e in row:
            if not col_e:
                t.append(0)
            else:
                t.append(random.randint(0,9)) # random land value
        map.append(t)
    return map

def write_map(arr, mapname="map.txt"):
    # write the contents of an array out to a text file to be used as
    # a map
    Map = open(mapname,'w') # write to map.txt

    for row in arr:
        for cole in row:
            Map.write(str(cole))
        Map.write('\n')

    Map.close()
    
def get_map(mapname='map.txt',n=GRIDWIDTH,m=GRIDHEIGHT):
    # returns an nxm map and saves to mapname
    # get the random array nxm
    boolarr = fill_bools(n,m)
    # do ca_johnson cellular automota rules to generate a cavelike thing
    # tweak this until we have something that looks more like islands.
    grid = ca_johnson(boolarr,steps=STEPS)
    randmap = raw_map(grid)
    # use discrete avg to smooth out terrain
    for step in range(STEPS2):
        randmap = moore_neighbor_avg(randmap)
    map = find_spawn(randmap)
    write_map(map)

    name_str = "Karamja"
    for i in range(n):
        for j in range(m):
            neighbors = moore_neighbors(i,j,n-1,m-1)
            T = count_neighbors_equal(neighbors,map,0)
            if T == 0:
                return (name_str, i*TILESIZE, j*TILESIZE)
            else:
                pass # not all water or less than current min
    return ("", i,j) # no name

    return names

def moore_neighbor_avg(arr):
    # avg integer values of moore neigbors of
    # arr[i][j]
    # first try without doing in place or making a mask array 
    n = len(arr)-1
    m = len(arr[0])-1
    for i in range(n):
        for j in range(m):
            neighbors = moore_neighbors(i,j,n,m)
            nsum = 0
            no_neighbors = len(neighbors)

            for nindex in neighbors:
                nsum+=int(arr[nindex[0]][nindex[1]])

            navg = int(nsum/no_neighbors)
            # now we avg our current cell with this axvg and make sure it is
            # withtin the range 0-9 we are working in
            new_val = (int(arr[i][j])+navg)//2
            if new_val > 9:
                arr[i][j] = 9
            elif new_val < 0:
                arr[i][j] = 0
            else:
                arr[i][j] = new_val # legal val

    return arr # after 1 iteration


def moore_neighbors(i,j,n,m):
    # instead x2, try each and return array of 2tuples
    # of legal neighbors
    # in an nxm matrix
    # n rows x m cols
    #print(n,m)


    # start with the array fully populated and remove those that are
    # found to not be valid so:
    neighbors = [(i-1,j-1),(i-1,j+0),(i-1,j+1),\
                 (i+0,j-1),(i+0,j+1),\
                 (i+1,j-1),(i+1,j+0),(i+1,j+1)]


    a_ns = [] # adjusted neighbors

    for neighbor in neighbors:
        if neighbor[0] < 0:
            n_y = n
        elif neighbor[0] > n: # off to bottom
            n_y = 0
        else:
            n_y = neighbor[0]
        
        if neighbor[1] < 0: # off left
            n_x = m
        elif neighbor[1] > m: # greater than number of columns maybe greater
            n_x = 0
        else:
            n_x = neighbor[1]

        
        a_ns.append((n_y,n_x))
    return a_ns


def count_neighbors(neighbors, grid):
    # count all nearby trues
    acc = 0
    for n in neighbors:
        if grid[n[0]][n[1]]:
            acc+=1
    return acc

def ca_johnson(grid,steps=STEPS):
    # nxn grid and ruleset which gets applied iteratively
    # moore_neighbors (8 surrounding) need to get from indices
    # of an nxm grid
    # requires that every entry have the same number of cols
    n = len(grid)-1
    m = len(grid[0])-1
    for step in range(steps):

        for row in range(n):
            for col in range(m):
                neighbors = moore_neighbors(row,col,n,m)
                T = count_neighbors(neighbors, grid)
                if T > 4:
                    grid[row][col] = True
                elif T == 4:
                    pass # C = C
                else:
                    grid[row][col] = False # cell dies
    return grid
def normalize_2d(arr):
    # normalize a 2d array
    current_max = arr[1][1]
    current_min = arr[1][1]
    # return all values 0-9
    for row in arr:
        for element in row:
            if not isinstance(element, str):
                if element > current_max:
                    current_max = element
                elif element < current_min:
                    current_min = element
                else:
                    pass # not larger or smaller
    # we have a max and min
    newarr = []
    t = []
    for row in arr:
        for element in row:
            if isinstance(element, str):
                # if its a string
                # add it to new arr
                t.append(element)
            else:
                t.append(scale(element, current_max, current_min))
        newarr.append(t)
        t = [] # new row
        
    game_folder = path.dirname(__file__)
    maptxt = open(path.join(game_folder, 'map.txt'), 'w')
    for row in arr:
        for element in row:
            maptxt.write(str(element))
        maptxt.write('\n')
    
        
def scale(x, imax, imin):
    # val between 0,1
    first_scale = (x-imin)/(imax-imin)
    # val in 0,...,9 bin
    return int(str(first_scale*100)[0])-1

def abs(x):
    if x<0:
        return x*-1
    else:
        return x

