# turtle_poly.py

# 다각형 그리기

import turtle

turtle.setup(810,510)
turtle.title("다각형 그리기")
t = turtle.Turtle()
t.shape("turtle")

n = -1
while n == -1:
    t.pencolor("skyblue")
    t.pensize(3)
    t.color("black","gold")
    n = int(input("몇 각형: "))

    # 도형 내부 색상 filled
    t.begin_fill()
    for i in range(n):
        t.right(360/n)
        t.fd(70)
    t.end_fill()
    t.reset()
    
    t.home()

# 터틀 객체를 활용하여 십이각형을 그려보기
# 한변 길이: 80
# 펜 사이즈: 7
# 색상(테두리/내부): black/olive

t.color("black","olive")
t.pensize(7)

t.begin_fill()
for i in range(12):
    t.right(360/12)
    t.fd(80)
t.end_fill()

t.home()
t.reset()

# 터틀 객체를 활용하여 다각형을 만드는 함수를 정의하고
# 함수를 호출하여 삼각형을 그리시오
# 펜 사이즈: 7
# 색상(테두리/내부): black/olive
# 다각형 함수
#   입력: 각개수, 변길이
#   인수: 3, 80

def poly_drawing(x,length):
    t.pensize(7)
    t.color("black","olive")
    
    t.begin_fill()
    for i in range(x):
        t.right(360/x)
        t.fd(length)
    t.end_fill()
t.home()
t.reset()

poly_drawing(3,80)

turtle.exitonclick()

