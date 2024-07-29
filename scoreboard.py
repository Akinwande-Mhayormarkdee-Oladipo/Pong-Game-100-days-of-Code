from turtle import Turtle


class Score:
    def __init__(self):
        self.score_left = 0
        self.score_right = 0
        self.score_pen = Turtle()
        self.score_pen.speed(0)
        self.score_pen.color("white")
        self.score_pen.penup()
        self.score_pen.goto(0, 280)
        self.score_pen.hideturtle()
        self.update_score()

    def update_score(self):
        self.score_pen.clear()
        self.score_pen.write(f"{self.score_left}   |    {self.score_right}", align="center",
                             font=("Arial", 40, "normal"))

    def increase_score_left(self):
        self.score_left += 1
        self.update_score()

    def increase_score_right(self):
        self.score_right += 1
        self.update_score()
