FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(-200,260)
        self.write(f"Level:{self.score}",align="center",font=("Arial",24,"normal"))

    def update(self):
        self.clear()
        self.score=self.score+1
        self.write(f"Level:{self.score}", align="center", font=("Arial", 24, "normal"))
    def game_over(self):
        self.clear()
        self.write(f"Game over total level:{self.score}", align="center", font=("Arial", 24, "normal"))