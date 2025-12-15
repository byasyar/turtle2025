import turtle
t = turtle.Turtle()
s = turtle.Screen()
t.hideturtle()

s.bgcolor("black")
t.width(2)
t.speed(15)

col = ('pink', 'purple', 'yellow')
for i in range (250):
    t.pencolor(col[i%3])
    t.forward(i*5)
    t.right(121)


