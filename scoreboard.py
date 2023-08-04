from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("yellow")
        self.pu()
        self.goto(-5, 280)

    def update_scoreboard(self, current_score):
        self.clear()
        self.write(arg=f"Score: {current_score}", align="center", font=("Arial", 12, "normal"))

    def final_score(self, current_score):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"Game Over, your score:{current_score}", align="center", font=("Arial", 19, "normal"))
