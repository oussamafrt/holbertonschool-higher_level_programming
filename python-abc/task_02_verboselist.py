#!/usr/bin/python3
"""Shebang line indicating the interpreter for the script."""


class VerboseList(list):
    """Overriding the append method"""

    def append(self, item):
        """Overriding the extend method"""
        print("Added [{}] to the list.".format(item))
        super().append(item)

    def extend(self, items):
        """"""
        print("Extended the list with [{}] items.".format(len(items)))
        super().extend(items)

    def remove(self, item):
        """Overriding the remove method"""
        print("Removed [{}] from the list".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Overriding the pop method"""
        print("Popped [{}] from the list.".format(self[index]))
        return super().pop(index)
