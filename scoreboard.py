# Importing the Turtle module to create a scoreboard for a game
from turtle import Turtle

# Constants for text alignment and font style
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

# Creating a Scoreboard class that inherits from the Turtle class


class Scoreboard(Turtle):
    # Constructor method that initializes the scoreboard
    def __init__(self):
        # Initializing the Turtle properties
        super().__init__()  # Calls the constructor of the Turtle class
        self.score = 0  # Setting the initial score to 0
        self.color("white")  # Setting text color to white
        self.penup()  # Not drawing while moving
        self.goto(0, 270)  # Positioning the scoreboard at (0, 270)
        self.hideturtle()  # Hiding the turtle icon
        self.update_scoreboard()  # Updating the scoreboard initially

    def update_scoreboard(self):
        """
        Updates the scoreboard with the current score.
        """
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """
        Increases the score by 1 and updates the scoreboard display.
        """
        self.score += 1  # Incrementing the score by 1
        self.clear()  # Clearing the previous score display
        self.update_scoreboard()  # Updating the scoreboard with the new score

    def game_over(self):
        """
        Displays "GAME OVER" at the center of the screen.
        """
        self.goto(0, 0)  # Moving to the center of the screen
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)  # Displaying "GAME OVER"
