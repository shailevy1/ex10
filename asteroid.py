class Asteroid:
    """
    this class simulates a asteroid in the "Asteroids" video game
    """

    def __init__(self, place_x, speed_x, place_y, speed_y, size):
        """
        the constructor for class Asteroid
        :param place_x: the location of the ship on x axis
        :param speed_x: the speed of the ship on x axis
        :param place_y: the location of the ship on y axis
        :param speed_y: the speed of the ship on y axis
        :param size: the size of the asteroid.
        """
        self._place_x = place_x
        self._speed_x = speed_x
        self._place_y = place_y
        self._speed_y = speed_y
        # checking size
        self._size = size
