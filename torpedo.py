

class Torpedo:
    RADIUS = 4
    TORPEDO_LIFE = 200

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