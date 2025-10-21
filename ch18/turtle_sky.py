# turtle_sky.py

#무지개와 별을 하늘에 그리는 프로그램을 작성하시오.
# 단, 무지개를 그리는 모듈(turtle_rainbow.py)
# 별을 그리는 모듈 (turtle_yellow_sta.py)을 하위 모듈로 활용하시오

import turtle, turtle_yellow_star, turtle_rainbow

turtle.setup(600,400)
turtle.bgcolor("skyblue")


turtle_yellow_star.star_drawing(15,20,90)
turtle_yellow_star.star_drawing(15,-150,150)
turtle_yellow_star.star_drawing(15,120,200)
turtle_rainbow.rainbow_drawing(50,10,10)

turtle.exitonclick()