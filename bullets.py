import turtle
from turtle import Turtle
from math import tan,cos,sin,pi
class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,0)
        self.color('yellow')
        self.shape('circle')
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.penup()
    def set_position(self,a):
        self.goto(a)
    def set_heading(self,head):
        head=head*pi/180
        self.move_x=3*cos(head)
        self.move_y=3*sin(head)
    def moveto(self):
        self.goto(self.xcor()+self.move_x,self.ycor()+self.move_y)