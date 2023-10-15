from turtle import Turtle


class Paddle(Turtle):
    # Create self
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.size = 5
        self.shapesize(stretch_len=self.size, stretch_wid=1)
        self.penup()
        self.goto(0, -250)

    # Move self
    def go_right(self):
        x = self.xcor()
        x += 20
        if x > 340:
            x = 340
        self.setx(x)

    def go_left(self):
        x = self.xcor()
        x -= 20
        if x < -350:
            x = -350
        self.setx(x)

    def update_size(self):
        self.size -= 1
