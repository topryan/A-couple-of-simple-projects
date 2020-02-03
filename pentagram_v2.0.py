import turtle

def draw_pentagram(x):
    count = 1
    while count <= 5:
        count += 1
        turtle.forward(x)
        turtle.right(144)

def main():

    turtle.penup()
    turtle.backward(100)
    turtle.pendown()
    turtle.pensize(2)
    turtle.color('blue')
    turtle.speed(3)
    size = 100
    while size <= 300:
        size += 30
        draw_pentagram(size)
    turtle.exitonclick()

if __name__ == '__main__':
    main()