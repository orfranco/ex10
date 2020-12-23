
TORPEDO_START_LIFE = 200

class Torpedo:
    RADIUS = 4

    def __init__(self, x, y, heading, speed_x, speed_y):
        """
        The constructor of the Torpedo class.
        TODO: finish
        :param x:
        :param y:
        :param heading:
        :param speed_x:
        :param speed_y:
        """
        self.x, self.y = x, y
        self.speed_x, self.speed_y = speed_x, speed_y
        self.heading = heading
        self.life_time = TORPEDO_START_LIFE

    def get_radius(self):
        return self.RADIUS

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_speed_x(self):
        return self.speed_x

    def get_speed_y(self):
        return self.speed_y

    def get_heading(self):
        return self.heading

    def get_life_time(self):
        return self.life_time

    def reduce_life_time(self, amount):
        self.life_time -= amount