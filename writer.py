from turtle import Turtle

class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def writer(self, x, y, state):
        self.goto(x, y)
        self.write(f"{state}", align="center", font=("Arial", 8, "bold"))