# Modified version of Listing_19-5.py:
#   -Copyright Warren & Csrter Sande, 2013
#   -Released under MIT license   http://www.opensource.org/licenses/mit-license.php
#   -Version $version  ----------------------------
#Modifications
#   -Realistic(gravity, side hitting, etc.)
#   -Changed spawn pos and vel of ball
#   -New scoring system(hit bricks to gain points)
#   -Controlled by AI

# PyPong with sounds and music

import pygame, sys
#################### New stuff start
import random

class OutOfTurnError(Exception):
    #A custom error describing a state in which the paddle controller move the paddle multiple times in one move
    def __str__(self):
        return 'The AI of paddle controller tried to move the paddle multiple times in one move'
#################### New stuff end

class MyBallClass(pygame.sprite.Sprite): 
    def __init__(self, image_file, speed, location = [0,0]): 
        pygame.sprite.Sprite.__init__(self)   
        self.image = pygame.image.load(image_file) 
        self.rect = self.image.get_rect() 
        self.rect.left, self.rect.top = location 
        self.speed = speed
        #################### New stuff start
        #The gravity constant
        self.gravity = 0.4
        #################### New stuff end
 
    def move(self): 
        global points, score_text 
        self.rect = self.rect.move(self.speed) 
        if self.rect.left < 0 or self.rect.right > screen.get_width():
            self.speed[0] = -self.speed[0] 
            if self.rect.top < screen.get_height(): 
                pass
                # hit_wall.play()          #Play sound when the ball hits the side wall
                                               
        if self.rect.top <= 0 : 
            self.speed[1] = -self.speed[1]
            #hit_wall.play()             #Play sound when the ball hits the top wall

        #################### New stuff start
        #A tiny bit of acceleration due to gravity
        self.speed[1] += self.gravity
        #################### New stuff end

class MyPaddleClass(pygame.sprite.Sprite): 
    def __init__(self, location = [0,0]): 
        pygame.sprite.Sprite.__init__(self) 
        image_surface = pygame.surface.Surface([100, 20]) 
        image_surface.fill([0,0,0]) 
        self.image = image_surface.convert() 
        self.rect = self.image.get_rect() 
        self.rect.left, self.rect.top = location
        
#################### New stuff start
#The brick class
class MyBrickClass(pygame.sprite.Sprite):
    def __init__(self, location=[0, 0], color=[0, 0, 0]):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([100, 50])
        image_surface.fill([0, 0, 0], [0, 0, 100, 50])
        image_surface.fill(color, [1, 1, 98, 48])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

#AI class to store the imported ai and allow it to interact with the world
paddleMoved = False
class PaddleController:
    def __init__(self, ai):
        self.ai = ai
        ai.paddle = self

    def getBallRect(self, key): #Get attrubutes about the ball rect
        global myBall
        if key == 'x':
            return myBall.rect.x
        if key == 'y':
            return myBall.rect.y
        if key == 'top':
            return myBall.rect.top
        if key == 'left':
            return myBall.rect.left
        if key == 'bottom':
            return myBall.rect.bottom
        if key == 'right':
            return myBall.rect.right
        if key == 'topleft':
            return myBall.rect.topleft
        if key == 'bottomleft':
            return myBall.rect.bottomleft
        if key == 'topright':
            return myBall.rect.topright
        if key == 'bottomright':
            return myBall.rect.bottomright
        if key == 'midtop':
            return myBall.rect.midtop
        if key == 'midleft':
            return myBall.rect.mideft
        if key == 'midbottom':
            return myBall.rect.midbottom
        if key == 'midright':
            return myBall.rect.midright
        if key == 'center':
            return myBall.rect.center
        if key == 'centerx':
            return myBall.rect.centerx
        if key == 'centery':
            return myBall.rect.centery
        if key == 'size':
            return myBall.rect.size
        if key == 'width':
            return myBall.rect.width
        if key == 'height':
            return myBall.rect.height
        if key == 'w':
            return myBall.rect.w
        if key == 'h':
            return myBall.rect.h
        else:
            if type(key) == str:
                raise ValueError('There are no such key named ' + key)
            else:
                raise TypeError('The function only accept string typed parameters, got ' + str(type(key)) + ' insted')

    #Get attributes about the paddle rect
    def getSelfRect(self, key):
        global paddle
        if key == 'x':
            return paddle.rect.x
        if key == 'y':
            return paddle.rect.y
        if key == 'top':
            return paddle.rect.top
        if key == 'left':
            return paddle.rect.left
        if key == 'bottom':
            return paddle.rect.bottom
        if key == 'right':
            return paddle.rect.right
        if key == 'topleft':
            return paddle.rect.topleft
        if key == 'bottomleft':
            return paddle.rect.bottomleft
        if key == 'topright':
            return paddle.rect.topright
        if key == 'bottomright':
            return paddle.rect.bottomright
        if key == 'midtop':
            return paddle.rect.midtop
        if key == 'midleft':
            return paddle.rect.mideft
        if key == 'midbottom':
            return paddle.rect.midbottom
        if key == 'midright':
            return paddle.rect.midright
        if key == 'center':
            return paddle.rect.center
        if key == 'centerx':
            return paddle.rect.centerx
        if key == 'centery':
            return paddle.rect.centery
        if key == 'size':
            return paddle.rect.size
        if key == 'width':
            return paddle.rect.width
        if key == 'height':
            return paddle.rect.height
        if key == 'w':
            return paddle.rect.w
        if key == 'h':
            return paddle.rect.h
        else:
            if type(key) == str:
                raise ValueError('There are no such key named ' + key)
            else:
                raise TypeError('The function only accept string typed parameters, got ' + str(type(key)) + ' insted')

    #Get the number of bricks currently on the screen
    def getBrickNum(self):
        global bricks
        return len(bricks)

    #Get attributes about the bricks rect
    def getBrickRect(self, brickNum, key):
        #Note: brickNum start at 0
        global bricks
        if type(brickNum) != int: 
            raise TypeError('The function only accept int typed parameters, got ' + str(type(key)) + ' insted')
        if type(brickNum) == int and brickNum > len(bricks) - 1:
            raise IndexError('There are only ' + str(len(bricks)) + ' bricks. You cannot ask about the ' + str(brickNum + 1) + 'th brick as it does not exist')
        if key == 'x':
            return bricks[brickNum].rect.x
        if key == 'y':
            return bricks[brickNum].rect.y
        if key == 'top':
            return bricks[brickNum].rect.top
        if key == 'left':
            return bricks[brickNum].rect.left
        if key == 'bottom':
            return bricks[brickNum].rect.bottom
        if key == 'right':
            return bricks[brickNum].rect.right
        if key == 'topleft':
            return bricks[brickNum].rect.topleft
        if key == 'bottomleft':
            return bricks[brickNum].rect.bottomleft
        if key == 'topright':
            return bricks[brickNum].rect.topright
        if key == 'bottomright':
            return bricks[brickNum].rect.bottomright
        if key == 'midtop':
            return bricks[brickNum].rect.midtop
        if key == 'midleft':
            return bricks[brickNum].rect.mideft
        if key == 'midbottom':
            return bricks[brickNum].rect.midbottom
        if key == 'midright':
            return bricks[brickNum].rect.midright
        if key == 'center':
            return bricks[brickNum].rect.center
        if key == 'centerx':
            return bricks[brickNum].rect.centerx
        if key == 'centery':
            return bricks[brickNum].rect.centery
        if key == 'size':
            return bricks[brickNum].rect.size
        if key == 'width':
            return bricks[brickNum].rect.width
        if key == 'height':
            return bricks[brickNum].rect.height
        if key == 'w':
            return bricks[brickNum].rect.w
        if key == 'h':
            return bricks[brickNum].rect.h
        else:
            if type(key) == str:
                raise ValueError('There are no such key named ' + key)
            else:
                raise TypeError('The function only accept string typed parameters, got ' + str(type(key)) + ' insted')

    #Get the ball's velocity
    def getBallSpeed(self):
        global myBall
        return myBall.speed

    #Get the width and height of screen
    def getScreenSize(self):
        global screen
        return [screen.get_width(), screen.get_height()]

    #Get the acceleration due to gravity that is affecting the ball
    def getGravity(self):
        global myBall
        return myBall.gravity

    #Move the paddle left at speed
    def paddleLeft(self, speed):
        global paddle
        global paddleMoved
        #Error detection
        if type(speed) != int and type(speed) != float:
            raise TypeError('The function only accept int typed parameters, got ' + str(type(speed)) + ' insted')
        if paddleMoved:
            raise OutOfTurnError
        #Edge collision
        if paddle.rect.left < 0:
            return
        #Speed regulation
        if speed > 50: 
            speed = 50
        if speed < 0:
            speed = 0
        #Moving the paddle
        paddle.rect.centerx -= speed
        paddleMoved = True

    #Move the paddle right at speed
    def paddleRight(self, speed):
        global paddle
        global paddleMoved
        #Error detection
        if type(speed) != int and type(speed) != float:
            raise TypeError('The function only accept int typed parameters, got ' + str(type(speed)) + ' insted')
        if paddleMoved:
            raise OutOfTurnError
        #Edge collision
        if paddle.rect.right > screen.get_width():
            return
        #Speed regulation
        if speed > 50: 
            speed = 50
        if speed < 0:
            speed = 0
        #Moving the paddle
        paddle.rect.centerx += int(speed)
        paddleMoved = True

#Function to create new bricks
def createNewBricks(amount):
    global bricks
    global bricksGroup
    #Creating instances of bricks
    bricks = []
    for i in range(amount):
        position = [random.randint(0, 540), random.randint(0, 400)]
        color = [random.randint(20, 200), random.randint(20, 200), random.randint(20, 200)]
        brick = MyBrickClass(position, color)
        bricks.append(brick)
    bricksGroup = pygame.sprite.Group(bricks)
    #Try reposition bricks if they are overlapsing for 100 times (too many times will cause lag)
    for brick in bricks:
        bricksGroup.remove(brick)
        for i in range(100):
            if pygame.sprite.spritecollide(brick, bricksGroup, False):
                brick.location = [random.randint(0, 540), random.randint(0, 400)]
        bricksGroup.add(brick)

#Create Paddle Controller based on ai

#Get name of ai
aiName = input('Enter ai: ')
#Dynamically import the ai as a module
ai = __import__(aiName)
#Create paddleController object with ai
paddleController = PaddleController(ai.AI())
#################### New stuff end
pygame.init()
pygame.mixer.init()


pygame.mixer.music.load("AI PyPong/Single Player/bg_music.mp3")          # Load background music
pygame.mixer.music.set_volume(0.3)               # Set volume for music
pygame.mixer.music.play(-1)                      # Play music forever
hit = pygame.mixer.Sound("AI PyPong/Single Player/hit_paddle.wav")          # Load other sounds 
hit.set_volume(0.4)                                 #   and set their volumes 
new_life = pygame.mixer.Sound("AI PyPong/Single Player/new_life.wav")       #
new_life.set_volume(0.5)                            #
splat = pygame.mixer.Sound("AI PyPong/Single Player/splat.wav")             #
splat.set_volume(0.6)                               #
hit_wall = pygame.mixer.Sound("AI PyPong/Single Player/hit_wall.wav")       #
hit_wall.set_volume(0.4)                            #
get_point = pygame.mixer.Sound("AI PyPong/Single Player/get_point.wav")     #
get_point.set_volume(0.2)                           #
bye = pygame.mixer.Sound("AI PyPong/Single Player/game_over.wav")           #
bye.set_volume(0.6)                                 #

screen = pygame.display.set_mode([640,640]) 
clock = pygame.time.Clock() 

#################### New stuff start
#Got rid of: myBall = MyBallClass('wackyball.bmp', [12,0], [50, 50])
#Goto top center with randomized horizontal momentum
myBall = MyBallClass('AI PyPong/Single Player/wackyball.png', [random.choice([12, -12]),0], [320, 50])
#################### New stuff end
ballGroup = pygame.sprite.Group(myBall) 
paddle = MyPaddleClass([270, 560])
#################### New stuff start
#For later use in calculating paddle vel per tick
oldPaddleX = paddle.rect.centerx
PaddleX = paddle.rect.centerx
paddleXVel = 0

#create 10 initial bricks
bricks = []
bricksGroup = []
createNewBricks(10)
#################### New stuff end
lives = 3
points = 0 
 
font = pygame.font.Font(None, 50) 
score_text = font.render(str(points), 1, (0, 0, 0)) 
textpos = [10, 10] 
done = False 

running = True
while running: 
    clock.tick(30) 
    screen.fill([255, 255, 255]) 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
        #################### New stuff start
        #This is the old paddle controlling system
        #Got rid of: elif event.type == pygame.MOUSEMOTION: 
        #Got rid of:    paddle.rect.centerx = event.pos[0]
        #################### New stuff end

    #################### New stuff start
    #Reset paddleController's paddleMoved because it is a new turn
    paddleMoved = False
    #AI do it's move
    try:
        paddleController.ai.move()
    except Exception as e:
        print('The AI controlling the paddle failed with error')
        print (e)

    #Calculate paddle velocity per frame
    oldPaddleX = PaddleX
    PaddleX = paddle.rect.centerx
    paddleXVel = PaddleX - oldPaddleX
    #################### New stuff end

    if pygame.sprite.spritecollide(paddle, ballGroup, False):
        # hit.play()                              # Play sound when the ball hits the paddle
        #################### New stuff start
        #If hit side of paddle reverse horizontal vel as well
        if myBall.rect.bottom + myBall.speed[1] < paddle.rect.top:
            myBall.speed[0] = -myBall.speed[0]
        #Paddle velocity affect ball velocity (f=m*a)
        myBall.speed[0] += paddleXVel / 5.0
        #Got rid of: myBall.speed[1] = -myBall.speed[1]
        #Ball always go up
        myBall.speed[1] = -abs(myBall.speed[1])
        #################### New stuff end

    #################### New stuff start
    bricksToDelete = []
    for brick in bricks:
        if pygame.sprite.spritecollide(brick, pygame.sprite.Group(myBall), False):
                points = points + 1          #(player gets a point)
                score_text = font.render(str(points), 1, (0, 0, 0)) 
                # get_point.play()             #Plays sound when the ball hits the top

                #Ball bounce off
                if myBall.rect.bottom - myBall.speed[1] < brick.rect.top or myBall.rect.top - myBall.speed[1] > brick.rect.bottom :
                    myBall.speed[1] = -myBall.speed[1]
                if myBall.rect.right - myBall.speed[0] < brick.rect.left or myBall.rect.left - myBall.speed[0] > brick.rect.right:
                    myBall.speed[0] = -myBall.speed[0]

                #Sotre brick to delete it later
                bricksToDelete.append(brick)
    #Brick is deleted
    for brick in bricksToDelete:
        bricks.remove(brick)
        bricksGroup.remove(brick)

    #if there are no bricks left create some more
    if len(bricks) == 0:
        createNewBricks(10)
    #################### New stuff end
 
    myBall.move() 
 
    if not done:
        #################### New stuff start
        #Render the bircks
        for brick in bricks:
            screen.blit(brick.image, brick.rect)
        #################### New stuff end
        screen.blit(myBall.image, myBall.rect) 
        screen.blit(paddle.image, paddle.rect) 
        screen.blit(score_text, textpos) 
        for i in range (lives): 
            width = screen.get_width() 
            screen.blit(myBall.image, [width - 40 * i, 20]) 
        pygame.display.flip() 
 
    if myBall.rect.top >= screen.get_rect().bottom: 
        if not done: 
            pass
            # splat.play()           # Plays sound when the player loses a life
        lives = lives - 1 
        if lives <= 0: 
            if not done: 
                pygame.time.delay(1000)             #Wait one second, 
                # bye.play()                          #  then play the ending sound
            final_text1 = "Game Over" 
            final_text2 = "Your final score is:  " + str(points) 
            ft1_font = pygame.font.Font(None, 70) 
            ft1_surf = font.render(final_text1, 1, (0, 0, 0)) 
            ft2_font = pygame.font.Font(None, 50) 

            ft2_surf = font.render(final_text2, 1, (0, 0, 0)) 
            screen.blit(ft1_surf, [screen.get_width()/2 - \
                        ft1_surf.get_width()/2, 100]) 
            screen.blit(ft2_surf, [screen.get_width()/2 - \
                        ft2_surf.get_width()/2, 200]) 

            pygame.display.flip() 
            done = True 
            pygame.mixer.music.fadeout(2000)        #Fade out the music
            running = False
        else: 
            pygame.time.delay(1000)                 
            # new_life.play()                         #Play sound when a new life starts
            #################### New stuff start
            #Got rid of: myBall.rect.topleft = [50, 50]
            #Goto top center
            myBall.rect.center = [320, 50]
            #Have no vertical momentum and random horizontal momentum when start
            myBall.speed[0] = random.choice([12, -12])
            myBall.speed[1] = 0
            #################### New stuff end
            screen.blit(myBall.image, myBall.rect) 
            pygame.display.flip() 
            pygame.time.delay(1000)

running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
pygame.quit()
