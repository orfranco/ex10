##############################################################################
# FILE: asteroid.py
# EXERCISE: intro2cs1 ex10 2020
# DESCRIPTION: An Asteroid class for an Asteroids game.
##############################################################################
from typing import Any
import math


class Asteroid:
    """
    TODO: add class docstring.
    """
    def __init__(self, x: float, y: float, speed_x: float,
                 speed_y: float, size: int = 3):
        """
        The constructor of the Asteroid class.
        :param x: the x coordinate of the starting point
        :param y: the y coordinate of the starting point
        :param speed_x: the speed of the asteroid on the x-axis.
        :param speed_y: the speed of the asteroid on the y-axis.
        :param size: an int between 1 and 3
        """
        self.__x, self.__y = x, y
        self.__speed_x, self.__speed_y = speed_x, speed_y
        self.__size = size

    def has_intersection(self, obj: Any) -> bool:
        """
        this function checks if the asteroid intersected with the object
        given as an argument.
        :param obj: an object of the game.
        :return: True if the asteroid intersected with the object, False else.
        """
        distance = math.sqrt((obj.get_x() - self.__x)**2
                             + (obj.get_y() - self.__y)**2)
        # finds the distance between the object and the asteroid, and compare
        # it to the sum of their radius
        # (representing the intersection distance)
        return distance <= self.get_radius() + obj.get_radius()

    def get_radius(self) -> int:
        """
        :return: the radius of the asteroid (calculated by the given formula).
        """
        return (self.__size * 10) - 5

    def set_x(self, x: float):
        """
        this function updating the x coordinate of the asteroid.
        :param x: the new x coordinate.
        """
        self.__x = x

    def set_y(self, y: float):
        """
        this function updating the y coordinate of the asteroid.
        :param y: the new y coordinate.
        """
        self.__y = y

    def get_x(self) -> float:
        """
        this function returns the current x coordinate of the asteroid.
        """
        return self.__x

    def get_y(self) -> float:
        """
        this function returns the current y coordinate of the asteroid.
        """
        return self.__y

    def get_speed_x(self) -> float:
        """
        this function returns the current speed of the asteroid on the x-axis.
        """
        return self.__speed_x

    def get_speed_y(self) -> float:
        """
        this function returns the current speed of the asteroid on the y-axis.
        """
        return self.__speed_y

    def get_size(self) -> int:
        """
        this function returns the size of the asteroid.
        """
        return self.__size
