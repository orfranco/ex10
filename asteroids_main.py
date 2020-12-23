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
ASTEROID_ALLOWED_SPEEDS = (-4, -3, -2, -1, 1, 2, 3, 4)
ASTEROID_DAMAGE = 1
DAMAGE_MESSAGE = "Ouch !!"
DAMAGE_TITLE = "Damage"


class GameRunner:

    def __init__(self, asteroids_amount):
        self.__screen = Screen()

        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        self._add_ship()
        self._add_asteroids(asteroids_amount)
        self.__score = 0

    def _add_asteroids(self, asteroids_amount):
        """
        TODO
        :param asteroids_amount:
        :return:
        """
        self.__asteroids = []
        for i in range(asteroids_amount):
            ast_x = random.randint(self.__screen_min_x, self.__screen_max_x)
            ast_y = random.randint(self.__screen_min_y, self.__screen_max_y)
            ast_speed_x = random.choice(ASTEROID_ALLOWED_SPEEDS)
            ast_speed_y = random.choice(ASTEROID_ALLOWED_SPEEDS)
            asteroid = Asteroid(ast_x, ast_y, ast_speed_x, ast_speed_y)
            self.__asteroids.append(asteroid)
            self.__screen.register_asteroid(asteroid, asteroid.get_size())

    def _add_ship(self):
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
        self._ship_handler()
        self._asteroid_handler()

    def _asteroid_handler(self):
        for asteroid in self.__asteroids:
            self._move_obj(asteroid)
            self.__screen.draw_asteroid(asteroid, asteroid.get_x(), asteroid.get_y())
            if asteroid.has_intersection(self.ship):
                self.__screen.show_message(DAMAGE_TITLE, DAMAGE_MESSAGE)
                self.ship.take_damage(ASTEROID_DAMAGE)
                self.__screen.remove_life()
                self.__screen.unregister_asteroid(asteroid)
                self.__asteroids.remove(asteroid)

        if not self.ship.get_health():
            pass  # TODO

    def _ship_handler(self):
        """

        :return:
        """
        # move_ship according to keys pressed
        if self.__screen.is_up_pressed():
            self._accelerate_ship()
        if self.__screen.is_left_pressed():
            self.ship.set_heading(ROTATE_LEFT)
        if self.__screen.is_right_pressed():
            self.ship.set_heading(ROTATE_RIGHT)
        self._move_obj(self.ship)
        self.__screen.draw_ship(int(self.ship.get_x()),
                                int(self.ship.get_y()),
                                self.ship.get_heading())

    def _accelerate_ship(self):
        """

        :return:
        """
        cos_heading = math.cos(math.radians(self.ship.get_heading()))
        sin_heading = math.sin(math.radians(self.ship.get_heading()))
        new_speed_x = self.ship.get_speed_x() + cos_heading
        new_speed_y = self.ship.get_speed_y() + sin_heading
        self.ship.set_speed_x(new_speed_x)
        self.ship.set_speed_y(new_speed_y)

    def _move_obj(self, obj):
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
