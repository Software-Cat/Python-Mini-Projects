import turtle as t
import math
import random

X_Vel = 0
Y_Vel = 0

enemy_X_Vel = 0
enemy_Y_Vel = 0

t.hideturtle()

t.bgcolor('skyblue')

player = t.Turtle()
player.shape('circle')
player.color('red')
player.speed(0)
player.penup()
player.hideturtle()
player.goto([200, -200])

enemy = t.Turtle()
enemy.shape('square')
enemy.color('green')
enemy.speed(0)
enemy.penup()
enemy.goto([-200, 200])
enemy.ht()
warp_cooldown = 100

player_bullet = t.Turtle()
player_bullet.shape('triangle')
player_bullet.color('orange')
player_bullet.speed(0)
player_bullet.penup()
player_bullet.ht()
enemy_knock_back_count = 0
bullet_time = 0

player_clone = t.Turtle()
player_clone.shape('circle')
player_clone.color('red')
player_clone.speed(0)
player_clone.penup()
player_clone.ht()
using_player_clone = False
player_clone_X_Vel = 0
player_clone_Y_Vel = 0

player_clone_bullet = t.Turtle()
player_clone_bullet.shape('triangle')
player_clone_bullet.color('orange')
player_clone_bullet.speed(0)
player_clone_bullet.penup()
player_clone_bullet.ht()
player_clone_enemy_knock_back_count = 0
player_clone_bullet_time = 0

game_started = False
text_turtle = t.Turtle()
text_turtle.write('Press SPACE to start', align='center', font=('arial', 16, 'bold'))
text_turtle.hideturtle()

def move_left():
    global X_Vel
    X_Vel += -5

def move_right():
    global X_Vel
    X_Vel += 5

def move_up():
    global Y_Vel
    Y_Vel = 10

def touching_enemy(entity):
    if entity.distance(enemy) < 20:
        return True
    else:
        return False

def player_shoot_bullet():
    global bullet_time
    bullet_time = 50

def player_clone_shoot_bullet():
    global player_clone_bullet_time
    player_clone_bullet_time = 50

def player_make_clone():
    global using_player_clone
    using_player_clone = True
    player_clone.goto(player.pos())
    player_clone.st()
    player_clone_shoot_bullet()

def enemy_warp():
    if warp_cooldown == 0:
        enemy.goto([random.randint(-t.window_width() // 2, t.window_width() // 2), random.randint(-t.window_height() // 2, t.window_height() // 2)])

def start_game():
    global game_started
    if game_started:
        return
    game_started = True

    global X_Vel
    global Y_Vel
    global enemy_X_Vel
    global enemy_Y_Vel
    global enemy_knock_back_count
    global bullet_time
    global player_clone_enemy_knock_back_count
    global player_clone_bullet_time
    global warp_cooldown
    global player_clone_X_Vel
    global player_clone_Y_Vel
    global using_player_clone

    text_turtle.clear()
    player.st()
    enemy.st()

    enemy_moving_counter_X = 0
    enemy_moving_counter_Y = 0

    while True:
        #Player
        player.setx(player.pos()[0] + X_Vel)
        X_Vel *= 0.9

        player.sety(player.pos()[1] + Y_Vel)
        if player.pos()[1] <= -t.window_height() // 2.0 + 18:
            player.sety(-t.window_height() // 2.0 + 19)
            Y_Vel = 0
        else:
            if player.pos()[1] > -t.window_height() // 2.0 + 19:
                Y_Vel -= 1
        #Player clone
        if using_player_clone:
            if player_clone.distance(player_clone_bullet) > player_clone.distance(enemy) or not player_clone_bullet.isvisible():
                player_clone_shoot_bullet()

            if player_clone.distance(player) > 200:
                if player_clone.pos()[0] < player.pos()[0]:
                    player_clone_X_Vel += 3
                else:
                    player_clone_X_Vel -= 3
                if player_clone.pos()[1] < player.pos()[1]:
                    player_clone_Y_Vel = 10
            else:
                if player_clone.pos()[0] < enemy.pos()[0]:
                    player_clone_X_Vel += 3
                else:
                    player_clone_X_Vel -= 3
                if player_clone.pos()[1] < enemy.pos()[1]:
                    player_clone_Y_Vel =  player_clone.distance(enemy) // 100

            if player_clone.pos()[0] > t.window_width() // 2.0 or player_clone.pos()[0] < -t.window_width() // 2.0:
                player_clone_X_Vel *= -1
            if player_clone.pos()[1] > t.window_height() // 2.0:
                player_clone_Y_Vel *= -1

            player_clone.setx(player_clone.pos()[0] + player_clone_X_Vel)
            player_clone_X_Vel *= 0.9
            player_clone.sety(player_clone.pos()[1] + player_clone_Y_Vel)
            if player_clone.pos()[1] <= -t.window_height() // 2.0 + 18:
                player_clone.sety(-t.window_height() // 2.0 + 19)
                player_clone_Y_Vel = 0
            else:
                if player_clone.pos()[1] > -t.window_height() // 2.0 + 19:
                    player_clone_Y_Vel -= 1
        else:
            player_clone.ht()
        #Player clone bullet
        if player_clone_bullet_time == 50:
            player_clone_bullet.goto(player_clone.pos())
            if player_clone_bullet.pos()[0] == enemy.pos()[0]:
                if player_clone_bullet.pos()[1] > enemy.pos[1]:
                    player_clone_bullet.setheading(270)
                else:
                    player_clone_bullet.setheading(90)
            elif player_clone_bullet.pos()[1] == enemy.pos()[1]:
                if player_clone_bullet.pos()[0] > enemy.pos()[0]:
                    player_clone_bullet.setheading(180)
                else:
                    player_clone_bullet.setheading(0)
            else:
                difX = abs(player_clone_bullet.pos()[0] - enemy.pos()[0])
                difY = abs(player_clone_bullet.pos()[1] - enemy.pos()[1])
                turn_angle = math.degrees(math.atan(difY//float(difX)))
                if player_clone_bullet.pos()[0] > enemy.pos()[0] and player_clone_bullet.pos()[1] > enemy.pos()[1]:
                    player_clone_bullet.setheading(0)
                    player_clone_bullet.left(turn_angle)
                elif player_clone_bullet.pos()[0] < enemy.pos()[0] and player_clone_bullet.pos()[1] > enemy.pos()[1]:
                    player_clone_bullet.setheading(180)
                    player_clone_bullet.right(turn_angle)
                elif player_clone_bullet.pos()[0] < enemy.pos()[0] and player_clone_bullet.pos()[1] < enemy.pos()[1]:
                    player_clone_bullet.setheading(180)
                    player_clone_bullet.left(turn_angle)
                else:
                    player_clone_bullet.setheading(0)
                    player_clone_bullet.right(turn_angle)
                player_clone_bullet.left(180)
            player_clone_bullet.st()
            player_clone_bullet.forward(20)
            player_clone_bullet_time -= 1
        elif player_clone_bullet_time > 0:
            player_clone_bullet.forward(20)
            player_clone_bullet_time -= 1
        else:
            player_clone_bullet.ht()

        if touching_enemy(player_clone_bullet):
            player_clone_enemy_knock_back_count = 10
            player_clone_bullet.ht()
            player_clone_bullet_time = 0
        #Player bullet
        if bullet_time == 50:
            player_bullet.goto(player.pos())
            if player_bullet.pos()[0] == enemy.pos()[0]:
                if player_bullet.pos()[1] > enemy.pos[1]:
                    player_bullet.setheading(270)
                else:
                    player_bullet.setheading(90)
            elif player_bullet.pos()[1] == enemy.pos()[1]:
                if player_bullet.pos()[0] > enemy.pos()[0]:
                    player_bullet.setheading(180)
                else:
                    player_bullet.setheading(0)
            else:
                difX = abs(player_bullet.pos()[0] - enemy.pos()[0])
                difY = abs(player_bullet.pos()[1] - enemy.pos()[1])
                turn_angle = math.degrees(math.atan(difY//float(difX)))
                if player_bullet.pos()[0] > enemy.pos()[0] and player_bullet.pos()[1] > enemy.pos()[1]:
                    player_bullet.setheading(0)
                    player_bullet.left(turn_angle)
                elif player_bullet.pos()[0] < enemy.pos()[0] and player_bullet.pos()[1] > enemy.pos()[1]:
                    player_bullet.setheading(180)
                    player_bullet.right(turn_angle)
                elif player_bullet.pos()[0] < enemy.pos()[0] and player_bullet.pos()[1] < enemy.pos()[1]:
                    player_bullet.setheading(180)
                    player_bullet.left(turn_angle)
                else:
                    player_bullet.setheading(0)
                    player_bullet.right(turn_angle)
                player_bullet.left(180)
            player_bullet.st()
            player_bullet.forward(20)
            bullet_time -= 1
        elif bullet_time > 0:
            player_bullet.forward(20)
            bullet_time -= 1
        else:
            player_bullet.ht()
    
        if touching_enemy(player_bullet):
            enemy_knock_back_count = 10
            player_bullet.ht()
            bullet_time = 0
        #Enemy
        if warp_cooldown == 0:
            enemy_warp()
            warp_cooldown = 100
        else:
            warp_cooldown -= 1
        
        "Attack real player and clone"
        if not using_player_clone:
            if player.pos()[0] > enemy.pos()[0]:
                if enemy_moving_counter_X >= 5:
                    enemy_X_Vel += 5
                    enemy_moving_counter_X = 0
            elif player.pos()[0] < enemy.pos()[0]:
                if enemy_moving_counter_X >= 5:
                    enemy_X_Vel += -5
                    enemy_moving_counter_X = 0
            enemy_moving_counter_X += 1
            if player.pos()[1] > enemy.pos()[1]:
                if enemy_moving_counter_Y >= 5:
                    enemy_Y_Vel = 10
                    enemy_moving_counter_Y = 0
            enemy_moving_counter_Y += 1
        else:
            if enemy.distance(player) < enemy.distance(player_clone):
                if player.pos()[0] > enemy.pos()[0]:
                    if enemy_moving_counter_X >= 5:
                        enemy_X_Vel += 5
                        enemy_moving_counter_X = 0
                elif player.pos()[0] < enemy.pos()[0]:
                    if enemy_moving_counter_X >= 5:
                        enemy_X_Vel += -5
                        enemy_moving_counter_X = 0
                enemy_moving_counter_X += 1
                if player.pos()[1] > enemy.pos()[1]:
                    if enemy_moving_counter_Y >= 5:
                        enemy_Y_Vel = 10
                        enemy_moving_counter_Y = 0
                enemy_moving_counter_Y += 1
            else:
                if player_clone.pos()[0] > enemy.pos()[0]:
                    if enemy_moving_counter_X >= 10:
                        enemy_X_Vel += 5
                        enemy_moving_counter_X = 0
                elif player_clone.pos()[0] < enemy.pos()[0]:
                    if enemy_moving_counter_X >= 10:
                        enemy_X_Vel += -5
                        enemy_moving_counter_X = 0
                enemy_moving_counter_X += 1
                if player_clone.pos()[1] > enemy.pos()[1]:
                    if enemy_moving_counter_Y >= 10:
                        enemy_Y_Vel = 10
                        enemy_moving_counter_Y = 0
                enemy_moving_counter_Y += 1
        "Only attack the real player"
        """
        if player.pos()[0] > enemy.pos()[0]:
            if enemy_moving_counter_X >= 5:
                enemy_X_Vel += 5
                enemy_moving_counter_X = 0
        elif player.pos()[0] < enemy.pos()[0]:
            if enemy_moving_counter_X >= 5:
                enemy_X_Vel += -5
                enemy_moving_counter_X = 0
        enemy_moving_counter_X += 1
        if player.pos()[1] > enemy.pos()[1]:
            if enemy_moving_counter_Y >= 5:
                enemy_Y_Vel = 10
                enemy_moving_counter_Y = 0
        enemy_moving_counter_Y += 1
        """

        if enemy_knock_back_count >= 1:
            enemy.setheading(player_bullet.heading())
            enemy.forward(20)
            enemy.setheading(0)
            enemy_knock_back_count -= 1
        if player_clone_enemy_knock_back_count >= 1:
            enemy.setheading(player_clone_bullet.heading())
            enemy.forward(20)
            enemy.setheading(0)
            player_clone_enemy_knock_back_count -= 1

        enemy.setx(enemy.pos()[0] + enemy_X_Vel)
        enemy_X_Vel *= 0.9
        enemy.sety(enemy.pos()[1] + enemy_Y_Vel)
        if enemy.pos()[1] <= -t.window_height() // 2.0 + 18:
            enemy.sety(-t.window_height() // 2.0 + 19)
            enemy_Y_Vel = 0
        else:
            if enemy.pos()[1] > -t.window_height() // 2.0 + 19:
                enemy_Y_Vel -= 1
        #Killing
        if touching_enemy(player):
            text_turtle.write('Game Over', align='center', font=('arial', 16, 'bold'))
            break
        if touching_enemy(player_clone):
            using_player_clone = False

t.onkey(start_game, 'space')
t.onkey(move_left, 'a')
t.onkey(move_right, 'd')
t.onkey(move_up, 'w')
t.onkey(player_shoot_bullet, 'q')
t.onkey(player_make_clone, 'e')
t.listen()
t.mainloop()
