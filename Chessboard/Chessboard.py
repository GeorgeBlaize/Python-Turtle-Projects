import turtle

sc=turtle.Screen()

pen=turtle.Turtle()

def draw_square(color):
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(4):
        pen.forward(50)
        pen.left(90)
    pen.end_fill()

if __name__=="__main__":
    sc.setup(600,600)
    sc.setworldcoordinates(-250,-250,250,250)

    pen.speed(10)
    pen.penup()
    
    for row in range(8):
        for col in range(8):
            x=col*50-200
            y=row*50-200
            pen.goto(x,y)
            pen.pendown()
            color='black' if(row+col)%2==0 else 'white'
            draw_square(color)
            pen.penup()
    pen.hideturtle()
    sc.mainloop()
