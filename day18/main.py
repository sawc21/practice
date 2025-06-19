
import turtle as t
import random

# Setup
t.colormode(255)
screen = t.Screen()
screen.setup(1200, 1200)

# Constants
DOT_SIZE = 25
DOT_SPACING = 50
GRID_SIZE = 10
START_POS = (-500, -500)

# Color palette
color_list = [
    (184, 163, 130), (130, 91, 70), (79, 92, 117), (147, 160, 179),
    (210, 208, 138), (178, 151, 159), (113, 83, 93), (35, 38, 49),
    (47, 31, 25), (55, 29, 35), (144, 170, 154), (83, 107, 89),
    (163, 156, 63), (108, 36, 49), (161, 110, 120), (117, 36, 28),
    (36, 43, 41), (52, 58, 88), (105, 121, 160), (170, 106, 96),
    (108, 146, 104), (184, 187, 207), (213, 182, 176), (211, 179, 188),
    (172, 205, 178), (70, 76, 35)
]

# Turtle setup
timmy = t.Turtle()
timmy.penup()
timmy.hideturtle()
timmy.setposition(START_POS)
timmy.speed("fastest")

# Draw the grid
for row in range(GRID_SIZE):
    for col in range(GRID_SIZE):
        timmy.dot(DOT_SIZE, random.choice(color_list))
        if col < GRID_SIZE - 1:
            timmy.forward(DOT_SPACING)

    # Move to next row
    if row < GRID_SIZE - 1:
        if row % 2 == 0:
            timmy.left(90)
            timmy.forward(DOT_SPACING)
            timmy.left(90)
        else:
            timmy.right(90)
            timmy.forward(DOT_SPACING)
            timmy.right(90)

screen.exitonclick()
