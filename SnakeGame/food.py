from snake import Snake
from turtle import Turtle
import random



class Food():
    def __init__(self):
       self.create_food()
       self.X_cor = random.randint(-280, 280)
       self.Y_cor = random.randint(-280, 280)

    def create_food(self):
        self.food = Turtle("circle")
        self.food.color("blue")
        self.food.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.food.penup()
        self.food.goto(x=X_cor, y=Y_cor)
        self.food.speed("fastest")
        self.food.showturtle()

    def refresh(self):
        self.food.goto(x=self.X_cor, y=Y_cor)

