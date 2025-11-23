#!/usr/bin/python3
"""
Module 1-square
Defines a class Square with size validation.
"""


class Square:
    """
    Class Square that defines a square with size validation.
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
