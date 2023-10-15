from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.turns = 3
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 270)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 16, "normal"))
        self.goto(100, 270)
        self.write(f"Turns: {self.turns}", align="center", font=("Courier", 16, "normal"))

    def increase_score(self, color):
        points = 0
        if color == "yellow":
            points = 1
        elif color == "green":
            points = 3
        elif color == "orange":
            points = 5
        elif color == "red":
            points = 7
        self.score += points
        self.update_scoreboard()

    def decrease_turn(self):
        self.turns -= 1
        self.update_scoreboard()
        if self.turns == 0:
            message = "Game Over"
            self.game_over(message)

    def game_over(self, message):
        self.goto(0, 0)
        self.write(message, align="center", font=("Courier", 20, "normal"))
