# The Heap with Heap property = min

import heapq

class MinHeap:

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
        heapq.heappush(self.array, key)

    """
    Removes the item from the array.
    """
    def remove(self, key):
        stack = []
        while (True):
            val = heapq.heappop(self.array)
            stack.append(val)
            if val == key:
                break
        toReturn = stack.pop()
        for x in stack:
            self.add(x)
        return toReturn
    """
    Returns the item at index index
    """
    def get(self, index):
        #stack = []
        #for x in range(index-1):
         #   stack.append(heapq.heappop(self.array))
        #toReturn = heapq.heappop(self.array)
        #for x in stack:
         #   self.add(x)
        #return toReturn
        return 0

