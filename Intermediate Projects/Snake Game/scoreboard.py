from turtle import Turtle
from food import Food


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscores.txt") as data:
            self.high_score = int(data.read())
        self.ht()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", False, align='center', font=('Courier', 14, 'normal'))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align='center', font=('Courier', 14, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscores.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

