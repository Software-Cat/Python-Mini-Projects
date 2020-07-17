"""
AI Name: Physics AI

Made by: Bowen

Strategy: Calculate where the ball will land and go there (calculation don't include bricks)

"""

class Rect:
    def __init__(self, position, size):
        self.x = position[0]
        self.y = position[1]
        self.top = position[0]
        self.left = position[1]
        self.bottom = position[1] + size[1]
        self.right = position[0] + size[0]
        self.topleft = [self.top, self.left]
        self.bottomleft = [self.bottom, self.left]
        self.topright = [self.top, self.right]
        self.bottomright = [self.bottom, self.right]
        self.midtop = [(self.left + self.right) / 2.0, self.top]
        self.midleft = [self.left, (self.top + self.bottom) / 2.0]
        self.midbottom = [(self.left + self.right) / 2.0, self.bottom]
        self.midright = [self.right, (self.top + self.bottom) / 2.0]
        self.center = [(self.left + self.right) / 2.0, (self.top + self.bottom) / 2.0]
        self.centerx = (self.left + self.right) / 2.0
        self.centery = (self.top + self.bottom) / 2.0
        self.size = size
        self.width = size[0]
        self.height = size[1]

class Ball(Rect):
    def __init__(self, speed, position, size):
        self.rect = Rect(position, size)
        self.speed = speed

class AI:
    def __init__(self):
        self.needCalculation = True
        self.posXToReach = 0
        self.ball = Ball(self.paddle.getBallSpeed(), self.paddle.getBallRect())
    def move(self):
        if self.needCalculation:
            pass
        
