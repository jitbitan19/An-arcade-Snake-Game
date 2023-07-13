from turtle import Screen, Turtle

move_distance = 20
screen = Screen()
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []
right = 0
up = 90
left = 180
down = 270


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        # Adds a segment
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(move_distance)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(270)
