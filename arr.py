import bisect

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
                return True
        return False

    """
    Adds the item to the array.
    """
    def add(self, key):
        self.array.append(key)
        print self.array

    """
    Removes the item from the array.
    """
    def remove(self, key):
        print "fda"
        print key
        print self.array
        self.array.remove(key)
        print self.array

    """
    Returns the item at index index
    """
    def get(self, index):
        self.array.sort()
        return self.array[index]

    def sort(self):
        l = []
        for i in range(len(self.array)):
            bisect.insort(l, self.array[i])
        return l

