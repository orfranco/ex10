
TORPEDO_START_LIFE = 200


class Torpedo:
    """
    TODO: add class docstring.
    """
    RADIUS = 4

    def __init__(self, x: float, y: float, heading: float,
                 speed_x: float, speed_y: float):
        """
        The constructor of the Torpedo class.
        :param x: the x coordinate of the starting point
        :param y: the y coordinate of the starting point
        :param heading: the heading of the torpedo.
        :param speed_x: the speed of the torpedo on the x-axis.
        :param speed_y: the speed of the torpedo on the y-axis.
        """
        self.x, self.y = x, y
        self.speed_x, self.speed_y = speed_x, speed_y
        self.heading = heading
        self.life_time = TORPEDO_START_LIFE

    def get_radius(self) -> int:
        # TODO: erase and update uses in main.
        return self.RADIUS

    def set_x(self, x: float):
        """
        this function update the x coordinate of the torpedo.
        :param x: the new x coordinate.
        """
        self.x = x

    def set_y(self, y: float):
        """
        this function update the y coordinate of the torpedo.
        :param y: the new y coordinate.
        """
        self.y = y

    def get_x(self) -> float:
        """
        this function returns the current x coordinate of the torpedo.
        """
        return self.x

    def get_y(self) -> float:
        """
        this functions returns the current y coordinate of the torpedo.
        """
        return self.y

    def get_speed_x(self) -> float:
        """
        :return: the speed of the torpedo on the x-axis
        """
        return self.speed_x

    def get_speed_y(self) -> float:
        """
        :return: the speed of the torpedo on the y-axis
        """
        return self.speed_y

    def get_heading(self) -> float:
        """
        :return: the heading of the torpedo.
        """
        return self.heading

    def get_life_time(self) -> int:
        """
        this function returns the current life time of the torpedo.
        """
        return self.life_time

    def reduce_life_time(self, amount: int):
        """
        this function reduces the life time of the torpedo by the amount given.
        :param amount: the amount of life to reduce.
        """
        self.life_time -= amount