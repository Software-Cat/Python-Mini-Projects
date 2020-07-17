import random

def best_spot(grid, playerTurn, computerTurn):
    emptySpots = []
    for x in range(3):
        for y in range(3):
            if grid[x][y] == '':
                emptySpots.append([x, y])
    
    if [0, 0] in emptySpots:
        if grid[1][0] == playerTurn and grid[2][0] == playerTurn:
            return [0, 0]
        elif grid[1][1] == playerTurn and grid[2][2] == playerTurn:
            return [0, 0]
        elif grid[0][1] == playerTurn and grid[0][2] == playerTurn:
            return [0, 0]
    if [1, 0] in emptySpots:
        if grid[0][0] == playerTurn and grid[2][0] == playerTurn:
            return [1, 0]
        elif grid[1][1] == playerTurn and grid[1][2] == playerTurn:
            return [1, 0]
    if [2, 0] in emptySpots:
        if grid[0][0] == playerTurn and grid[1][0] == playerTurn:
            return [2, 0]
        elif grid[1][1] == playerTurn and grid[0][2] == playerTurn:
            return [2, 0]
        elif grid[2][1] == playerTurn and grid[2][2] == playerTurn:
            return [2, 0]
    if [0, 1] in emptySpots:
        if grid[0][0] == playerTurn and grid[0][2] == playerTurn:
            return [0, 1]
        elif grid[1][1] == playerTurn and grid[2][1] == playerTurn:
            return [0, 1]
    if [1, 1] in emptySpots:
        if grid[0][1] == playerTurn and grid[2][1] == playerTurn:
            return [1, 1]
        elif grid[1][0] == playerTurn and grid[1][2] == playerTurn:
            return [1, 1]
        elif grid[2][0] == playerTurn and grid[0][2] == playerTurn:
            return [1, 1]
        elif grid [0][0] == playerTurn and grid[2][2] == playerTurn:
            return [1, 1]
    if [2, 1] in emptySpots:
        if grid[2][0] == playerTurn and grid[2][2] == playerTurn:
            return [2, 1]
        elif grid[0][1] == playerTurn and grid[1][1] == playerTurn:
            return [2, 1]
    if [0, 2] in emptySpots:
        if grid[0][0] == playerTurn and grid[0][1] == playerTurn:
            return [0, 2]
        elif grid[1][1] == playerTurn and grid[2][0] == playerTurn:
            return [0, 2]
        elif grid[1][2] == playerTurn and grid[2][2] == playerTurn:
            return [0, 2]
    if [1, 2] in emptySpots:
        if grid[0][2] == playerTurn and grid[2][2] == playerTurn:
            return [1, 2]
        elif grid[1][1] == playerTurn and grid[1][0] == playerTurn:
            return [1, 2]
    if [2, 2] in emptySpots:
        if grid[0][2] == playerTurn and grid[1][2] == playerTurn:
            return [2, 2]
        elif grid[1][1] == playerTurn and grid[0][0] == playerTurn:
            return [2, 2]
        elif grid[2][1] == playerTurn and grid[2][0] == playerTurn:
            return [2, 2]

    return(random.choice(emptySpots))
    
    print('WHAT!')
