import turtle
t = turtle.Turtle()
s = turtle.Screen()
t.hideturtle()

s.bgcolor("black")
t.width(1)
t.speed(110)


col = ('red', 'white')
for i in range (300):
    t.pencolor(col[i%1])
    t.forward(5)
    t.left(i/2)
    t.back(i)







