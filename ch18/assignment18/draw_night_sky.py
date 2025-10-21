# draw_night_sky.py

print("---------10번---------")
import turtle
import turtle_moon
import turtle_star2

turtle.setup(800, 600)
turtle.bgcolor("black")

turtle_star2.drawStar(50, 30, 10, "white")
turtle_star2.drawStar(-120, 120, 15, "white")
turtle_star2.drawStar(200, -50, 20, "white")
turtle_moon.drawMoon(180, 180, 60, "yellow")

turtle.exitonclick()
