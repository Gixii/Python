# Import necessary modules for the game
from turtle import Screen
import time
from snake import Snake  # Import the Snake class from a separate file
from food import Food  # Import the Food class from a separate file
from scoreboard import Scoreboard  # Import the Scoreboard class from a separate file

# Create the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turn off animation

# Initialize game elements: snake, food, scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen for user keyboard inputs for controlling the snake
screen.listen()
screen.onkey(snake.up, "Up")  # Bind 'up' key to move up
screen.onkey(snake.down, "Down")  # Bind 'down' key to move down
screen.onkey(snake.left, "Left")  # Bind 'left' key to move left
screen.onkey(snake.right, "Right")  # Bind 'right' key to move right

# Set up the game loop
is_game_on = True
while is_game_on:
    screen.update()  # Update the screen
    time.sleep(0.1)  # Pause for a short time to control the speed of the game
    snake.move()  # Move the snake

    # Check if the snake has collided with the food
    if snake.head.distance(food) < 15:
        food.refresh()  # Move the food to a new random location
        scoreboard.increase_score()  # Increase the score
        snake.extend()  # Extend the length of the snake

    # Check if the snake has hit the walls
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        is_game_on = False  # End the game if the snake hits the walls
        scoreboard.game_over()  # Display game over message

    # Check if the snake has collided with its own tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False  # End the game if the snake collides with itself
            scoreboard.game_over()  # Display game over message

# Exit the game when the user clicks on the screen
screen.exitonclick()
