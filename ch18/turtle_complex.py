# turtle_complex.py

import turtle

turtle.setup(410,310)
t = turtle.Turtle()
t.shape("turtle")
t.pencolor("skyblue")
t.pensize(1)
t.color("black","skyblue")
t.speed(0)


n = 300

for i in range(n):
    t.forward(i)
    t.right(91)


turtle.exitonclick()