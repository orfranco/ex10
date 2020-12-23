##############################################################################
# FILE: ship.py
# EXERCISE: intro2cs1 ex10 2020
# DESCRIPTION: A Ship class for an Asteroids game.
##############################################################################

# Constants:
SHIP_START_HEALTH = 3


class Ship:
    """
    This is a class of Ship objects for games.
    """
    RADIUS = 1

    def __init__(self, x: float, y: float, heading: float = 0,
                 speed_x: float = 0, speed_y: float = 0):
        """
        The constructor of the Ship class.
        :param x: the x coordinate of the starting point
        :param y: the y coordinate of the starting point
        :param heading: the heading of the ship when the game starts,
                        initialized to 0 if not given.
        :param speed_x: the speed of the ship on the x-axis.
        :param speed_y: the speed of the ship on the y-axis.
        """
        self.__x, self.__y = x, y
        self.__speed_x, self.__speed_y = speed_x, speed_y
        self.__heading = heading
        self.__health = SHIP_START_HEALTH

    def get_radius(self) -> float:
        """
        this function returns the radius of the ship.
        """
        return self.RADIUS

    def set_heading(self, angle: float):
        """
        this function adds the angle to the heading of the ship.
        :param angle: angle in degrees that needed to be added to the heading.
        """
        self.__heading += angle

    def get_heading(self) -> float:
        """
        :return: the heading of the ship.
        """
        return self.__heading

    def set_x(self, x: float):
        """
        this function update the x coordinate of the ship.
        :param x: the new x coordinate of the ship.
        """
        self.__x = x

    def set_y(self, y: float):
        """
        this function update the y coordinate of the ship.
        :param y: the new y coordinate of the ship.
        """
        self.__y = y

    def get_x(self) -> float:
        """
        this function returns the x coordinate of the ship
        """
        return self.__x

    def get_y(self) -> float:
        """
        this function returns the y coordinate of the ship
        """
        return self.__y

    def get_speed_x(self) -> float:
        """
        :return: the speed of the ship on the x-axis
        """
        return self.__speed_x

    def get_speed_y(self) -> float:
        """
        :return: the speed of the ship on the y-axis
        """
        return self.__speed_y

    def set_speed_x(self, speed_x: float):
        """
        this function update the speed of the ship on the x-axis.
        :param speed_x: the new speed of the ship on the x-axis.
        """
        self.__speed_x = speed_x

    def set_speed_y(self, speed_y: float):
        """
        this function update the speed of the ship on the y-axis.
        :param speed_y: the new speed of the ship on the y-axis.
        """
        self.__speed_y = speed_y

    def get_health(self) -> int:
        """
        :return: the current health of the ship.
        """
        return self.__health

    def take_damage(self, damage: int):
        """
        this function reducing the damage from the current health.
        :param damage: the damage taken by the ship.
        """
        self.__health -= damage
