from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for positions in STARTING_POSITIONS:
            self.add_segment(positions)

    def add_segment(self, positions):
        new_square = Turtle("square")
        new_square.pen(pencolor="white", pensize=20, fillcolor="white")
        new_square.color("white")
        new_square.penup()
        new_square.setpos(positions)
        self.segment.append(new_square)

    def extend(self):
        self.add_segment(self.segment[-1].position())

        #Adds a new segment to the snake


    def move(self):
        for num_seg in range(len(self.segment) - 1, 0, -1):
            x_seg = self.segment[num_seg - 1].xcor()
            y_seg = self.segment[num_seg - 1].ycor()
            self.segment[num_seg].setpos(x=x_seg, y=y_seg)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(0)
