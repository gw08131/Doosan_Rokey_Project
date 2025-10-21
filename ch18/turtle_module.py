# turtle_module.py

import turtle

# 전체 그래픽 창 및 전역 설정
# 윈도우 제목 설정
turtle.title("거북이 그래픽스")
# 윈도우 크기 설정
turtle.setup(410,310)

# 배경색 설정
turtle.bgcolor("beige")
#turtle.bgcolor("#4B78C7")

# 터틀 객체 생성
t = turtle.Turtle()

# 터틀 객체 모양 설정
t.shape("turtle")               # 모양 could be: shapes: 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
# 터틀 객체 색 설정
t.color("black","green")    # t.color("경계선색","채움색")

# 회전
t.right(180)
t.left(90)

# 홈(원) 위치로 이동
t.home()

# 속도 설정
t.speed(10)          # 0-10까지 속도 조절 가능 (느림-빠름 but 0 is the fastest)

# 글 작성
# t.write("거북아 글 작성해줘~",font=("바탕체", 10, "normal"))
# t.write("토끼와 거북이", font=("arial",20,"italic"))
t.write("거북이", font=("맑은고딕",30,"bold"))

# 이동
# 펜 들기/ 내리기
t.penup()
t.forward(80)
t.pendown()
t.backward(100)
# 펜 색상 설정
t.pencolor("blue")          # 터틀 객체 경계선 색상도 같이 변경됨
# 펜 크기 설정
t.pensize(3)

# 사각형 그리기
t.left(90); t.fd(50)
t.right(90); t.fd(150)
t.right(90); t.fd(50)
t.right(90); t.fd(150)
t.left(180)

# 빈 도화지 상태로 리셋
t.reset()       


# 터틀 객체를 활용하여 정사각형을 그려보기
# 가로 70, 세로 70
# 펜 색상: skyblue
# 펜 사이즈:5

t.home()
t.color("black","green")
t.pencolor("skyblue")
t.pensize(5)

t.speed(1)

t.fd(70); t.left(90)
t.fd(70); t.left(90)
t.fd(70); t.left(90)
t.fd(70); t.left(90)


# 터틀 객체를 활용하여 정사각형을 그려보기
# 가로 120, 세로 80
# 펜 색상: green
# 펜 사이즈:3

t.reset()     
t.home()
t.pensize(3)
t.pencolor("green")

t.speed(1)

t.fd(120); t.left(90)
t.fd(80); t.left(90)
t.fd(120); t.left(90)
t.fd(80); t.left(90)



# 메인 루프 실행
# turtle.mainloop()
# turtle.done()
turtle.exitonclick()