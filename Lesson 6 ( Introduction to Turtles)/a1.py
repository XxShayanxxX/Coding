import turtle 

turtle.Screen().bgcolor("white")

screen = turtle.Screen()
screen.setup(800,600)

turtle.title("Welcome to Turtle ")

board = turtle.Turtle()

for i in range(4):
    board.forward(100)
    board.left(90)

    i = i + 1

turtle.done()