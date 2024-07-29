from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score

screen = Screen()
screen.bgcolor("black")
screen.width = 800
screen.height = 600
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-370, 0))
r_paddle = Paddle((370, 0))
ball = Ball()
score = Score()

difficulty = 0.1

screen.listen()
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(l_paddle) < 50 and (ball.xcor() == -350):
        ball.bounce_x()
    if ball.distance(r_paddle) < 50 and (ball.xcor() == 350):
        ball.bounce_x()
    # detect ball out of bounds
    if ball.xcor() > 420:
        ball.reset_position()
        l_paddle.reset_position()
        r_paddle.reset_position()
        score.increase_score_left()

    if ball.xcor() < -420:
        ball.reset_position()
        l_paddle.reset_position()
        r_paddle.reset_position()
        score.increase_score_right()

screen.exitonclick()
