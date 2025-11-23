#!/usr/bin/python3
"""
Module 2-square
Defines class Square with size validation and area method.
"""


class Square:
    """
    Class Square that defines a square.
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2
