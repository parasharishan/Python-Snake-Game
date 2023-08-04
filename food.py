import random
from turtle import Turtle
colors = {"red": [0.35, 10], "orange": [0.45, 8], "green": [0.5, 6], "blue": [0.6, 5]}


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.speed("fastest")
        self.score = 0
        self.refresh()

    def refresh(self):
        current_colour = list(random.choice(list(colors.items())))
        self.color(current_colour[0])
        self.score = current_colour[1][1]
        self.shapesize(stretch_len=current_colour[1][0], stretch_wid=current_colour[1][0])
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)
