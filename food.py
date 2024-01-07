# Importing necessary modules
from turtle import Turtle  # Importing the Turtle class from the turtle module
import random  # Importing the random module for generating random numbers

# Creating a Food class that inherits from the Turtle class


class Food(Turtle):
    def __init__(self):
        # Initializing the Food object
        super().__init__()  # Calling the constructor of the Turtle class
        self.shape("circle")  # Setting the shape of the food as a circle
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Making the circle smaller
        self.penup()  # Preventing drawing lines when moving
        self.color("blue")  # Setting the color of the food to blue
        self.speed("fastest")  # Setting the speed of the food object's movements
        self.refresh()  # Calling the method to position the food initially

    def refresh(self):
        """
        Moves the food to a new random position within the game window.
        """
        # Generating random coordinates for the food within a specific range
        cor_x = random.randint(-280, 280)  # Random x-coordinate within -280 to 280
        cor_y = random.randint(-280, 280)  # Random y-coordinate within -280 to 280
        # Moving the food to the randomly generated coordinates
        self.goto(x=cor_x, y=cor_y)
