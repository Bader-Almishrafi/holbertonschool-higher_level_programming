#!/usr/bin/python3
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    Abstract base class that defines
    the blueprint for all shapes
    """

    @abstractmethod
    def area(self):
        """
        Calculate and return the area of the shape
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate and return the perimeter of the shape
        """
        pass


class Circle(Shape):
    """
    Circle class that inherits from Shape
    """

    def __init__(self, radius):
        # Private attribute for radius
        self.__radius = radius

    def area(self):
        # Area of a circle = π * r^2
        return self.__radius ** 2 * pi

    def perimeter(self):
        # Perimeter (circumference) of a circle = 2 * π * r
        return abs(self.__radius * 2 * pi)


class Rectangle(Shape):
    """
    Rectangle class that inherits from Shape
    """

    def __init__(self, width, height):
        # Private attributes for width and height
        self.__width = width
        self.__height = height

    def area(self):
        # Area of a rectangle = width * height
        return self.__width * self.__height

    def perimeter(self):
        # Perimeter of a rectangle = 2 * (width + height)
        return abs((self.__width + self.__height) * 2)


def shape_info(any_shape):
    """
    Prints the area and perimeter of any shape.
    Uses duck typing: the object must implement
    area() and perimeter() methods.
    """
    print(f"Area: {any_shape.area()}")
    print(f"Perimeter: {any_shape.perimeter()}")
