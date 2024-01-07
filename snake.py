# Import the Turtle module to create graphics
from turtle import Turtle

# Initial coordinates for the snake segments
COORDINATES = [(0, 0), (-10, 0), (-20, 0)]

# Distance the snake moves in one step
MOVE_DIST = 12

# Constants for direction in degrees
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


# Snake class to manage the snake's behavior
class Snake:
    def __init__(self):
        # List to store the snake segments
        self.segments = []

        # Create the snake segments
        self.create_snake()

        # Set the snake's head
        self.head = self.segments[0]

        # Modify the appearance of the snake's head
        self.head_mod()

        # Start the snake's movement
        self.move()

    # Method to create the snake segments
    def create_snake(self):
        """
        Create initial segments of the snake using predefined coordinates.
        """
        for pos in COORDINATES:
            # Add a segment to the snake at the given position
            self.add_segment(pos)

    def add_segment(self, position):
        """
        Add a new segment to the snake at a given position.
        """
        # Create a new segment using Turtle graphics
        new_segment = Turtle(shape="square")

        # Set the color of the segment
        new_segment.color("orange")

        # Lift the pen to avoid drawing lines
        new_segment.penup()

        # Set the size of the segment
        new_segment.shapesize(0.5, 0.5)

        # Move the segment to the specified position
        new_segment.goto(position)

        # Add the new segment to the snake segments list
        self.segments.append(new_segment)

    def extend(self):
        """
        Extend the snake by adding a new segment at the last segment's position.
        """
        # Add a new segment to the snake at the last segment's position
        self.add_segment(self.segments[-1].position())

    def head_mod(self):
        """
        Modify the appearance of the snake's head.
        """
        self.head.color("cyan")  # Sets the color of the snake's head to cyan
        self.head.shape("circle")  # Changes the shape of the head to a circle
        self.head.shapesize(0.6, 0.8)  # Adjusts the size of the head

    def move(self):
        """
        Move the snake by updating the positions of its segments.
        """
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()  # Retrieves the x-coordinate of the segment before the current one
            new_y = self.segments[seg - 1].ycor()  # Retrieves the y-coordinate of the segment before the current one
            self.segments[seg].goto(new_x, new_y)  # Moves the current segment to the new coordinates
        self.head.forward(MOVE_DIST)  # Moves the snake's head forward by the specified distance

    def up(self):
        """
        Change the snake's direction to up (90 degrees).
        """
        if self.head.heading() != DOWN:  # Checks if the snake is not currently moving downwards
            self.head.setheading(UP)  # Changes the snake's direction to upwards

    def down(self):
        """
        Change the snake's direction to down (270 degrees).
        """
        if self.head.heading() != UP:  # Checks if the snake is not currently moving upwards
            self.head.setheading(DOWN)  # Changes the snake's direction to downwards

    def left(self):
        """
        Change the snake's direction to left (180 degrees).
        """
        if self.head.heading() != RIGHT:  # Checks if the snake is not currently moving to the right
            self.head.setheading(LEFT)  # Changes the snake's direction to the left

    def right(self):
        """
        Change the snake's direction to right (0 degrees).
        """
        if self.head.heading() != LEFT:  # Checks if the snake is not currently moving to the left
            self.head.setheading(RIGHT)  # Changes the snake's direction to the right
