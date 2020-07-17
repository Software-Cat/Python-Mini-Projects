import turtle as t
import math
import random

t.ht()
t.bgcolor('lightblue')

X_Vel = 0
Y_Vel = 0

player = t.Turtle()
player.hideturtle()
player.shape('square')
player.color('green')
player.speed(0)
player.penup()
player.goto([-200, 200])

bullets = []
time_before_vanishing = {}
for i in range(5):
    bullet = t.Turtle()
    bullet.ht()
    bullet.shape('triangle')
    bullet.color('orange')
    bullet.speed(0)
    bullet.penup()
    bullets.append(bullet)
    time_before_vanishing[bullet] = 50
origin = {}
knock_back_directions = {}

game_started = False
text_turtle = t.Turtle()
text_turtle.hideturtle()
text_turtle.write('Press SPACE to start', align='center', font=('arial', 16, 'bold'))

def move_left():
    global X_Vel
    X_Vel += -5

def move_right():
    global X_Vel
    X_Vel += 5

def move_up():
    global Y_Vel
    Y_Vel = 15

def touching_player(entity):
    if entity.distance(player) < 20:
        return True
    else:
        return False

def player_warp():
    player.goto([random.randint(-t.window_width() // 2, t.window_width() // 2), random.randint(-t.window_height() // 2, t.window_height() // 2)])

def start_game():
    global game_started
    if game_started:
        return
    game_started = True

    global X_Vel
    global Y_Vel
    global bullets
    global knock_back_directions
    global time_before_vanishing
    global origin

    text_turtle.clear()
    player.st()

    while True:
        #Player
        player.setx(player.pos()[0] + X_Vel) #X Vel
        X_Vel *= 0.9
        player.sety(player.pos()[1] + Y_Vel) #Y Vel
        if player.pos()[1] <= -t.window_height() // 2.0 + 18: #If on ground
            player.sety(-t.window_height() // 2.0 + 19)
            Y_Vel = 0
        else: #accel. down if not on ground
            if player.pos()[1] > -t.window_height() // 2.0 + 19:
                Y_Vel -= 1

        to_delete = []
        for direction in knock_back_directions: #Knock-backing
            if knock_back_directions[str(direction)] <= 0:
                to_delete.append(str(direction))
            else:
                player.setheading(float(direction))
                player.forward(20)
                player.setheading(0)
                knock_back_directions[str(direction)] -= 1
        for item in to_delete:
            del knock_back_directions[item]
        #Bullets
        for bullet in bullets:
            if time_before_vanishing[bullet] == 50:
                origin[bullet] = [random.randint(-t.window_width() // 2, t.window_width() // 2), random.randint(-t.window_height() // 2, t.window_height() // 2)]#Random position
                bullet.goto(origin[bullet])
                if bullet.pos()[0] == player.pos()[0]: #If are in straight directions
                    if bullet.pos()[1] > player.pos()[1]:
                        bullet.setheading(270)
                    else:
                        bullet.setheading(90)
                elif bullet.pos()[1] == player.pos()[1]:
                    if bullet.pos()[0] > player.pos()[0]:
                        bullet.setheading(180)
                    else:
                        bullet.setheading(0)
                else: #Else calculate direction with inverse tan
                    difX = abs(bullet.pos()[0] - player.pos()[0])
                    difY = abs(bullet.pos()[1] - player.pos()[1])
                    turn_angle = math.degrees(math.atan(difY//float(difX)))
                    if bullet.pos()[0] > player.pos()[0] and bullet.pos()[1] > player.pos()[1]:
                        bullet.setheading(0)
                        bullet.left(turn_angle)
                    elif bullet.pos()[0] < player.pos()[0] and bullet.pos()[1] > player.pos()[1]:
                        bullet.setheading(180)
                        bullet.right(turn_angle)
                    elif bullet.pos()[0] < player.pos()[0] and bullet.pos()[1] < player.pos()[1]:
                        bullet.setheading(180)
                        bullet.left(turn_angle)
                    else:
                        bullet.setheading(0)
                        bullet.right(turn_angle)
                    bullet.left(180)
                bullet.st() 
                bullet.forward(20)
                time_before_vanishing[bullet] -= 1
            elif time_before_vanishing[bullet] > 0: #Constant move forward
                bullet.forward(20)
                time_before_vanishing[bullet] -= 1
            else: #Reborn as a new bullet after vanishing
                bullet.ht()
                time_before_vanishing[bullet] = 50

            if touching_player(bullet): #Appling knockback force
                knock_back_directions[str(bullet.heading())] = 10
                bullet.ht()
                time_before_vanishing[bullet] = 50

            difX = abs(bullet.pos()[0] - origin[bullet][0])
            difY = abs(bullet.pos()[1] - origin[bullet][1])
            difX2 = abs(origin[bullet][0] - player.pos()[0])
            difY2 = abs(origin[bullet][1] - player.pos()[1])
            if math.sqrt(difX**2 + difY**2) > math.sqrt(difX2**2 + difY2**2): #Reborn as a new bullet when sure cannot hit player even when not time to vanish yet
                bullet.ht()
                time_before_vanishing[bullet] = 50

t.onkey(start_game, 'space')
t.onkey(move_left, 'a')
t.onkey(move_right, 'd')
t.onkey(move_up, 'w')
t.onkey(player_warp, 'q')
t.listen()
t.mainloop()
