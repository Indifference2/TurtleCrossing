from turtle import Turtle
import random
### CONSTANST ###
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_car = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Create a car on a random position"""
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.turtlesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_car.append(new_car)

    def move_car(self):
        for car in self.all_car:
            car.backward(self.move_speed)

    def check_car_collision_with_turtle(self, Player):
        for car in self.all_car:
            if car.distance(Player) < 20:
                return True

    def increase_speed(self):
        """Increase cars speed each the Turtle cross the road"""
        self.move_speed += MOVE_INCREMENT
