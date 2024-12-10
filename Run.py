from sun import Sun
from Planet import Planet
from solarsystem import SolarSystem
from simulation import Simulation

if __name__ == '__main__':
    solar_system = SolarSystem()

    the_sun = Sun("SOL", 5000, 10000000, 5800, )
    solar_system.add_sun(the_sun)

    earth = Planet("EARTH", 1, 5.0, 600, 31,0,"green")
    #earth = Planet( "Earth",47.5,1, 25, 5.0, 2000)
    solar_system.add_planet(earth)

    mars = Planet("MARS", .1, 10.0, 400, 62, 0,"red")
    #mars = Planet("MARS", 40.5, .1, 62, 10.0, 125.0,)
    solar_system.add_planet(mars)

    Venus = Planet("Venus", .05, 16.0, 311,93, 0, "blue")
    solar_system.add_planet(Venus)

    Pluto = Planet("Pluto", .02,18.0,350,200,0,"black")
    solar_system.add_planet(Pluto)

    simulation = Simulation(solar_system, 500,500, 2000)
    simulation.run()