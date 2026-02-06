#!/usr/bin/python3
"""
Demonstrates mixin pattern for code reuse.

SwimMixin and FlyMixin provide swimming/flying capabilities.
Dragon combines both mixins plus its own roar method.
"""


class SwimMixin:
    """Mixin providing swimming capability."""
    def swim(self):
        """Creature swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Mixin providing flying capability."""
    def fly(self):
        """Creature flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class combining swim, fly, and roar abilities."""
    def roar(self):
        """Dragon roaring behavior."""
        print("The dragon roars!")
