#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class Animal"""

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Dog class"""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat class"""

    def sound(self):
        return "Meow"
