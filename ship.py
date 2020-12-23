
SHIP_START_HEALTH = 3


class Ship:
    RADIUS = 1

    def __init__(self, x, y, heading=0, speed_x=0, speed_y=0):
        """
        The constructor of the Ship class.
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
        self.health = SHIP_START_HEALTH

    def get_radius(self):
        """
        :return: The radius of the ship.
        """
        return self.RADIUS

    def set_acceleration(self):
        """
        TODO: write
        :return:
        """
        pass

    def set_heading(self, angle):
        """
        TODO ?
        :return:
        """
        # TODO: add validation using exceptions
        self.heading += angle

    def get_heading(self):
        return self.heading

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

    def set_speed_x(self, speed_x):
        """
        TODO
        :param speed_x:
        :return:
        """
        self.speed_x = speed_x

    def set_speed_y(self, speed_y):
        """
        TODO
        :param speed_y:
        :return:
        """
        self.speed_y = speed_y

    def get_health(self):
        """
        TODO
        :return:
        """
        return self.health

    def take_damage(self, damage):
        """

        :return:
        """
        self.health -= damage
