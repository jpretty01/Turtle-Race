""" Turtle Race"""
# Import the Turtle items needed
import random
import turtle
from turtle import Turtle, Screen

# Creating the Screen for the game
screen = Screen()

# Creating the screen size
screen.setup(width=500, height=400)

# Taking input on the bet
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# Colors of turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Starting field
y_positions = [-70, -40, -10, 20, 50, 80]

# all turtle array
all_turtles = []

is_race_on = False

# Creating each turtle!
for turtle_index in range (0, 5):
    # Creating our Turtle character and putting it at the starting line
    new_turtle = Turtle(shape="turtle")
    # Different colors on each turtle
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    # taking the y positions and making sure they are at the right positions
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# Dont start until bet is in place
if user_bet:
    is_race_on = True

# While the race is ongoing, move turles!
while is_race_on:

    # Keep moving the turtles forward!
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
