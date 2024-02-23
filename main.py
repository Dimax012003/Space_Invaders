import math
import time

import serial
from turtle import Screen
from test_player import Player
from bullets import Bullet
from spacecrafts import SpaceCraft
from ScoreBoard import Scoreboard
seria=serial.Serial(port='COM7',baudrate=9600)
screen=Screen()
screen.title("square")
screen.setup(height=600,width=600)
screen.tracer(0)
player=Player()
screen.bgcolor("black")

movement={
    "move_x":   0,
    "move_y":   0
}
direction={
    "read_x":   0,
    "read_y":   0
}
scoreboard=Scoreboard()
new_bullets=[]
i=0
k=0
spaceships=[]
losses=0
while True:

    time.sleep(0.001)
    screen.update()
    data=str(seria.readline(1000),"UTF-8")
    new_data = data.split(' ')
    # append direction and movement for the object
    movement["move_x"] = float(new_data[0])
    movement["move_y"] = float(new_data[1])
    direction["read_x"] = float(new_data[3])-520
    direction["read_y"] = float(new_data[4])-520
    player.move(movement["move_x"],movement["move_y"])
    player.set_direction(direction["read_x"],direction["read_y"])
    if(i==10):

        bullet=Bullet()
        bullet.set_position(player.position())
        bullet.set_heading(player.heading()-135)
        print(math.cos(player.heading()))
        new_bullets.append(bullet)
        i=0
    for b in new_bullets:
        b.moveto()
    for s in spaceships:
        s.move()
    if(k==40):
        spacecraft = SpaceCraft()
        spaceships.append(spacecraft)
        k=0
    for b in new_bullets:
        for s in spaceships:
            if(abs(b.xcor()-s.xcor())<=20 and abs(b.ycor()-s.ycor())<=20):
                spaceships.remove(s)
                s.hideturtle()
                new_bullets.remove(b)
                b.hideturtle()
                scoreboard.update()
    for s in spaceships:
        if(s.ycor()<=-300):
            s.hideturtle()
            spaceships.remove(s)
            losses+=1
    for b in new_bullets:
        if(b.ycor()>=300):
            b.hideturtle()
            new_bullets.remove(b)
    if (losses>=5):
        scoreboard.game_over()
        break

    i+=1
    k+=1
screen.mainloop()
