# turtle_rainbow.py

# 써클무지개
import turtle


colors = ["red","orange","yellow","green","blue","navy","purple"]

def rainbow_drawing(radius, x, y):
    
    rainbow = turtle.Turtle()
    rainbow.pensize(5)
    rainbow.shape("turtle")
    rainbow.speed(10)

    for i in range(len(colors)):
        
        rainbow.color(colors[i])
        rainbow.penup()
        rainbow.goto(x-5*i,y)
        # rainbow.home()
        # rainbow.left(90)
        rainbow.setheading(90)
        rainbow.pendown()
        rainbow.circle(radius-5*i,180)
    turtle.hideturtle()
    rainbow.home

if __name__ == "__main__": 
    turtle.setup(410,310)
    turtle.bgcolor("skyblue")

    rainbow_drawing(50,20,90)
    turtle.exitonclick()