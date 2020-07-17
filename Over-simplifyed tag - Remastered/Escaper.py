import turtle as t

friction = 0.9

class Escaper(t.RawTurtle):
    _screen = None
    
    def __init__(self, x, y, speed, shape='classic', color='black', visible=True):
        # Init raw turtle and canvas
        if Escaper._screen is None:
            Escaper._screen = t.Screen()
        t.RawTurtle.__init__(self, Escaper._screen, shape=shape, visible=True)

        # Set appearance
        self.color(color)
        self.speed(0)
        self.penup()

        # Set variables regarding pos
        self.x = x
        self.y = y
        self.goto(x, y)
        self.xVel = 0
        self.yVel = 0

    def move_up(self):
        self.yVel += 3

    def move_down(self):
        self.yVel -= 3

    def move_left(self):
        self.xVel -= 3

    def move_right(self):
        self.xVel += 3

    def animate(self):
        # Move
        self.x += self.xVel
        self.y += self.yVel
        self.goto(self.x, self.y)
        self.x *= friction
        self.y *= friction

        # Detect collision
        for tagger in taggers:
            if collide_with(tagger):
                textTurtle.write('GAME OVER', align='center', font=('arial', 16, 'bold'))

    def collide_with(self, turtleObj):
        if self.distance(turtleObj) < 20:
            return True
        else:
            return False

class Tagger(t.RawTurtle):
    def __init__(self, x, y, shape='classic', size=1, color='black', visible=True):
        # Init raw turtle and canvas
        if Escaper._screen is None:
            Escaper._screen = t.Screen()
        t.RawTurtle.__init__(self, Escaper._screen, shape=shape, visible=True)

        # Set appearance
        self.color(color)
        self.speed(0)
        self.penup()
        self.size = size
        self.shapesize(size, size)

        # Set variables regarding pos
        self.x = x
        self.y = y
        self.goto(x, y)
        self.xVel = 0
        self.yVel = 0

textTurtle = t.Turtle()
textTurtle.ht()

taggers = []

def loop():
    pass

def end_loop():
    pass

player = Escaper(100, 100, 'circle', 1)

player.animate()

