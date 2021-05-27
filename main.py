from turtle import Turtle, Screen, color, turtles
import random

# Setting up the screen and resizing it
screen = Screen()
screen.title("Welcome to the turtle race!")
screen.setup(width=500, height=400)


# Variables
colors = ["red", "green", "orange", "yellow", "purple", "blue"]
y_positions = [-70, -40, -10, 20, 50, 80]
is_race_on = False
all_turtles = []

# Asking the user for a turtle color
usert_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# Calling the function that creates the turtles
for i in range(0, 6):
  turtle = Turtle(shape="turtle")

  turtle.color(colors[i])
  turtle.penup()
  turtle.goto(x=-230, y=y_positions[i])
  all_turtles.append(turtle)

if usert_bet:
  is_race_on = True

while is_race_on:
  for turtle in all_turtles:
    if turtle.xcor() > 230:
      is_race_on = False
      winner = turtle.pencolor()
      if usert_bet.lower() == winner:
        print(f"You've won! The {winner} turtle is the winner. Congratulations 👏")
      else:
        print(f"You've lost 😭 The {winner} turtle is the winner.")

    distance = random.randint(0, 10)
    turtle.forward(distance)


screen.exitonclick()