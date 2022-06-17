from turtle import Turtle
Y_COORD = 270
ALIGNMENT = "center"
FONT = ("Impact", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.ht()
        self.sety(Y_COORD)
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.write(f"SCORE: {self.score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


