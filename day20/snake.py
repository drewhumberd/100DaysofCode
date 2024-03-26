from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270

class Snake:
    '''defines snake object you use to play the game'''
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        '''arrays starting three segments to starting positions'''
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        '''adds a segment to the snake'''
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setpos(position)
        self.segments.append(new_segment)

    def extend(self):
        '''extends snake when it eats'''
        self.add_segment(self.segments[-1].position())

    def move(self):
        '''moves snake forward according to heading'''
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].setpos(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        '''turns snake left'''
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        '''turns snake right'''
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        '''turns snake north'''
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        '''turns snake south'''
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
