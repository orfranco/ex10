from screen import Screen
from ship import Ship
from asteroid import Asteroid
from torpedo import Torpedo
import sys
import random
import math

DEFAULT_ASTEROIDS_NUM = 5
ROTATE_LEFT = 7
ROTATE_RIGHT = -7


class GameRunner:

    def __init__(self, asteroids_amount):
        self.__screen = Screen()

        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        self.__add_ship()
        # TODO:
        #  - add list(?) of asteroids with length = asteroids_amount
        #       and register each one using
        #       __screen.register_asteroid(asteroid, asteroid_size).
        #  - add user score (as a class variable?)

    def __add_ship(self):
        """
        TODO
        :return:
        """
        ship_x_cord = random.randint(self.__screen_min_x, self.__screen_max_x)
        ship_y_cord = random.randint(self.__screen_min_y, self.__screen_max_y)
        self.ship = Ship(ship_x_cord, ship_y_cord)

    def run(self):
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You should not to change this method!
        self._game_loop()
        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def _game_loop(self):
        self.__ship_handler()

    def __ship_handler(self):
        # move_ship according to keys pressed
        if self.__screen.is_up_pressed():
            self.accelerate_ship()
        if self.__screen.is_left_pressed():
            self.ship.set_heading(ROTATE_LEFT)
        if self.__screen.is_right_pressed():
            self.ship.set_heading(ROTATE_RIGHT)
        self.move_obj(self.ship)
        self.__screen.draw_ship(int(self.ship.get_x()),
                                int(self.ship.get_y()),
                                self.ship.get_heading())

    def accelerate_ship(self):
        """

        :return:
        """
        cos_heading = math.cos(math.radians(self.ship.get_heading()))
        sin_heading = math.sin(math.radians(self.ship.get_heading()))
        new_speed_x = self.ship.get_speed_x() + cos_heading
        new_speed_y = self.ship.get_speed_y() + sin_heading
        self.ship.set_speed_x(new_speed_x)
        self.ship.set_speed_y(new_speed_y)

    def move_obj(self, obj):
        """

        :param obj:
        :return:
        """
        delta_x = self.__screen_max_x - self.__screen_min_x
        new_spot_x = self.__screen_min_x + (obj.get_x() + obj.get_speed_x()
                                            - self.__screen_min_x) % delta_x
        delta_y = self.__screen_max_y - self.__screen_min_y
        new_spot_y = self.__screen_min_y + (obj.get_y() + obj.get_speed_y()
                                            - self.__screen_min_y) % delta_y
        obj.set_x(new_spot_x)
        obj.set_y(new_spot_y)


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
