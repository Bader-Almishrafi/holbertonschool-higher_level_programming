#!/usr/bin/python3


class Fish:
    """
    Fish parent class
    """

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """
    Bird parent class
    """

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    FlyingFish class that inherits from both Fish and Bird
    Demonstrates multiple inheritance and method overriding
    """

    def fly(self):
        # Override Bird.fly
        print("The flying fish is soaring!")

    def swim(self):
        # Override Fish.swim
        print("The flying fish is swimming!")

    def habitat(self):
        # Override habitat from both parents
        print("The flying fish lives both in water and the sky!")
