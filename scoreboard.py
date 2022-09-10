from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 10, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.penup()
        self.goto(x=0, y=270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def gameover(self):
        self.color("white")
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
