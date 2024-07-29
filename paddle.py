from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, tuple_position):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(tuple_position)
        self.init_position = tuple_position

    def move_up(self):
        y = self.ycor()
        y += 20
        self.goto(self.xcor(), y)

    def move_down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)

    def reset_position(self):
        self.goto(self.init_position)
