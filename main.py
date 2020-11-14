import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


def main():
    # initialize snake
    snake = Snake()

    # initialize food
    food = Food()

    # initialize scoreboard
    scoreboard = Scoreboard()

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

        # Detect collision with food
        if snake.head.distance(food) < 15: # 15 is a distance between food and head of the snake
            food.refresh()

            scoreboard.increase_score()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            scoreboard.game_over()



main()

screen.exitonclick()
