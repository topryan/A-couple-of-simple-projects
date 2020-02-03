import turtle

def draw_branch(branch_length):
    if branch_length >= 10:
        # paint right branches
        turtle.forward(branch_length)
        print('go forward', branch_length)
        turtle.right(20)
        print('turn right 20')
        draw_branch(branch_length-5)

        # paint left branches
        turtle.left(40)
        print('turn left 40')
        draw_branch(branch_length - 5)

        # return to the last branch
        turtle.right(20)
        print('turn right 20')
        turtle.backward(branch_length)
        print('go backward', branch_length)

def main():
    turtle.left(90)
    turtle.penup()
    turtle.backward(100)
    turtle.pendown()
    turtle.color('brown')
    draw_branch(50)
    turtle.exitonclick()

if __name__ == '__main__':
    main()