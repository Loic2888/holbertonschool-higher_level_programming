#!/usr/bin/python3
"""
VerboseList class extending built-in list with operation notifications.
Overrides append(), extend(), remove(),
and pop() to print informative messages.
"""


class VerboseList(list):
    """
    List subclass that prints notifications for modification operations.
    """

    def append(self, item):
        """Append item and notify."""
        super().append(item)
        print(f"Added {repr(item)} to the list.")

    def extend(self, items):
        """Extend list and notify with item count."""
        count = len(items)
        super().extend(items)
        print(f"Extended the list with {count} items.")

    def remove(self, item):
        """Notify before removing item."""
        print(f"Removed {repr(item)} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Notify before popping item."""
        item = self[index]
        super().pop(index)
        print(f"Popped {repr(item)} from the list.")
