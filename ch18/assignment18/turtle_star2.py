# turtle_star2.py


print("---------8번---------")
import turtle

def drawStar(x,y,length,defined_color):

    star = turtle.Turtle()
    star.shape("turtle")
    star.speed(5)
    star.pensize(1)

    star.color(defined_color)
    star.penup()
    star.goto(x,y)
    star.setheading(0)
    star.pendown()
    for i in range(5):
        star.fd(int(length))
        star.right(144)
    star.hideturtle()


if __name__ == "__main__": 
    turtle.setup(800,600)
    turtle.bgcolor("black")
    drawStar(100,80,50,"yellow")
    turtle.exitonclick()

