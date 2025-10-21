# turtle_star.py

import turtle



def star_drawing(size,x,y):
    star = turtle.Turtle()
    star.pensize(2)
    star.shape("turtle")
    star.speed(10)

    star.penup()
    star.goto(x,y)
    star.pendown()
    star.color("yellow")

    for i in range(5):
        star.forward(size)
        star.right((360/5)*2)
    star.hideturtle()
    star.home



# 터틀 객체 숨기기


if __name__ == "__main__": 
    turtle.setup(410,310)
    turtle.bgcolor("black")

    star_drawing(50,10,10)
    star_drawing(15,60,80)
    turtle.exitonclick()