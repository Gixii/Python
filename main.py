# Import necessary modules from the Turtle graphics library
from turtle import Screen
import time

# Import classes from separate files (snake.py, food.py, scoreboard.py)
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Set up the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turn off automatic screen updates

# Create instances of Snake, Food, and Scoreboard classes
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Set up event listeners for arrow key presses to control the snake's movement
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Variable to control the game loop
is_game_on = True

# Main game loop
while is_game_on:
    screen.update()  # Update the screen manually

    # Introduce a slight delay to control the speed of the snake
    time.sleep(0.1)

    snake.move()  # Move the snake based on its current direction

    # Detect collisions with food
    if snake.head.distance(food) < 15:
        food.refresh()  # Move the food to a new random location
        scoreboard.increase_score()  # Increase the player's score
        snake.extend()  # Extend the length of the snake

    # Detect collisions with the screen boundaries
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        scoreboard.reset()  # Reset the score
        snake.reset()  # Reset the snake to its initial state

    # Detect collisions with the snake's own tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()  # Reset the score
            snake.reset()  # Reset the snake to its initial state

# The game loop will continue running until the user clicks on the game window to exit
screen.exitonclick()
