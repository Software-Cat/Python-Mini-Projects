import turtle as t
import random as r

directions = [0, 90, 180, 270]
colors = ["red","orange","yellow","green","cyan","blue","purple"]
step_length = 10
turn = 0

t.bgcolor("black")
t.speed(0)
t.pensize(1)
t.goto(0,0)

t.pendown()
while True:
    t.color(r.choice(colors)) # change direction and color
    t.setheading(r.choice(directions))

    if t.pos()[0] < -t.window_width() / 2: # if inside GUI
        t.setheading(0)
    if t.pos()[0] > t.window_width() / 2:
        t.setheading(180)
    if t.pos()[1] < -t.window_height() / 2:
        t.setheading(90)
    if t.pos()[1] > t.window_height() / 2:
        t.setheading(270)

    if r.randint(1,5) == 1: # move with a chance of not leaving a line behind
        t.penup()
        for i in range(r.randint(1,5)):
            t.forward(step_length)
        t.pendown()
    else:
        for i in range(r.randint(1,5)):
            t.forward(step_length)
