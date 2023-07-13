from turtle import Turtle
import random

points = []
for i in range(-280, 280, 20):
    points.append(i)
size = 0.5


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=size, stretch_wid=size)
        self.color("yellow")
        self.speed("fastest")
        random_x = random.choice(points)
        random_y = random.choice(points)
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.choice(points)
        random_y = random.choice(points)
        self.goto(random_x, random_y)
