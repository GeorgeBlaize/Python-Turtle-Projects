from turtle import *

hideturtle()
speed(1)
penup()
goto(-150,-100)
pendown()
fillcolor('red')
begin_fill()
for i in [300,200]*2:
    forward(i)
    circle(30,90)
end_fill()

penup()
goto(-30,-20)
pendown()
fillcolor('white')
begin_fill()
for i in [30,120,120]:
    left(i)
    forward(100)
end_fill()
done()
