from turtle import Turtle

# Constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # body positions of snake
MOVE_DISTANCE = 20

# headings
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []  # body of the snake
        self.create_snake()  # create the body of the snake
        self.head = self.segments[0]  # head of the snake

    def create_snake(self):
        for position in STARTING_POSITIONS:  # create body
            self.add_segment(position)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        new_segment = Turtle("square")  # create body segment
        new_segment.color("white")  # color of body segment
        new_segment.penup()
        new_segment.goto(position)  # position snake's body segment
        self.segments.append(new_segment)  # add body segment to the list

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # move forward
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)

    # Turn up
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
