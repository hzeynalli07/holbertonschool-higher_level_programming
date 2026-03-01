#!/usr/bin/python3
"""
Module for BaseGeometry class with integer_validator
"""


class BaseGeometry:
    """Class with area and integer_validator methods"""

    def area(self):
        """Raises an Exception because area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value as a positive integer.
        
        Args:
            name (str): The name of the value.
            value (any): The value to validate.
            
        Raises:
            TypeError: If value is not exactly an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
