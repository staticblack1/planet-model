
from lab week 14 import point

class Rectangle:
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner

    def translate(self, dx, dy):
        self.corner.translate(dx, dy)

    def grow(self, dwidth, dheight):
        self.width += dwidth
        self.height += dheight

        # Example of using the classes

    sun = Sun(coordinate=(0.0, 0.0), mass=1.989e30, size=1.0)  # Sun with mass similar to real life
    planet1 = Planet(position=(10.0, 0.0), mass=5.97e24, size=0.1, velocity=(0.0, 1.0))
    planet2 = Planet(position=(20.0, 0.0), mass=4.87e24, size=0.08, velocity=(0.0, 0.5))

    # Create a simulation and add planets
    simulation = Simulation()
    simulation.add_planet(sun)  # Add Sun first to the solar system
    simulation.add_planet(planet1)
    simulation.add_planet(planet2)

    # Run simulation for a few steps
    simulation.run(steps=5)

    # Get positions of planets after the simulation
    print("Planet 1 position:", simulation.get_planet_location(planet1))
    print("Planet 2 position:", simulation.get_planet_location(planet2))

    # Calculate the distance from the planets to the Sun
    print("Distance from Planet 1 to Sun:", simulation.planet_distance_from_sun(planet1))
    print("Distance from Planet 2 to Sun:", simulation.planet_distance_from_sun(planet2))