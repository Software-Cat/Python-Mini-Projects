import random

def best_spot(grid, *args):
    emptySpots = []
    for x in range(3):
        for y in range(3):
            if grid[x][y] == '':
                emptySpots.append([x, y])
    
    return random.choice(emptySpots)