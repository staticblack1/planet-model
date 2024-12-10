
from gravity import Uninversalgravity as U
import math


class SolarSystem:
    def __init__(self):
        self.the_sun = None
        self.planets = []

    def add_planet(self, new_planet):
        self.planets.append(new_planet)

    def add_sun(self, the_sun):
        self.the_sun = the_sun

    def show_planets(self):
        for planet in self.planets:
            print(planet)

    def move_planets(self):
        print(uninversalgravity)

    def move_planets(self):
        dt = .001  # Constant time interval for each solar system iteration.

        for planet in self.planets:
            # Move the distance covered in the interval dt
            planet.move_to(
                planet.get_x_pos() + dt * planet.get_x_vel(),
                planet.get_y_pos() + dt * planet.get_y_vel())

            # After move we need to calculate the new distance from the sun using the distance formula.
            dist_x = self.the_sun.get_x_pos() - planet.get_x_pos()
            dist_y = self.the_sun.get_y_pos() - planet.get_y_pos()
            new_distance = math.sqrt(dist_x**2 + dist_y**2)
            planet.set_distance(new_distance)

            # Let's calculate our new acceleration so we can set our new velocity
            acc_x = U.G * self.the_sun.get_mass()*dist_x/new_distance**3
            acc_y = U.G * self.the_sun.get_mass()*dist_y/new_distance**3

            # Now let's calculate the new x and y velocities and update them for the planet
            planet.set_x_vel(planet.get_x_vel() + dt * acc_x)
            planet.set_y_vel(planet.get_y_vel() + dt * acc_y)
