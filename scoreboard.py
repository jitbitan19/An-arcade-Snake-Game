from turtle import Turtle
import time

font = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.setpos(0, 260)
        self.hideturtle()
        self.update_score()

    def add_score(self):
        self.score += 1

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score = {self.high_score}", False, "center", font)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over...", False, "center", font)

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update_score()
