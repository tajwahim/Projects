FONT = ("Courier", 17, "bold")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.ht()
        self.goto(-280, 250)
        self.display_level()

    def display_level(self):
        self.write(f"level: {self.level}", font=FONT)

    def over(self):
        s = Turtle()
        s.home()
        s.pu()
        s.ht()
        s.write("Game Over", align="center", font=FONT)
