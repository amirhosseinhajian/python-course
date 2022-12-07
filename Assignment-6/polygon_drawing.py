import turtle

pen = turtle.Turtle()
pen.shape("turtle")
x = 24
for i in range(3, 50):
    pen.up()
    pen.setheading(0)
    pen.forward(7)
    pen.down()
    pen.left(30)
    for j in range(i):
        pen.left(360 / i)
        pen.forward(x)
    x += 8
turtle.done()
