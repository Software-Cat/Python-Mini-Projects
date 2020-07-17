import pygame
import sys

def vertical_dashed_line(screen, color, startPos, length, width, dashLength):
    segments = []
    dashes = int(length/dashLength)
    startY = startPos[1]

    for i in range(dashes):
        if i%2 == 0:
            segments.append([[startPos[0], startY+i*dashLength], [startPos[0], startY+(i+1)*dashLength]])

    for segment in segments:
        pygame.draw.line(screen, color, segment[0], segment[1], width)
    


def game_over():
    pass


def pause():
    pass


def draw_stage():
    # Ground
    pygame.draw.rect(screen, [200, 200, 200], [0, 0, 1105, 697])
    pygame.draw.rect(screen, [0, 0, 0], [0, 0, 1105, 697], 2)

    # Court
    pygame.draw.rect(screen, [230, 230, 230], [42.5, 93.5, 1020, 510])

    # Neutral Zone
    pygame.draw.rect(screen, [190, 190, 190], [518.5, 93.5, 68, 510], 0)
    # Court lines
    # Centerline
    pygame.draw.line(screen, [0, 0, 0], [552.5, 93.5], [552.5, 603.5])
    # Neutral lines
    vertical_dashed_line(screen, [0, 0, 0], [518.5, 93.5], 510, 1, 12)
    #pygame.draw.line(screen, [0, 0, 0], [518.5, 93.5], [518.5, 603.5])
    pygame.draw.line(screen, [0, 0, 0], [586.5, 93.5], [586.5, 603.5])
    # Court border accent
    pygame.draw.rect(screen, [0, 0, 0], [42.5, 93.5, 1020, 510], 5)


pygame.init()
screen = pygame.display.set_mode([1105, 697])
# Coefficient = 17

running = True
while running:
    draw_stage()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

game_over()
