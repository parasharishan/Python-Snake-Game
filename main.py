from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

game_is_on = True
snake = Snake()
food = Food()
score_board = Scoreboard()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
score = 0
while game_is_on:
    screen.update()
    time.sleep(0.1333333332)
    snake.move()
    score_board.update_scoreboard(score)
    # Detect collisions
    if snake.head.distance(food) < (food.shapesize()[0]) * 30:
        score += food.score
        food.refresh()
        snake.elongate()

    if snake.head.xcor() < -300 or snake.head.xcor() > 298 or snake.head.ycor() > 298 or snake.head.ycor() < -298:
        game_is_on = False

    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False

score_board.final_score(current_score=score)
screen.exitonclick()
