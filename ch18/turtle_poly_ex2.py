# turtle_poly_ex2.py

# 터틀 객체를 활용하여 다각형을 만드는 함수를 정의하고
# 함수를 호출하여 삼각형을 그리시오
# 펜 사이즈: 7
# 색상(테두리/내부): black/olive
# 다각형 함수
#   입력: 각개수, 변길이
#   인수: 3, 80

import turtle

turtle.setup(810,510)
turtle.title("다각형 그리기")
t = turtle.Turtle()
t.shape("turtle")


def poly_drawing(angle,length):
    t.pensize(7)
    t.color("black","olive")
    
    
    for i in range(angle):
        t.right(360/angle)
        t.fd(length)


t.home()
t.reset()

t.begin_fill()
poly_drawing(int(input("각개수:")),int(input("변길이:")))
t.end_fill()


turtle.exitonclick()