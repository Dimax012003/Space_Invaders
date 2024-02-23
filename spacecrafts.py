from turtle import Turtle
import random
class SpaceCraft(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.color('green')
        self.shapesize(stretch_wid=2,stretch_len=2)
        self.goto(random.random()*1000-500,300)
    def move(self):
        self.goto(self.xcor(),self.ycor()-2)
