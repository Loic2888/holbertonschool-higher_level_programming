#!/usr/bin/python3
"""
CountedIterator class - Custom iterator that tracks traversed elements.

Features:
- Iterates over any iterable object (list, tuple, etc.)
- Counts how many elements have been read
- Provides get_count() to know total processed elements
"""


class CountedIterator():
    def __init__(self, iterable):
        """
        Initialize iterator with iterable object.

        Args:
            iterable: List or iterable object to traverse
        """
        self.iterable = iterable
        self.count = 0

    def __iter__(self):
        """
        Makes this object iterable for 'for' loops.
        Always returns self.
        """
        return self

    def __next__(self):
        """
        Called each iteration in for loop.
        Returns next element or stops iteration.
        """
        if self.count >= len(self.iterable):
            raise StopIteration
        item = self.iterable[self.count]
        self.count += 1
        return item

    def get_count(self):
        """
        Returns total number of elements read so far.
        Returns:
            int: Number of processed elements
        """
        return self.count
