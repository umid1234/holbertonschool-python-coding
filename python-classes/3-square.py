#!/usr/bin/python3
"""
Module 3-square
Defines a class Square with getter and setter for size.
"""
class Square:
    """
    Class Square that defines a square with controlled size attribute.
    """
    def __init__(self, size=0):
        self.size = size
    @property
    def size(self):
        """
        Getter for size.
        """
        return self.__size
    @size.setter
    def size(self, value):
        """
        Setter for size with validation.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2
