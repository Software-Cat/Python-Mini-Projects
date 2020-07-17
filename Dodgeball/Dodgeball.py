import sys, pygame
import random
pygame.init()

screenX, screenY = 1300, 800
screen = pygame.display.set_mode([screenX, screenY])



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP and event.key == 27:
            print(event.key)
            running = False

pygame.quit()
