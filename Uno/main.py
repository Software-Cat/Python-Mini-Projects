import deck
import players

direction = 'counterclockwise'


def set_direction(newDirection):
    direction = newDirection


def get_direction():
    return direction


def reverse_direction():
    global direction
    if direction is 'clockwise':
        direction = 'counterclockwise'
    else:
        direction = 'clockwise'

if __name__ == "__main__":
    print(direction)
    reverse_direction()
    print(direction)