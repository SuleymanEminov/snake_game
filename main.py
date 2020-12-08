import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# CONSTANTS
SPEED = 0.07

# set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


# initialize snake
snake = Snake()

# initialize food
food = Food()

# initialize scoreboard
scoreboard = Scoreboard()


def main():
    screen.listen()

    # listen to keys. Turn snake
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(SPEED)

        snake.move()

        collision_with_food()  # check if snake collided with food

        game_is_on = collision_with_wall(game_is_on)  # check if snake collided with wall

        game_is_on = collision_with_tail(game_is_on)  # check if snake collided with tail


def collision_with_food():
    # Detect collision with food
    if snake.head.distance(food) < 15:  # 15 is a distance between food and head of the snake
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


def collision_with_wall(game_is_on):
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    return game_is_on


def collision_with_tail(game_is_on):
    # Detect collision with tail
    # if head collides with any segment in the tail:
    # trigger game_over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

    return game_is_on


main()

screen.exitonclick()
