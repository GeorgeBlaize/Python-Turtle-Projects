import turtle

screen=turtle.Screen()
t=turtle.Turtle()

colors=['red','purple','blue','green','orange','yellow']

t.speed(0)
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x//100+1)
    t.forward(x)
    t.left(59)

screen.mainloop()
