from screen import Screen
import sys

DEFAULT_ASTEROIDS_NUM = 5


class GameRunner:

    def __init__(self, asteroids_amount):
        self.__screen = Screen()

        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        # TODO:
        #  - add list(?) of asteroids with length = asteroids_amount
        #       and register each one using
        #       __screen.register_asteroid(asteroid, asteroid_size).
        #  - initialize ship with random coords
        #       and draw it using __screen.draw_ship(x,y,heading).
        #  - add user score (as a class variable?)

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
        # TODO: Your code goes here
        pass

    def move_obj(self, obj):
        delta_x = self.__screen_max_x - self.__screen_min_x
        new_spot_x = self.__screen_min_x + (obj.get_x() + obj.get_speed_x()
                                            - self.__screen_min_x) % delta_x
        delta_y = self.__screen_max_y - self.__screen_min_y
        new_spot_y = self.__screen_min_y + (obj.get_y() + obj.get_speed_y()
                                            - self.__screen_min_y) % delta_y

        obj.set_x = new_spot_x
        obj.set_y = new_spot_y

def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
