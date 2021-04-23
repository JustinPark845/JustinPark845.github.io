from turtle import Turtle, Screen
from score import Score
from math import floor
from food import Food
import time

snake_length = 3
food_exists = 0
snake_previous_location = (0,0)
stamp_id_list = []
stamp_pos_id_list = []

#initialize screen
screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
    
#initialize snake and calibration
snake = Turtle()
snake.shapesize(1.4, 1.4, 1.4)
snake.shape("square")
snake.color("white")
snake.penup()
snake.speed(10)
snake.hideturtle()
snake.home()

#instantiate
score = Score()
food = Food()

#movement functions followed by movement listening prompts
def move_up():
    if snake.heading() != 270:
        snake.setheading(90)
def move_down():
    if snake.heading() != 90:
        snake.setheading(270)
def move_left():
    if snake.heading() != 0:
        snake.setheading(180)
def move_right():
    if snake.heading() != 180:
        snake.setheading(0)

screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

should_reset = False
while should_reset == False:
    #continuous movement
    screen.update()
    snake.forward(30)
    time.sleep(0.1)
    #creating a tail with stamps
    int_distance = int(snake.distance(snake_previous_location))
    if int_distance <= 30.00:
        snake_previous_location = snake.pos()
        new_stamp = snake.stamp()
        stamp_id_list.append(new_stamp)
        stamp_pos_id_list.append(snake_previous_location)

    #if collision, end
    if snake_length > 3:
        for stamps in range(snake_length-1):
            if round(snake.distance(stamp_pos_id_list[stamps]), 0) < 10:
                should_reset = True
    if should_reset == True:
        score.reset()
        score.game_over()

    #if out of bounds, end
    if snake.xcor() < -280 or snake.xcor() > 280 or snake.ycor() < -280 or snake.ycor() > 280:
        should_reset = True
    if should_reset == True:
        score.reset()
        score.game_over()

    #food + growth from eating it
    if food_exists == 0:
        food.random_spawn(stamp_pos_id_list)
        food_exists = 1
    if round(snake.distance(food.food_pos_x,food.food_pos_y), 0) <= 15:
        score.increase_score()
        food.remove_stamp()
        snake_length += 1
        food_exists = 0

    #maintain snake size
    if len(stamp_id_list) > snake_length:
        snake.clearstamp(stamp_id_list[0])
        stamp_pos_id_list.pop(0)
        stamp_id_list.pop(0)

score.highscore_list()
with open("/Users/justinpark/Desktop/Angela_Yu_Coding_Class/snake game/highscores.txt", mode="w") as file:
    file.write("0")


screen.exitonclick()

# Afterthoughts:
# 1: Should have made a seperate module/class for making the snake itself to simplify the code
# 2: On that note, I could have used inheritance on my crafting of the snake body to the food module to
#    further simplify the code