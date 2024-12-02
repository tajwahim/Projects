COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.make_car()

    def make_car(self):
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(1, 2)
        self.penup()
        self.goto(300, random.randint(-250, 250))

    def move(self):
        self.setx(self.xcor() - STARTING_MOVE_DISTANCE)

    def speedup(self, level):
        move = 10
        move *= level
        self.setx(self.xcor() - move)
