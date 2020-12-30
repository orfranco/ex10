##############################################################################
# FILE: asteroids_main.py
# EXERCISE: intro2cs1 ex10 2020
# DESCRIPTION: The main module for an Asteroids game.
##############################################################################
from screen import Screen
from ship import Ship
from asteroid import Asteroid
from torpedo import Torpedo
from typing import List, Tuple, Any
import sys
import random
import math

# Constants:
DEFAULT_ASTEROIDS_NUM = 5
ROTATE_LEFT = 7
ROTATE_RIGHT = -7
ASTEROID_ALLOWED_SPEEDS = (-4, -3, -2, -1, 1, 2, 3, 4)
ASTEROID_DAMAGE = 1
DAMAGE_MESSAGE = "Ouch !!"
DAMAGE_TITLE = "Damage"
TORPEDO_LIFETIME_REDUCER = 1
TORPEDOS_LIMIT = 10
SHIP_WRECKED_MSG = "You are dead!!"
VICTORY_MSG = "You have Won!"
QUIT_PRESSED_MSG = "Quitting is for quitters..."
END_TITLE = "BYE"


class GameRunner:
    """
    The class runs the game 'Asteroids'.
    Uses the following classes: Ship(), Asteroid(), Torpedo(), and Screen().
    """
    def __init__(self, asteroids_amount: int):
        """
        The constructor of the GameRunner class.
        :param asteroids_amount: The amount of asteroids to initialize.
        """
        self.__screen = Screen()

        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        self._add_ship()
        self._add_asteroids(asteroids_amount)
        self.__torpedos = []
        self.__score = 0

    def _add_asteroids(self, asteroids_amount: int):
        """
        This method adds Asteroid objects to the game.
        :param asteroids_amount: The amount of asteroids to be added.
        :return: None
        """
        self.__asteroids: List[Asteroid] = []

        for i in range(asteroids_amount):
            # Generate random location and speed:
            ast_x = random.randint(self.__screen_min_x, self.__screen_max_x)
            ast_y = random.randint(self.__screen_min_y, self.__screen_max_y)
            ast_speed_x = random.choice(ASTEROID_ALLOWED_SPEEDS)
            ast_speed_y = random.choice(ASTEROID_ALLOWED_SPEEDS)

            # Create the asteroid and add it to the game:
            asteroid = Asteroid(ast_x, ast_y, ast_speed_x, ast_speed_y)
            #  make sure the asteroid won't intersect with the ship on the
            #  start of the game:
            while asteroid.has_intersection(self.ship):
                ast_x = random.randint(self.__screen_min_x,
                                       self.__screen_max_x)
                ast_y = random.randint(self.__screen_min_y,
                                       self.__screen_max_y)
                asteroid.set_x(ast_x)
                asteroid.set_y(ast_y)
            self.__asteroids.append(asteroid)

            # Register the asteroid to the screen:
            self.__screen.register_asteroid(asteroid, asteroid.get_size())

    def _add_ship(self):
        """
        This method creates a Ship object and adds it to the game.
        :return: None
        """
        # Generate random location:
        ship_x_cord = random.randint(self.__screen_min_x, self.__screen_max_x)
        ship_y_cord = random.randint(self.__screen_min_y, self.__screen_max_y)
        # Create and add the ship:
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
        """
        This function manages the iterations of the game.
        :return: None
        """
        self._ship_handler()
        self._torpedo_handler()
        self._asteroid_handler()
        self._is_game_over()

    def _is_game_over(self):
        """
        This function checks if the game should be ended.
        If so - ends the game and prints an suitable message to the screen.
        :return: None
        """
        game_over: bool = False

        # Check if the ship life is 0:
        if not self.ship.get_health():
            game_over = True
            msg: str = SHIP_WRECKED_MSG

        # Check if the asteroids were all destroyed:
        elif not self.__asteroids:
            game_over = True
            msg: str = VICTORY_MSG

        # Check if the user wants to quit the game:
        elif self.__screen.should_end():
            game_over = True
            msg: str = QUIT_PRESSED_MSG
        
        if game_over:
            self.__screen.show_message(END_TITLE, msg)
            self.__screen.end_game()
            sys.exit()

    def _torpedo_handler(self):
        """
        This function handles everything that has to do with the torpedos
        in the game:
        - Creates a torpedo if the space button was pressed.
        - Moves the torpedos in every iteration of the game.
        - Removes torpedos after their lifetime is over (torpedo.__life_time)
        :return: None
        """
        if self.__screen.is_space_pressed() and \
                len(self.__torpedos) < TORPEDOS_LIMIT:

            # Create a torpedo and add it to the game:
            torpedo_speed_x, torpedo_speed_y = self.calc_torpedo_speeds()
            torpedo = Torpedo(self.ship.get_x(), self.ship.get_y(),
                              self.ship.get_heading(),
                              torpedo_speed_x, torpedo_speed_y)
            self.__torpedos.append(torpedo)

            # Register the torpedo to the screen:
            self.__screen.register_torpedo(torpedo)

        # Handle every torpedo currently in the game:
        for torpedo in self.__torpedos:
            self._move_obj(torpedo)
            self.__screen.draw_torpedo(torpedo, int(torpedo.get_x()),
                                       int(torpedo.get_y()),
                                       torpedo.get_heading())
            torpedo.reduce_life_time(TORPEDO_LIFETIME_REDUCER)

            # Remove torpedos after their lifetime is over:
            if not torpedo.get_life_time():
                self.__screen.unregister_torpedo(torpedo)
                self.__torpedos.remove(torpedo)

    def calc_torpedo_speeds(self) -> Tuple[float, float]:
        """
        This method calculates the speed of the torpedo in both axis,
        according to the speed and orientation of the ship.
        :return: None
        """
        cos_heading: float = math.cos(math.radians(self.ship.get_heading()))
        sin_heading: float = math.sin(math.radians(self.ship.get_heading()))

        speed_x: float = self.ship.get_speed_x() + (2 * cos_heading)
        speed_y: float = self.ship.get_speed_y() + (2 * sin_heading)

        return speed_x, speed_y

    def _asteroid_handler(self):
        """
        This function handles everything that has to do with the asteroids in
        the game:
        - Moves the asteroids in every iteration of the game.
        - Handles intersection of the asteroids with the ship or with torpedos.
        :return:
        """
        for asteroid in self.__asteroids:
            self._move_obj(asteroid)
            self.__screen.draw_asteroid(asteroid, int(asteroid.get_x()),
                                        int(asteroid.get_y()))

            # In case the asteroid was hit by the ship:
            if asteroid.has_intersection(self.ship):
                self.__screen.show_message(DAMAGE_TITLE, DAMAGE_MESSAGE)
                self.__screen.remove_life()
                self.__screen.unregister_asteroid(asteroid)
                self.ship.take_damage(ASTEROID_DAMAGE)
                self.__asteroids.remove(asteroid)

            for torpedo in self.__torpedos:
                # In case the asteroid was hit by a torpedo:
                if asteroid.has_intersection(torpedo):
                    self._split_asteroid(asteroid, torpedo)
                    self.__torpedos.remove(torpedo)
                    self._increase_usr_points(asteroid.get_size())
                    self.__screen.unregister_torpedo(torpedo)

    def _increase_usr_points(self, asteroid_size: int):
        """
        Adds points to the overall score of the player according to the size
        of the asteroid that he has destroyed.
        :param asteroid_size: The size of the asteroid that was destroyed.
        :return: None
        """
        if asteroid_size == 3:
            self.__score += 20

        elif asteroid_size == 2:
            self.__score += 50

        elif asteroid_size == 1:
            self.__score += 100

        # Update the score on the screen:
        self.__screen.set_score(self.__score)

    def _split_asteroid(self, asteroid: Asteroid, torpedo: Torpedo):
        """
        This method splits the given asteroid that was hit by the given torpedo
        into 2 smaller asteroids.
        If the asteroid is as small as it can get - will remove it.
        :param asteroid: The asteroid that was hit.
        :param torpedo: The torpedo which hit the asteroid.
        :return: None
        """
        # If the asteroid is big enough to split:
        if asteroid.get_size() > 1:
            new_size = asteroid.get_size() - 1
            # Get the speed for the first smaller asteroid:
            new_speed_x_1, new_speed_y_1 = \
                asteroids_speed_after_split(asteroid, torpedo)

            # Use the opposite speed for the second smaller asteroid:
            new_speed_x_2 = -1 * new_speed_x_1
            new_speed_y_2 = -1 * new_speed_y_1

            # Create the new asteroids:
            new_ast_1 = Asteroid(asteroid.get_x(), asteroid.get_y(),
                                 new_speed_x_1, new_speed_y_1, size=new_size)
            new_ast_2 = Asteroid(asteroid.get_x(), asteroid.get_y(),
                                 new_speed_x_2, new_speed_y_2, size=new_size)
            self.__asteroids += [new_ast_1, new_ast_2]
            self.__screen.register_asteroid(new_ast_1, new_ast_1.get_size())
            self.__screen.register_asteroid(new_ast_2, new_ast_2.get_size())

        # Remove the original asteroid:
        self.__screen.unregister_asteroid(asteroid)
        self.__asteroids.remove(asteroid)

    def _ship_handler(self):
        """
        This function moves (accelerates and rotates) the ship
        according to the user key strokes.
        """
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
        this function accelerates the speed of the ship on the current
        direction with the given formula.
        """
        # calculating the new x-axis speed and the y-axis coordinate:
        cos_heading = math.cos(math.radians(self.ship.get_heading()))
        sin_heading = math.sin(math.radians(self.ship.get_heading()))
        new_speed_x = self.ship.get_speed_x() + cos_heading
        new_speed_y = self.ship.get_speed_y() + sin_heading

        # updates the ship speeds with the new x and y speeds:
        self.ship.set_speed_x(new_speed_x)
        self.ship.set_speed_y(new_speed_y)

    def _move_obj(self, obj: Any):
        """
        this function moves a given game object (asteroid/ship/torpedo)
        according to the given formula.
        :param obj: a moving object in the game (asteroid/ship/torpedo).
        """
        # calculating the new x coordinate and y coordinate:
        delta_x = self.__screen_max_x - self.__screen_min_x
        new_spot_x = self.__screen_min_x + (obj.get_x() + obj.get_speed_x()
                                            - self.__screen_min_x) % delta_x
        delta_y = self.__screen_max_y - self.__screen_min_y
        new_spot_y = self.__screen_min_y + (obj.get_y() + obj.get_speed_y()
                                            - self.__screen_min_y) % delta_y

        # updates the object coordinates with the new coordinates:
        obj.set_x(new_spot_x)
        obj.set_y(new_spot_y)


def asteroids_speed_after_split(asteroid: Asteroid, torpedo: Torpedo) -> \
                                                        Tuple[float, float]:
    """
    This function calculates the appropriate speeds (in 2 axis) for the new
    asteroids that are created by splitting an asteroid.
    :param asteroid: The original asteroid (that needs to be split).
    :param torpedo: The torpedo which hit the asteroid.
    :return: A tuple with the speed for the new asteroids (speed_x, speed_y)
    """
    old_speed_x, old_speed_y = asteroid.get_speed_x(), asteroid.get_speed_y()
    old_speeds_root = math.sqrt((old_speed_x ** 2) + (old_speed_y ** 2))

    new_speed_x = (torpedo.get_speed_x() + old_speed_x) / old_speeds_root
    new_speed_y = (torpedo.get_speed_y() + old_speed_y) / old_speeds_root

    return new_speed_x, new_speed_y


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
