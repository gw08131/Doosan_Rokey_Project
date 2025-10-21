# turtle_circle_rainbow.py

# 써클무지개
import turtle

turtle.setup(410,310)
turtle.bgcolor("black")

rainbow = turtle.Turtle()
rainbow.pensize(2)
rainbow.shape("turtle")
rainbow.speed(0)

colors = ["red","orange","yellow","green","blue","navy","purple"]

def rainbow_drawing():
    n = len(colors)
    for i in range(n):
        rainbow.color(colors[i])
        rainbow.circle(50+5*i)

    rainbow.home

rainbow_drawing()

# 터틀 객체 숨기기
rainbow.hideturtle()

turtle.exitonclick()