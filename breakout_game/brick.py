from turtle import Turtle


class Brick(Turtle):
    def __init__(self, color, x, y):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.goto(x, y)

    def create_bricks(self):
        bricks = []
        colors = ["red", "red", "orange", "orange", "green", "green", "yellow", "yellow"]
        y = 250

        for i in range(8):
            brick_color = colors[i]
            x = -350
            for _ in range(10):
                brick = Brick(brick_color, x, y)
                bricks.append(brick)
                x += 70
            y -= 30

        return bricks

