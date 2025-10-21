# turtle_circle.py

# 원그리기
import turtle

turtle.setup(410,310)
t = turtle.Turtle()
t.shape("turtle")
t.pencolor("skyblue")
t.pensize(3)
t.color("black","olive")


# 1. 사용자 입력을 통해 반지름 설정하기
# 2. 함수로 처리하기

def make_circle(raidus):
    t.circle(raidus)

t.begin_fill()
make_circle(int(input("반지름: ")))
t.end_fill()
t.reset()

r = 50
n = 60
t.speed(0)
t.color("black","skyblue")

t.begin_fill()
for i in range(n):
    make_circle(r)
    t.right(360/n)
t.end_fill()

turtle.exitonclick()