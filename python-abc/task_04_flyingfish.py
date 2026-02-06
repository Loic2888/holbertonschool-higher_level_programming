#!/usr/bin/python3
"""
Demonstrates multiple inheritance with FlyingFish class.

Fish and Bird parent classes with overridden methods in FlyingFish child.
Shows Method Resolution Order (MRO) for multiple inheritance.
"""


class Fish:
    """Base class for fish behavior."""

    def swim(self):
        """Fish swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Fish living environment."""
        print("The fish lives in water")

class Bird:
    """Base class for bird behavior."""

    def fly(self):
        """Bird flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Bird living environment."""
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """
    FlyingFish inherits from both Fish and Bird (multiple inheritance).
    
    Overrides all methods with flying fish specific behavior.
    MRO: FlyingFish -> Fish -> Bird -> object
    """
    def fly(self):
        """Flying fish soaring behavior."""
        print("The flying fish is soaring!")

    def swim(self):
        """Flying fish swimming behavior."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Flying fish dual habitat."""
        print("The flying fish lives both in water and the sky!")
