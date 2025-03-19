import turtle

turtle.speed(6)
turtle.bgcolor('black')

colors=['red','magenta','blue','cyan','green','yellow','white',
        'orange','purple','lime','pink','gold']

for i in range(6):
    for color in colors:
        turtle.color(color)
        turtle.pensize(3)
        turtle.left(10)
        for _ in range(4):
            turtle.forward(200)
            turtle.left(90)

turtle.done()
