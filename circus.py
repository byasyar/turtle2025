import turtle
t = turtle.Turtle()
s = turtle.Screen()
t.hideturtle()

s.bgcolor("black")
t.width(2)
t.speed(40)

col = ('orange','red')
for i in range (500):
    t.pencolor(col[i%2])
    t.forward(i/4)
    t.left(73)
    t.right(91)


