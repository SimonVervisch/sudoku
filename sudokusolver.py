import numpy as np

#def init_unassigned(grid):
#    for i in range(9):
#        for j in range(9):
#            if grid[i][j] == 0:
#                grid[i][j] = 10
#    return grid



# returns false if no double has been found
def check_square_doubles(grid,x,y):
    array_true = np.full((9,), False)
    for i in range(3):
        for j in range(3):
            if array_true[grid[x+i,y+j]]:
                return True
            array_true[grid[x+i,y+j]] = True

    return False

def check_row_doubles(grid,row):
    array_true = np.full((9,), False)
    for i in range(9):
        if array_true[grid[row,i]]:
            return True
        array_true[grid[row,i]] = True
    return False



# checks whether current grid has no constraints
def valid_grid(grid):
    found_double = False

    for i in range(3):
        for j in range(3):
            if check_square_doubles(grid, i * 3, j*3):
                return False

    for row in range(9):
        if check_row_doubles(grid, row):
            return False

def fill_grid(grid):
    last_filled = False
    array_unit_cells = find_unitialised_cells(grid) # these are the variables in CSP, domain is from 1-9
    
    while not last_filled:
        grid = fill_grid_once(grid,array_unit_cells) 
        if valid_grid(grid,array_unit_cells):
            return grid
        last_filled = is_last_fill(grid,array_unit_cells) 

    print("could not be filled")
    return False
        


def is_last_fill(grid,unit_cells):
    return not grid[unit_cells[0]] 





def find_unitialised_cells(grid):
    lst = []
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                lst.append([i, j])


    return lst

def extract_grid_el(grid,unit_cells,element_number):
    x_coordinate = unit_cells[element_number][0]
    y_coordinate = unit_cells[element_number][1]
    return grid[x_coordinate][y_coordinate]



def fill_grid_once(grid, unit_cells):

    current = 0
    while current < len(unit_cells):
        if grid[unit_cells[current]] in range(10): # even 0 will be included
            grid[unit_cells[current]] += 1
            return grid
        elif current == len(unit_cells):
            grid[unit_cells[0]] = False # First unit element false -> last element
            return grid
        else:
            current = len(unit_cells)

        current += 1


def init_unassigned(grid):
    list = []




#def increase_current(x,y,grid):





def naive_solver(grid):
    
    return valid_grid(grid)

grid = np.full((9, 9), 0)
grid = grid.copy()

print(naive_solver(np.full((9, 9), 0)))


