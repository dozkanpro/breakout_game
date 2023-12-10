from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard
import time

paddle = Paddle()
ball = Ball()
bricks = Brick("black", 1000, 1000).create_bricks()
scoreboard = Scoreboard()

ball_speed_increase = [4, 12, 16]

# Create Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.tracer(0)

screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

while scoreboard.turns > 0:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with side walls
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.bounce_x()

    # detect collision with upper wall
    if ball.ycor() > 290:
        ball.bounce_y()
        paddle.update_size()

    # detect collision with paddle
    if (ball.ycor() > -240) and (ball.ycor() < -210) and (
            paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.bounce_y()

    # Detect paddle miss the ball
    if ball.ycor() < -290:
        ball.reset_position()
        scoreboard.decrease_turn()

    # detect collision with brick
    for brick in bricks:
        if brick.distance(ball) < 20:
            brick.goto(1000, 1000)
            bricks.remove(brick)
            scoreboard.increase_score(brick.color()[0])

            if len(bricks) == 0:
                scoreboard.game_over("You Win!")

            if ball.current_speed_increase < len(ball_speed_increase) and scoreboard.score >= ball_speed_increase[ball.current_speed_increase]:
                ball.increase_ball_speed()

screen.exitonclick()
