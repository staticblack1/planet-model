from turtle import Turtle




class Sun:
    def __init__(self, name, radius, mass, temp, x= 0.0, y=0.0):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.temp = temp
        self.x = x
        self.y = y
        self.t = Turtle()
        self.t.shape('circle')
        self.t.color('yellow')
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.t.pendown()

    def get_mass(self):
        return self.mass

    def get_x_pos(self):
        return self.x

    def get_y_pos(self):
        return self.y

    def __str__(self):
        return f"Sun(name={self.name}, radius={self.radius}, mass={self.mass}, temp={self.temp}, x={self.x}, y={self.y})"

