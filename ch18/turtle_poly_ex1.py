# turtle_poly_ex1.py

# 터틀 객체를 활용하여 십이각형을 그려보기
# 한변 길이: 80
# 펜 사이즈: 7
# 색상(테두리/내부): black/olive

import turtle

turtle.setup(810,510)
turtle.title("다각형 그리기")
t = turtle.Turtle()
t.shape("turtle")

t.color("black","olive")
t.pensize(7)

t.begin_fill()
for i in range(12):
    t.right(360/12)
    t.fd(80)
t.end_fill()

t.home()
t.reset()

turtle.exitonclick()

