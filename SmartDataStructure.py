# The main file

class SD:

    """
    The data structure object that will be put into a heap to determine
    which data structure to use. The higher the weight the better this
    data structure.
    """
    def __init__(self):
        self.struct = Arr()

    def contains(self, key):
        return self.struct.contains(key)

    def add(self, key):
        self.struct.add(key)

    def remove(self, key):
        self.struct.remove(key)

    def get(self, index):
        return self.struct.get(index)


class Arr:

    """
    Creates an array.
    """
    def __init__(self):
        self.array = []

    """
    True iff the item is in the array.
    """
    def contains(self, key):
        for x in self.array:
            if x == key:
                return true
        return false

    """
    Adds the item to the array.
    """
    def add(self, key):
        self.array.add(self.array.size(), key)

    """
    Removes the item from the array.
    """
    def remove(self, key):
        self.array.remove(key)

    """
    Returns the item at index index
    """
    def get(self, index):
        return self.array[index]

