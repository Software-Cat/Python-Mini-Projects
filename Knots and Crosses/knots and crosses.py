import tkinter as tk

AIName = input('Enter your ai: ')
AI = __import__(AIName)

root = tk.Tk()
running = True

buttonGrid = [
    [object, object, object],
    [object, object, object],
    [object, object, object]
]
grid = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

BUTTON_CONFIG = {
    'master': root,
    'text': '',
    'width': 13,
    'height': 5
}

turn = 'O'
playerTurn = 'O'
computerTurn = 'X'
faces = [playerTurn, computerTurn]

def make_buttons():
    for x in range(3):
        for y in range(3):
            b = tk.Button(**BUTTON_CONFIG)
            b['command'] = lambda button=b, x=x, y=y: button_callback_player(button, x, y)
            b.grid(column=x, row=y)
            buttonGrid[x][y] = b

def switch_turn():
    global turn
    if turn == 'O':
        turn = 'X'
    else:
        turn = 'O'

def declare_win(face):
    # Clear Button Commands
    for column in buttonGrid:
        for button in column:
            button['command'] = lambda : None
    
    # Disable Turn and running
    global turn
    turn = ''
    global running
    running = False

    # Win Message
    if face == 'O':
        text = tk.Entry(root, justify='center', width=40)
        text.insert(tk.END, 'Knots Win!')
        text.grid(row=3, columnspan=3)
    else:
        text = tk.Entry(root, justify='center', width=40)
        text.insert(tk.END, 'Crosses Win!')
        text.grid(row=3, columnspan=3)

def declare_draw():
    # Clear Button Commands
    for column in buttonGrid:
        for button in column:
            button['command'] = lambda : None
    
    # Disable Turn and running
    global turn
    turn = ''
    global running
    running = False

    # Win Message
    text = tk.Entry(root, justify='center', width=40)
    text.insert(tk.END, "It's a Draw!")
    text.grid(row=3, columnspan=3)


def button_callback_player(self, x, y):
    if grid[x][y] == '' and turn == playerTurn:
        grid[x][y] = turn
        self['text'] = turn
        if detect_win():
            declare_win(turn)
        switch_turn()

def button_callback_computer(x, y):
    if grid[x][y] == '' and turn == computerTurn:
        grid[x][y] = turn
        buttonGrid[x][y]['text'] = turn
        if detect_win():
            declare_win(turn)
        switch_turn()

def detect_win():
    # Horizontal Wins
    for y in range(2):
        for face in faces:
            if grid[y][0] == face and grid[y][1] == face and grid[y][2] == face:
                return face
    
    # Vertical Wins
    for x in range(2):
        for face in faces:
            if grid[0][x] == face and grid[1][x] == face and grid[2][x] == face:
                return face
    
    # Diagonal Wins
    for face in faces:
        if grid[0][0] == face and grid[1][1] == face and grid[2][2] == face:
            return face
        elif grid[2][0] == face and grid[1][1] == face and grid[0][2] == face:
            return face

def best_spot():
    return AI.best_spot(grid, playerTurn, computerTurn)

def gameloop():
    if running:
        emptySpots = 0
        for x in range(3):
            for y in range(3):
                if grid[x][y] == '':
                    emptySpots += 1
        if emptySpots == 0 and turn != '':
            declare_draw()
        
        if turn == computerTurn:
            bestSpot = best_spot()
            button_callback_computer(bestSpot[0], bestSpot[1])
    root.after(1000, gameloop)

make_buttons()

root.after(1000, gameloop)
tk.mainloop()
