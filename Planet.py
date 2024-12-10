from turtle import Turtle


class Planet:
    def __init__(self, name: str, mass: float,vel_x: float, vel_y: float, x: float, y: float =0.0, color: str= "red"):
        self.name = name
        self.mass = mass
        self.distance = x
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.t = Turtle()
        self.t.shape('circle')
        self.color = color
        self.t.color(self.color)
        self.t. penup()
        self.t.goto(self.x, self.y)
        self.t.pendown()
        self.t.speed(5)


    def get_mass(self):
        return self.mass

    def get_distance(self):
        return self.distance


    def set_distance(self, distance):
        self.distance= distance


    def get_x_pos(self):
        return self.x

    def get_x_vel(self):
        return self.vel_x

    def get_y_pos(self):
        return self.y

    def get_y_vel(self):
        return self.vel_y

    def set_x_vel(self, new_x_vel):
        self.vel_x = new_x_vel

    def set_y_vel(self, new_y_vel):
        self.vel_y = new_y_vel

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.t.goto(new_x,new_y)


    def __str__(self):
        return f"Planet(name={self.name}, mass={self.mass}, distance={self.distance}, x={self.x}, y={self.y}, vel_x={self.vel_x}, vel_y={self.vel_y})"


