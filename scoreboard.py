from turtle import Turtle

# CONSTANTS
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
TOP = (0,270)
CENTER = (0,0)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(TOP)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):

        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(CENTER)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
