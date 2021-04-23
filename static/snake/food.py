from turtle import Turtle, Screen
from math import floor
import random

class Food:
    def __init__(self):
        self.turtle = Turtle()
        self.color = self.turtle.color("red")
        self.state = self.turtle.hideturtle()
        self.pen = self.turtle.penup()
        self.shape = self.turtle.shape("square")
        self.size = self.turtle.turtlesize(.5, .5, .5)
        self.food_pos_x = 0
        self.food_pos_y = 0
        self.stamp_id = []

    def random_spawn(self, occupied_coordinates):
        x_cord = random.randint(-9,9)*30
        y_cord = random.randint(-9,9)*30

        #this was code intended to prevent the food from spawning on top of the snake
        #it does not work
        while (x_cord, y_cord) in occupied_coordinates:
            x_cord = random.randint(-9,9)*30
            y_cord = random.randint(-9,9)*30
            
        self.food_pos_x = x_cord
        self.food_pos_y = y_cord
        self.turtle.setposition(x_cord, y_cord)
        food_stamp = self.turtle.stamp()
        self.stamp_id.append(food_stamp)

    def remove_stamp(self):
        self.turtle.clearstamp(self.stamp_id[0])
        self.stamp_id.pop(0)
