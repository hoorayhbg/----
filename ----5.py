import turtle

# square - квадрат, а - длина стороны
def square(a):
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)

square(100) # Вызов функции отрисовки квадрата
def red_cycle(radius):
    turtle.fillcolor('#ff0000')
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def blue_square(radius):
    turtle.fillcolor('#ff00ff')
    turtle.begin_fill()
    turtle.circle(blue_square)
    turtle.end_fill()
turtle.done(100) # Чтобы окно не закрылось
