from turtle import Turtle
from food import Food


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", False, align='center', font=('Courier', 14, 'normal'))

    def increase_score(self):
        self.score += 1
        self.write(f"Score: {self.score}", False, align='center', font=('Courier', 14, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align='center', font=('Courier', 20, 'normal'))