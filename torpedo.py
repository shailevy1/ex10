class Torpedo:
    """
    this class simulates a torpedo in the "Asteroids" video game
    """

    def __init__(self, place_x, speed_x, place_y, speed_y, direction):
        """
        the constructor for class Torpedo
        :param place_x: the location of the ship on x axis
        :param speed_x: the speed of the ship on x axis
        :param place_y: the location of the ship on y axis
        :param speed_y: the speed of the ship on y axis
        :param direction: the direction of the torpedo movement in degrees.
        """
        self._place_x = place_x
        self._speed_x = speed_x
        self._place_y = place_y
        self._speed_y = speed_y
        self._direction = direction
