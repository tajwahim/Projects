from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(500, 400)
bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "green", "yellow", "blue", "purple"]
all_turtles = []


tim = Turtle()
tim.shape("turtle")
tim.color(colors[0])
tim.penup()
tim.goto(-230, -100)
all_turtles.append(tim)

tom = Turtle()
tom.shape("turtle")
tom.color(colors[1])
tom.penup()
tom.goto(-230, -60)
all_turtles.append(tom)

bob = Turtle()
bob.shape("turtle")
bob.color(colors[2])
bob.penup()
bob.goto(-230, -20)
all_turtles.append(bob)

bill = Turtle()
bill.shape("turtle")
bill.color(colors[3])
bill.penup()
bill.goto(-230, 20)
all_turtles.append(bill)

jerry = Turtle()
jerry.shape("turtle")
jerry.color(colors[4])
jerry.penup()
jerry.goto(-230, 60)
all_turtles.append(jerry)

barry = Turtle()
barry.shape("turtle")
barry.color(colors[5])
barry.penup()
barry.goto(-230, 100)
all_turtles.append(barry)


if bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        distance = random.randint(0, 10)
        turtle.forward(distance)


screen.exitonclick()
