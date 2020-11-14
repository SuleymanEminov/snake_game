from turtle import Turtle

# CONSTANTS
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
TOP = (0,270)
CENTER = (0,0)
COLOR = "red"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.goto(TOP)
        self.update_scoreboard()

    def update_scoreboard(self):  # update the scoreboard after snake eats food
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):  # increase score by 1
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):  # print GAME OVER on the screen
        self.goto(CENTER)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
