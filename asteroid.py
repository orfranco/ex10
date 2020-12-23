
import math

class Asteroid:
    def __init__(self, x, y, speed_x, speed_y, size=3):
        """
        The constructor of the Asteroid class.
        TODO: finish
        :param x:
        :param y:
        :param size: an int between 1 and 3
        :param speed_x:
        :param speed_y:
        """
        self.x, self.y = x, y
        self.speed_x, self.speed_y = speed_x, speed_y
        self.size = size

    def has_intersection(self, obj):
        distance = math.sqrt((obj.get_x() - self.x)**2 +
                             (obj.get_y() - self.y)**2)

        return distance <= self.get_radius() + obj.get_radius()
    def get_radius(self):
        """
        TODO
        :return:
        """
        return (self.size * 10) - 5

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
