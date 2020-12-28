from screen import Screen
from ship import *
import sys
import random
import math

from ex10 import screen

DEFAULT_ASTEROIDS_NUM = 5


class GameRunner:

    def __init__(self, asteroids_amount):
        self.__screen = Screen()
        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        self.__ship = Ship(0,0, 0, 0, 0)

    def run(self):
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You should not to change this method!
        self._game_loop()
        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def add_ship(self):
        """
        random 2 integers numbers which will be the  beginning location of the
        ship in axies. add a ship to our game.
        :return: None
        """
        rand_x = int(random.randint(self.__screen_min_x, self.__screen_max_x))
        rand_y = int(random.randint(self.__screen_min_y, self.__screen_max_y))
        self.__ship = Ship(rand_x, 0, rand_y, 0, 0)
        self.__screen.draw_ship(self.__ship.get_place_x(),
                                self.__ship.get_place_y(), 0)

    def _new_spot_formula(self, spped, location, screen_min, screen_max):
        """
        this is an helping function which calculates the value of new spot
        according to the given formula
        :param spped:
        :param location:
        :param screen_min:
        :param screen_max:
        :return: None
        """
        delta = screen_max - screen_min
        new_spot = screen_min + (location + spped - screen_min) % delta
        return new_spot

    def move_object(self, place_x, place_y, speed_x, speed_y):
        """
        this function moves the objects using the helping function
         "new_spot_formula" which gives the coordinates of the new spot
        :return: None
        """
        new_spot_x = self._new_spot_formula(speed_x, place_x,
                                            self.__screen_min_x,
                                            self.__screen_max_x)

        new_spot_y = self._new_spot_formula(speed_y, place_y,
                                            self.__screen_min_y,
                                            self.__screen_max_y)
        return new_spot_x, new_spot_y

    def change_ship_direction(self):
        """
        this function moves the shop in 7 degrees according to the user input
        :return: None
        """
        # in case the user clicked right
        if self.__screen.is_right_pressed():
            direction = self.__ship.get_direction() + 7
            self.__ship.set_direction(direction)
        # in case the user clicked left
        if self.__screen.is_left_pressed():
            direction = self.__ship.get_direction() - 7
            self.__ship.set_direction(direction)
        #self.__screen.draw_ship(self.__ship.get_place_x(),
                                #self.__ship.get_place_y(),
                                #self.__ship.get_direction())

    def acceleration_of_ship(self):
        """
        Accelerates the speed of the ship to each axis according
        to the given formula
        :return: None
        """
        old_speed_x = self.__ship.get_speed_x()
        old_speed_y = self.__ship.get_speed_y()
        while self.__screen.is_up_pressed():
            heading = (self.__ship.get_direction() / 360) * (math.pi ** 2)
            new_speed_x = old_speed_x + math.cos(heading)
            new_speed_y = old_speed_y + math.sin(heading)
            self.__ship.set_speed_x(new_speed_x)
            self.__ship.set_speed_y(new_speed_y)
            self.__screen.draw_ship(self.__ship.get_place_x(),
                                    self.__ship.get_place_y(),
                                    self.__ship.get_direction())
            #self.move_object(self.__ship.get_place_x(),
                             #self.__ship.get_place_y(),
                             #self.__ship.get_speed_x(),
                             #self.__ship.get_speed_y())
            #self.__screen.draw_ship(self.__ship.get_place_x(),
                                    #self.__ship.get_place_y(),
                                    #self.__ship.get_direction())
        self.__ship.set_speed_x(old_speed_x)
        self.__ship.set_speed_y(old_speed_y)
        # TODO: make sure that there is no problem

    def _game_loop(self):
        # TODO: Your code goes here


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
