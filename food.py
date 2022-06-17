from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
SHAPE_SIZES = [0.5, 0.75, 1.00]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.get_random_shapesize()
        self.get_random_color()
        self.speed("fastest")
        self.refresh()

    def get_random_shapesize(self):
        shapesize = random.choice(SHAPE_SIZES)
        self.shapesize(stretch_len=shapesize, stretch_wid=shapesize)

    def get_random_color(self):
        self.color(random.choice(COLORS))

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.get_random_color()
        self.get_random_shapesize()
        self.goto(random_x, random_y)
