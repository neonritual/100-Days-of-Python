from turtle import Turtle, Screen

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.player_score = 1
        self.update_score()

    def update_score(self):
        self.goto(x=-200, y=250)
        self.write(arg=f"Level: {self.player_score}", font=FONT)

    def increase_score(self):
        self.player_score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
