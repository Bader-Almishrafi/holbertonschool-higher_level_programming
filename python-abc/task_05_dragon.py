#!/usr/bin/python3


class SwimMixin:
    """
    Mixin that provides swimming behavior
    """

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    Mixin that provides flying behavior
    """

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that combines multiple behaviors
    using mixins
    """

    def roar(self):
        print("The dragon roars!")
