import pygame
import sys
from random import randint


class Player(pygame.sprite.Sprite):
    def __init__(self, xPos, yPos, xVel, yVel, color=[0, 0, 0]):
        pygame.sprite.Sprite.__init__(self)

        imageSurface = pygame.surface.Surface([30, 30])
        imageSurface.fill([255, 255, 255])
        pygame.draw.circle(imageSurface, color, [imageSurface.get_width(
        )//2, imageSurface.get_height()//2], imageSurface.get_width()//2)
        self.image = imageSurface.convert()
        self.rect = self.image.get_rect()

        self.rect.x = xPos
        self.rect.y = yPos

        self.xVel = xVel
        self.yVel = yVel

        self.health = 3
        self.shield = 3

        self.invincibleTime = 0

    def right(self):
        self.xVel += 10

    def left(self):
        self.xVel -= 10

    def up(self):
        self.yVel += 10

    def down(self):
        self.yVel -= 10

    def collision(self):
        # With Border
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > screen.get_width():
            self.rect.right = screen.get_width()
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > screen.get_height():
            self.rect.bottom = screen.get_height()

        # With Obstacles
        if self.invincibleTime == 0:
            obstacleGroup = pygame.sprite.Group(obstacles)
            colliding = pygame.sprite.spritecollide(self, obstacleGroup, False)
            for sprite in colliding:
                if self.shield > 0:
                    self.shield -= 1
                elif self.health > 0:
                    self.health -= 1
                if self.health == 0:
                    global running
                    running = False

                self.invincibleTime = 100

    def animate(self):
        self.rect = self.rect.move([self.xVel, self.yVel])

        self.collision()

        self.xVel *= 0.9
        self.yVel *= 0.9


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, xPos, yPos, xVel, yVel, color=[0, 0, 0]):
        pygame.sprite.Sprite.__init__(self)

        imageSurface = pygame.surface.Surface([30, 30])
        imageSurface.fill([0, 0, 0])
        imageSurface.fill(color, [1, 1, 28, 28])
        self.image = imageSurface.convert()
        self.rect = self.image.get_rect()

        self.rect.x = xPos
        self.rect.y = yPos

        self.xVel = xVel
        self.yVel = yVel

    def collision(self):
        # With Border
        if self.rect.right < 0:
            obstacles.remove(self)
            del self
        elif self.rect.bottom < 0:
            obstacles.remove(self)
            del self

    def animate(self):
        self.rect = self.rect.move([self.xVel, self.yVel])

        self.collision()


def show_shield():
    font = pygame.font.Font(None, 30)
    shieldText = 'Shield: ' + str(player.shield)
    shieldTextSurf = font.render(shieldText, 1, (0, 0, 0))
    screen.blit(shieldTextSurf, [530, 10])


def show_health():
    font = pygame.font.Font(None, 30)
    healthText = 'Health: ' + str(player.health)
    healthTextSurf = font.render(healthText, 1, (0, 0, 0))
    screen.blit(healthTextSurf, [530, 40])


def show_score():
    global score
    font = pygame.font.Font(None, 30)
    scoreText = 'Score: ' + str(score)
    scoreTextSurf = font.render(scoreText, 1, (0, 0, 0))
    screen.blit(scoreTextSurf, [10, 10])


def game_over():
    global score
    font = pygame.font.Font(None, 30)

    final_text1 = "Game Over"
    final_text2 = "Your final score is:  " + str(score)

    ft1_font = pygame.font.Font(None, 70)
    ft1_surf = font.render(final_text1, 1, (0, 0, 0))
    ft2_font = pygame.font.Font(None, 50)
    ft2_surf = font.render(final_text2, 1, (0, 0, 0))

    while True:
        screen.fill([255, 255, 255])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.blit(player.image, player.rect)

        for obstacle in obstacles:
            screen.blit(obstacle.image, obstacle.rect)

        show_shield()
        show_health()

        screen.blit(ft1_surf, [screen.get_width() /
                               2 - ft1_surf.get_width()/2, 220])
        screen.blit(ft2_surf, [screen.get_width() /
                               2 - ft2_surf.get_width()/2, 420])

        pygame.display.flip()


def pause():
    while True:
        screen.fill([255, 255, 255])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                global running
                running = False
                return
            elif event.type == pygame.KEYDOWN and event.key == 32:
                return

        screen.blit(player.image, player.rect)

        for obstacle in obstacles:
            screen.blit(obstacle.image, obstacle.rect)

        show_shield()
        show_health()
        show_score()

        pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode([640, 640])

player = Player(320, 320, 0, 0, [randint(0, 200) for i in range(3)])
shiledRegenInterval = 1000
shieldRegenCount = 0

obstacles = []
spawnInterval = 200
spawnTimeCount = 0
spawnAccelInterval = 1000
spawnAccelCount = 0

score = 0

running = True
while running:
    screen.fill([255, 255, 255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == 100:
                player.right()
            elif event.key == 97:
                player.left()
            elif event.key == 115:
                player.up()
            elif event.key == 119:
                player.down()
            elif event.key == 32:
                pause()

    player.animate()
    screen.blit(player.image, player.rect)

    if player.invincibleTime > 0:
        player.invincibleTime -= 1

    if player.shield < 3:
        shieldRegenCount += 1
        if shieldRegenCount == shiledRegenInterval:
            player.shield += 1
            shieldRegenCount = 0

    for obstacle in obstacles:
        obstacle.animate()
        screen.blit(obstacle.image, obstacle.rect)

    spawnTimeCount += 1
    if spawnTimeCount >= spawnInterval:
        obstacles.append(Obstacle(screen.get_width(), randint(0, screen.get_height(
        )), -1-(200-spawnInterval)/90, 0, [randint(0, 200) for i in range(3)]))
        obstacles.append(Obstacle(randint(0, screen.get_width()), screen.get_height(
        ), 0, -1-(200-spawnInterval)/90, [randint(0, 200) for i in range(3)]))
        spawnTimeCount = 0

    spawnAccelCount += 1
    if spawnAccelCount == spawnAccelInterval:
        if spawnInterval > 0:
            spawnInterval -= 10
        spawnAccelCount = 0

    score += 1

    show_shield()
    show_health()
    show_score()

    pygame.display.flip()

game_over()
