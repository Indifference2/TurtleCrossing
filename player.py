from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.movement_turtle()

    def up(self):
        self.forward(MOVE_DISTANCE)

    def movement_turtle(self):
        self.screen.listen()
        self.screen.onkey(self.up, "Up")

    def check_turtle_cross_the_road(self):
        if self.ycor() == FINISH_LINE_Y:
            return True

    def reset_position(self):
        self.goto(STARTING_POSITION)

