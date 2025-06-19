from turtle import Turtle, Screen


starting_position = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DOWN = 270
UP = 90
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):

        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]


    def create_snake(self):
        for pos in starting_position:
            snake = Turtle()
            snake.color("white")
            snake.shape("square")
            snake.penup()
            snake.goto(pos)
            self.snake_list.append(snake)

    def move(self):
        for i in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[i - 1].xcor()
            new_y = self.snake_list[i - 1].ycor()
            self.snake_list[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:


           self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:

            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)



