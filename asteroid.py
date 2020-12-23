
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
        self.__x, self.__y = x, y
        self.__speed_x, self.__speed_y = speed_x, speed_y
        self.__size = size

    def has_intersection(self, obj):
        distance = math.sqrt((obj.get_x() - self.__x)**2 +
                             (obj.get_y() - self.__y)**2)

        return distance <= self.get_radius() + obj.get_radius()

    def get_radius(self):
        """
        TODO
        :return:
        """
        return (self.__size * 10) - 5

    def set_x(self, x):
        """

        :param x:
        :return:
        """
        self.__x = x

    def set_y(self, y):
        """

        :param y:
        :return:
        """
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_speed_x(self):
        return self.__speed_x

    def get_speed_y(self):
        return self.__speed_y

    def get_size(self):
        return self.__size
