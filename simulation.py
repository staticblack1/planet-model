import turtle

from solarsystem import SolarSystem
from jupyturtle import Turtle
class Simulation:
    def __init__(self, solar_system, width, height, num_periods):
        self.solar_system = solar_system
        self.width = width
        self.height = height
        self.num_periods = num_periods
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.screen = turtle.Screen()
        self.screen.setup(width= self.width, height=self.height)
        self.t.clear()

    def run(self):
        self.solar_system.show_planets()
        for _ in range(self.num_periods):
            self.solar_system.move_planets()
            self.solar_system.show_planets()


