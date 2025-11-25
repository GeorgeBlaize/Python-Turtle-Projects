from turtle import *

bgcolor('black')
pencolor('cyan')
speed(0)
pensize(2)
setposition(-180,-55)

n=10

while n>0:
    left(n)
    forward(n)
    forward(400)
    backward(200)
    circle(45,45)
    forward(200)
    circle(90,90)
    forward(100)
    circle(160,160)

done()
