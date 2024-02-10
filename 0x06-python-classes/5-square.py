#!/usr/bin/python3

"""
This is a module on how to
to incorporate loops in these classes
"""
class Square:
    """
    This is a class on square
    Attributes:
        __size(int): The size of the square
    """


    def __init__(self, size=0):
        self.__size = size

    @property

    def size(self):
        return self.__size

    @size.setter

    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__area ** 2

    def my_print(self):
        """
        This function will be used to
        print the # symbol to represent a
        square based on the size entered by the user
        """

        for i in range(0, self.size):
            for j in range(0, self.size):
                print("#", end="")
            print("")
