

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
        # TODO: do
        pass

    def get_radius(self):
        """
        TODO
        :return:
        """
        return (self.size * 10) - 5
