import time
from turtle import Screen

from snake import Snake

# set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


def main():
    # create snake
    snake = Snake()

    screen.listen()

    # listen to keys. Turn snake
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(.05)

        snake.move()


main()

screen.exitonclick()
