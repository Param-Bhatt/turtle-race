from turtle import *
from random import randint

penup()
goto (-140,140)
for step in range(16):
    speed(0)
    write(step,align='center')
    right(90)
    forward(10)
    for x in range(5):
        pendown()
        forward(20)
        penup()
        forward(20)
    backward(210)
    left(90)
    forward(20)

ada=Turtle()
ada.penup()
ada.goto(-160,100)
ada.color('red')
ada.shape('turtle')
for  turn in range(5):
    ada.right(72)
ada.pendown()

bob=Turtle()
bob.penup()
bob.goto(-160,50)
bob.color('blue')
bob.shape('turtle')
bob.pendown()
for  turn in range(5):
    bob.right(72)

cock=Turtle()
cock.penup()
cock.goto(-160,0)
cock.color('green')
cock.shape('turtle')
cock.pendown()
for  turn in range(5):
    cock.right(72)

duck=Turtle()
duck.penup()
duck.goto(-160,-50)
duck.color('yellow')
duck.shape('turtle')
duck.pendown()
for  turn in range(5):
    duck.right(72)

for turn in range(110):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    cock.forward(randint(1,5))
    duck.forward(randint(1,5))