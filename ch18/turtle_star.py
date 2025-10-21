# turtle_star.py

import turtle

turtle.setup(410,310)
turtle.bgcolor("black")
star = turtle.Turtle()
star.pensize(2)
star.shape("turtle")
star.speed(1)

colors = ["red","yellow","blue","green","purple"]

def star_drawing(color_list):
    n = len(color_list)
    for i in range(n):
        star.color(color_list[i])
        star.forward(100)
        star.right((360/n)*2)

star_drawing(colors)

# 터틀 객체 숨기기
star.hideturtle()

turtle.exitonclick()