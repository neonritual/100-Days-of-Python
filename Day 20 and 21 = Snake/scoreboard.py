from turtle import Turtle
ALIGNMENT = "center"
FONT = "Arial", 24

class Score(Turtle):
    def __init__(self):
        self.player_score = 0
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score: {self.player_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=("Arial", 50, "normal"))


    def increase_score(self):
        self.player_score += 1
        self.clear()
        self.update_score()