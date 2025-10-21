# turtle_for.py

import turtle

turtle.setup(410,310)

t = turtle.Turtle()
# 사각형 그리기
t.shape("turtle")
t.pencolor("skyblue")
t.pensize(3)

for i in range(4):
    t.right(90)
    t.fd(70)
t.home()

# 오각형 그리기
t.reset()

t.shape("turtle")
t.pencolor("tomato")
t.pensize(3)

for i in range(5):
    t.right(360/5)
    t.forward(70)
t.home()

turtle.exitonclick()