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
        with open("data.txt") as file: # Opening data.txt containg our High Score intialed to 0
            self.high_score = int(file.read())
        self.color("white")  # Setting text color to white
        self.penup()  # Not drawing while moving
        self.goto(0, 270)  # Positioning the scoreboard at (0, 270)
        self.hideturtle()  # Hiding the turtle icon
        self.update_scoreboard()  # Updating the scoreboard initially

    def update_scoreboard(self):
        """
        Updates the scoreboard with the current score.
        """
        self.clear()  # Clearing the previous score display
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """
        Increases the score by 1 and updates the scoreboard display.
        """
        self.score += 1  # Incrementing the score by 1
        self.update_scoreboard()  # Updating the scoreboard with the new score

    def resett(self):
    # Check if the current score is higher than the high score
    if self.score > self.high_score:
        # If yes, update the high score with the current score
        self.high_score = self.score
        # Open the file in write mode and write the new high score to "data.txt"
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")
    # Reset the current score to 0
    self.score = 0
    self.update_scoreboard()

