from turtle import Turtle,Screen
from paddle import Paddle
import time




screen = Screen()
screen.setup(width=800, height= 600)
screen.bgcolor('black')
screen.title("pong")
screen.tracer(0)


paddle_r_pos =Paddle((360,0))
paddle_l_pos = Paddle((-360,0))
screen.listen()
screen.onkey(paddle_r_pos.up,'Up')
screen.onkey(paddle_r_pos.down,"Down")

game_is_on = True


while game_is_on:
    screen.update()

screen.exitonclick()