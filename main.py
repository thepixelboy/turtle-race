from turtle import Turtle, Screen, color
import random

# Setting up the screen and resizing it
screen = Screen()
screen.setup(width=500, height=400)

# Variables
colors = ["red", "green", "orange", "yellow", "purple", "blue"]
y_positions = [-70, -40, -10, 20, 50, 80]

# Asking the user for a turtle color
usert_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# Calling the function that creates the turtles
for i in range(0, 6):
  turtle = Turtle(shape="turtle")

  turtle.color(colors[i])
  turtle.penup()
  turtle.goto(x=-230, y=y_positions[i])

screen.exitonclick()