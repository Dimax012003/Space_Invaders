import turtle

STARTING_POSITION = (0,0)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle
from math import atan,pi
class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.shapesize(stretch_wid=2,stretch_len=2)
        self.shape('circle')
        self.speed("fastest")
        self.goto(0,0)
        self.color('red')
        self.setheading(90)
    def move(self,x,y):
        self.goto(self.xcor()+((517-x)/52),self.ycor()+((y-517)/52))
    def set_direction(self,x,y):
        if(x==0 and y>0):
            c=90
        elif(x==0 and y<0):
            c=270
        else:
            if(x>0 and y>0):
                a=float(y/x)
                c = (atan(a))*180/pi
            elif(x<0 and y>0):
                a=float(y/(abs(x)))
                c = (atan(a) +  pi / 2)*180/pi
            elif(x<0 and y<0):
                a=float(y/x)
                c = (atan(a) + 2 * pi / 2)*180/pi
            elif(x>0 and y<0):
                a=float(abs(y)/x)
                c=(atan(a)+3*pi/2)*180/pi
        self.setheading(c)
    def finish(self):
        if self.ycor()==FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True