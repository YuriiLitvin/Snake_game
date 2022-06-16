from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

start_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for position in start_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    # new_segment.speed("slowest")
    new_segment.goto(position)
    segments.append(new_segment)

segments[0].color("red")
segments[1].color("green")
segments[2].color("blue")


# def turn_left():
#     segments[0].left(90)


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    for index in range(len(segments) - 1, 0, -1):
        pos = segments[index - 1].position()
        segments[index].goto(pos)
    segments[0].forward(20)

# screen.listen()
# screen.onkey(turn_left, "a")


screen.exitonclick()
