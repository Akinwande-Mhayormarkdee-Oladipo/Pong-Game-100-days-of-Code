from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(0)
        self.dx = 10
        self.dy = 10
        self.move_speed = 0.1
        self.move()

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

        # if (new_x > 370) or (new_x < -370):
        #     self.dx *= -1

    def bounce_y(self):
        # detect collision with top and bottom walls
        self.dy *= -1

    def bounce_x(self):
        # detect collision with left and right walls
        self.dx *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.dx *= -1
        self.dy *= -1
        self.move_speed = 0.1
