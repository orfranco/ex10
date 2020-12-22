

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

    def get_radius(self):
        """
        :return: The radius of the ship (=1).
        """
        return self.RADIUS

    def set_acceleration(self):
        """
        TODO: write
        :return:
        """
        pass

    def set_heading(self):
        """
        TODO ?
        :return:
        """
        pass
