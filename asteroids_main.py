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
TORPEDO_LIFETIME_REDUCER = 1
TORPEDOS_LIMIT = 10

class GameRunner:

    def __init__(self, asteroids_amount):
        self.__screen = Screen()

        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        self._add_ship()
        self._add_asteroids(asteroids_amount)
        self.__torpedos =[]
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
        self._torpedo_handler()
        self._asteroid_handler()

    def _torpedo_handler(self):
        # TODO : leyafyef
        if self.__screen.is_space_pressed() and len(self.__torpedos) < TORPEDOS_LIMIT:
            torpedo_speed_x = self.ship.get_speed_x() + (2 * math.cos(math.radians(self.ship.get_heading())))
            torpedo_speed_y = self.ship.get_speed_y() + (2 * math.sin(math.radians(self.ship.get_heading())))
            torpedo = Torpedo(self.ship.get_x(), self.ship.get_y(), self.ship.get_heading(), torpedo_speed_x, torpedo_speed_y)
            self.__screen.register_torpedo(torpedo)
            self.__torpedos.append(torpedo)

        for torpedo in self.__torpedos:
            self._move_obj(torpedo)
            self.__screen.draw_torpedo(torpedo, torpedo.get_x(),
                                       torpedo.get_y(), torpedo.get_heading())
            torpedo.reduce_life_time(TORPEDO_LIFETIME_REDUCER)
            if not torpedo.get_life_time():
                self.__screen.unregister_torpedo(torpedo)
                self.__torpedos.remove(torpedo)

    def _asteroid_handler(self):
        """
        TODO
        :return:
        """
        for asteroid in self.__asteroids:
            self._move_obj(asteroid)
            self.__screen.draw_asteroid(asteroid, asteroid.get_x(),
                                        asteroid.get_y())
            if asteroid.has_intersection(self.ship):
                self.__screen.show_message(DAMAGE_TITLE, DAMAGE_MESSAGE)
                self.ship.take_damage(ASTEROID_DAMAGE)
                self.__screen.remove_life()
                self.__screen.unregister_asteroid(asteroid)
                self.__asteroids.remove(asteroid)

            for torpedo in self.__torpedos:
                if asteroid.has_intersection(torpedo):
                    self._split_asteroid(asteroid, torpedo)
                    self.__torpedos.remove(torpedo)
                    self.__screen.unregister_torpedo(torpedo)
                    self._increase_usr_points(asteroid.get_size())

    def _increase_usr_points(self, asteroid_size):
        if asteroid_size == 3:
            self.__score += 20
        elif asteroid_size == 2:
            self.__score += 50
        elif asteroid_size == 1:
            self.__score += 100

        self.__screen.set_score(self.__score)

    def _split_asteroid(self, asteroid, torpedo):
        """
        TODO
        :param asteroid:
        :param torpedo:
        :return:
        """
        if asteroid.get_size() > 1:
            new_size = asteroid.get_size() - 1
            new_speed_x_1, new_speed_y_1 = \
                asteroids_speed_after_split(asteroid, torpedo)
            new_speed_x_2 = -1 * new_speed_x_1
            new_speed_y_2 = -1 * new_speed_y_1

            new_ast_1 = Asteroid(asteroid.get_x(), asteroid.get_y(), new_speed_x_1, new_speed_y_1, size=new_size)
            new_ast_2 = Asteroid(asteroid.get_x(), asteroid.get_y(), new_speed_x_2, new_speed_y_2, size=new_size)
            self.__asteroids += [new_ast_1, new_ast_2]
            self.__screen.register_asteroid(new_ast_1, new_ast_1.get_size())
            self.__screen.register_asteroid(new_ast_2, new_ast_2.get_size())

            self.__screen.unregister_asteroid(asteroid)
            self.__asteroids.remove(asteroid)

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

        # check if the ship life is 0:
        if not self.ship.get_health():
            pass  # TODO

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


def asteroids_speed_after_split(asteroid, torpedo):
    """
    TODO
    :param asteroid:
    :param torpedo:
    :return:
    """
    old_speed_x, old_speed_y = asteroid.get_speed_x(), asteroid.get_speed_y()
    old_speeds_root = math.sqrt((old_speed_x ** 2) + (old_speed_y ** 2))
    new_speed_x = (torpedo.get_speed_x() + old_speed_x) / old_speeds_root
    new_speed_y = (torpedo.get_speed_y() + old_speed_y) / old_speeds_root

    return new_speed_x, new_speed_y


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
