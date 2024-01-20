# Import the Turtle module to create a simple graphics window
from turtle import Turtle

# Initial coordinates for the snake segments
COORDINATES = [(0, 0), (-10, 0), (-20, 0)]

# Distance to move the snake in each step
MOVE_DIST = 12

# Constants for direction angles
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

# Snake class definition
class Snake:
    def __init__(self):
        # List to store the segments of the snake
        self.segments = []

        # Create the initial snake with default segments
        self.create_snake()

        # Set the head of the snake
        self.head = self.segments[0]

        # Customize the appearance of the snake head
        self.head_mod()

        # Move the snake
        self.move()

    def create_snake(self):
        # Create snake segments at specified coordinates
        for pos in COORDINATES:
            self.add_segment(pos)

    def add_segment(self, position):
        # Add a new segment to the snake
        new_segment = Turtle(shape="square")
        new_segment.color("orange")
        new_segment.penup()
        new_segment.shapesize(0.5, 0.5)
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # Add a new segment to the end of the snake
        self.add_segment(self.segments[-1].position())

    def head_mod(self):
        # Customize the appearance of the snake head
        self.head.color("cyan")
        self.head.shape("circle")
        self.head.shapesize(0.6, 0.8)

    def resett(self):
        # Reset the snake to its initial state
        for seg in self.segments:
            seg.goto(1000, 1000)  # Move segments out of the screen
        self.segments.clear()  # Clear the segments list
        self.create_snake()  # Recreate the snake
        self.head = self.segments[0]  # Set the head to the new first segment
        self.head_mod()  # Customize the appearance of the head again

    def move(self):
        # Move the snake forward
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

    def up(self):
        # Change the snake's direction to upward if not already moving downward
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Change the snake's direction to downward if not already moving upward
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # Change the snake's direction to the left if not already moving right
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # Change the snake's direction to the right if not already moving left
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
