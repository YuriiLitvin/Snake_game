from turtle import Turtle
Y_POSITION = 270


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.ht()
        self.sety(Y_POSITION)
        self.count()

    def count(self):
        self.clear()
        self.write(f"SCORE: {self.score}", False, align="center", font=('Arial', 16, 'normal'))
        self.score += 1


