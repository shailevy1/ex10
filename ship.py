class Ship:
    """
    this class simulates a spacecraft in the "Asteroids" video game
    """

    def __init__(self, place_x, speed_x, place_y, speed_y, direction):
        """
        the constructor for class ship
        :param place_x: the location of the ship on x axis
        :param speed_x: the speed of the ship on x axis
        :param place_y: the location of the ship on y axis
        :param speed_y: the speed of the ship on y axis
        :param direction: the direction of the tip in degrees
        """
        self.__place_x = place_x
        self.__speed_x = speed_x
        self.__place_y = place_y
        self.__speed_y = speed_y
        self.__direction = direction

    def get_direction(self):
        """
        :return: the direction of the ship
        """
        return self.__direction

    def get_place_x(self):
        """
        :return: the location of the ship on the X axis
        """
        return self.__place_x

    def get_place_y(self):
        """
        :return: the location of the ship on the y axis
        """
        return self.__place_y

    def get_speed_x(self):
        """
        :return: the speed of the ship on the X axis
        """
        return self.__speed_x

    def get_speed_y(self):
        """
        :return: the speed of the ship on the y axis
        """
        return self.__speed_y

    def set_direction(self, direction):
        """
        set new direction for the ship in degrees
        :param direction: new direction for the ship
        :return: none
        """
        self.__direction = direction

    def set_speed_x(self, speed_x):
        """
        set new speed for the ship on the x axis
        :param speed_x: new speed for the ship on x axis
        :return: None
        """
        self.__speed_x = speed_x

    def set_speed_y(self, speed_y):
        """
        set new speed for the ship on the y axis
        :param speed_y: new speed for the ship on y axis
        :return: None
        """
        self.__speed_y = speed_y
