# turtle_moon.py
 
print("---------9번---------")

import turtle

def drawMoon(x,y,radius,defined_color):
 
    moon = turtle.Turtle()
    moon.shape("turtle")

    moon.color(defined_color)
    moon.penup()
    moon.goto(x,y-int(radius))
    moon.setheading(0)
    moon.pendown()
   
    moon.begin_fill()
    moon.circle(int(radius))
    moon.end_fill()
    moon.hideturtle()

if __name__ == "__main__": 
    turtle.setup(800,600)
    turtle.bgcolor("black")

    drawMoon(100,80,50,"yellow")
    turtle.exitonclick()