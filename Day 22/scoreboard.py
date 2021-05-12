from turtle import Turtle
ALIGNMENT = "center"
FONT = "Arial", 24

class Score(Turtle):
    def __init__(self):
        self.r_player_score = 0
        self.l_player_score = 0
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()

        self.update_score()

    def update_score(self):
        self.goto(x=-50, y=190)
        self.write(arg=self.l_player_score, align=ALIGNMENT, font=FONT)
        self.goto(x=50, y=190)
        self.write(arg=self.r_player_score, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=("Arial", 50, "normal"))


    def increase_l_score(self):
        self.l_player_score += 1
        self.clear()
        self.update_score()

    def increase_r_score(self):
        self.r_player_score += 1
        self.clear()
        self.update_score()