"""
AI Name: Follow AI

Made by: Bowen

Strategy: Try to be exactly under the ball to catch it

"""

class AI:
    def __init__(self):
        pass
    def move(self):
        ballX = self.paddle.getBallRect('centerx')
        paddleX = self.paddle.getSelfRect('centerx')
        deltaX = abs(ballX - paddleX)

        if ballX > paddleX:
            self.paddle.paddleRight(deltaX)
        if ballX < paddleX:
            self.paddle.paddleLeft(deltaX)
        else:
            pass
