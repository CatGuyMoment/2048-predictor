import math
import numpy as np
from itertools import permutations 
#prediction 101:

#every move, this runs 8 times:

    #select a random available square

    #raycast on the x axis to the left
        #when something is found, it has an 80% chance of being picked AND it's smaller than something already raycasted, otherwise it's discarded

    #raycast on the y axis up
        #when something is found, it has an 80% chance of being picked AND it's smaller than something already raycasted, otherwise it's discarded


#probabilities for 1 run on 1 random square (which has to iterate 8 times)
    #for raycast x and raycast y:

    #if x = y or x < y, 
        #p(x) = 16.59%
        #p(y) = 79%
        #p(previous_selection) = 4.41%

    #if x > y, 
        #p(x) = 16.59%
        #p(y) = 79%
        #p(previous_selection) = 4.41%

    #if one of the raycasts fails

        #if previous_selection = successful_raycast or previous selection < successful raycast,
            #p(previous) = 100%

        #if previous_selection > successful_raycast,
            #p(successful) = 79%
            #p(previous) = 21%

    #if both raycasts fail,
        #p(previous) = 100%
MAX_NUMBER = 29

class grid:
    def __init__(self,size):
        self.lines_yx = [line() for _ in range(size)]
        self.lines_xy = [line() for _ in range(size)]
        for x in range(size):
            for y in range(size):
                line_x = self.lines_yx[y]
                line_y = self.lines_xy[x]
                new_tile = tile(line_x,line_y,x,y)

                line_x.append_tile(new_tile)
                line_y.append_tile(new_tile)

    def get_available_cells(self):
        pass
    def get_random_available_cell(self):
        pass

class line:
    def __init__(self):
        self.tiles = []
    def append_tile(self,new_tile):
        self.tiles.append(new_tile)

class tile:
    def __init__(self,line_x,line_y,pos_x,pos_y):
        self.value = 1 #1 = available
        self.parents = [line_x,line_y]
        self.position = [pos_x,pos_y]

    def update_availability(self):
        self.available = self.value == 1

    def update_value(self,newvalue):
        self.value = newvalue
        self.update_availability()

    def raycast(self):#gonna hardcode this to only work in +x and +y cuz thats how its done officially for some reason??
        pass #returns a CELL.






def run(grid,rv_list ): ##rv_list: first 3 reserved for raycasts and random cells, all others reserved for check_cell
    backup_cell = grid.get_random_available_cell(rv_list[0])

    value = MAX_NUMBER
    position = backup_cell.position.copy() #avoids reference nonesense

    for index in range(8):
        check_cell = grid.get_random_available_cell(rv_list[index+3])

        raycast_x, raycast_y = check_cell.raycast()

        if raycast_x and check_cell.value < value and rv_list[1] < 0.8:
            position = check_cell.position.copy()
            value = raycast_x.value
        
        if raycast_y and check_cell.value < value and rv_list[2] < 0.8:
            position = check_cell.position.copy()
            value = raycast_y.value
    

def assemble_list(size,values,dimensions):
    if dimensions == 0:
        return values
    return [assemble_list(size,values,dimensions-1) for _ in range(size)]

def get_linspace_size(decimal_places):
    return 10**decimal_places + 1

def create_linspace(linspace_size):
    return np.linspace(0,1,linspace_size)

def main(rv_decimal_places):
    rv_list_size = 8
    linspace_size = get_linspace_size(rv_decimal_places)
    linspace = create_linspace(linspace_size)

    state_i = [0 for _ in range(rv_list_size)]
    state_v = [0 for _ in range(rv_list_size)]

    results = []
    while state_i[-1] < rv_decimal_places:
        state_i[0] += 1
        for index in range(rv_list_size):
            if state_i[index] >= rv_decimal_places and index < rv_list_size - 1:
                state_i[index] = 0
                state_i[index+1] += 1
            state_v = linspace[state_i]
            results.append(state_v)
            # print(state_v)
    print(len(results))


run(grid(3) 3)    

