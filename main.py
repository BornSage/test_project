from random import randrange as rnd
from time import sleep


#ADD NEW CODE HERE
screen = [0] * 10
coords = [0, 0]


for i in range(len(screen)):
    screen[i] = ["."] * 10
screen[0][0] = 1

def random_move(c):
    c[0] = c[0] + rnd(-1, 2)
    if c[0] < 0:
        c[0] = 9
    elif c[0] > 9:
        c[0] = 0

    c[1] = c[1] + rnd(-1, 2)
    if c[1] < 0:
        c[1] = 9
    elif c[1] > 9:
        c[1] = 0
    return c

def print_screen(screen_for_print):
    for i in range(10):
        for j in range(10):
            print(screen_for_print[i][j], end="\t")
        print()


def runn(screen, coords):
    while True:
        screen[coords[0]][coords[1]] = "."
        coords = random_move(coords)
        screen[coords[0]][coords[1]] = "#"
        print("\n\n\n\n\n\n\n")
        print_screen(screen)
        sleep(0.5)

runn(screen, coords)