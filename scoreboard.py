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
        self.high_score = 0
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.goto(TOP)
        self.update_scoreboard()

    def update_scoreboard(self):  # update the scoreboard after snake eats food
        self.clear()
        with open("data.txt",mode="r") as file:
            score = file.read()
            self.high_score = int(score)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):  # increase score by 1
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):  # print GAME OVER on the screen
    #     self.goto(CENTER)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open("data.txt", mode="w") as file:
                contents = file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()