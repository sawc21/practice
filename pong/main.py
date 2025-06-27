from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
screen = Screen()
screen.setup(width=800, height= 600)
screen.bgcolor('black')
screen.title("pong")
screen.tracer(0)


paddle_r_pos =Paddle((360,0))
paddle_l_pos = Paddle((-360,0))
ball = Ball()
new_x = ball.xcor() + 5
new_y = ball.ycor() + 5


ball.speed('slowest')
screen.listen()
screen.onkey(paddle_r_pos.up,'Up')
screen.onkey(paddle_r_pos.down,"Down")

game_is_on = True


while game_is_on:

    screen.update()
    time.sleep(0.03)
    ball.move()



    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_r_pos) < 50 and ball.xcor() > 340 :
        ball.bounce_x()


    if ball.ycor() > paddle_l_pos.ycor() + 10 :
        paddle_l_pos.up()


    if ball.ycor() < paddle_l_pos.ycor() - 10 :

        paddle_l_pos.down()



screen.exitonclick()