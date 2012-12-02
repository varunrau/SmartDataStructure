# The Heap with Heap property = max

import heapq
from minheap import *

class MaxHeap:

    """
    Creates an array.
    """
    def __init__(self):
        self.heap = MinHeap()

    """
    True iff the item is in the array.
    """
    def contains(self, key):
        return self.heap.contains(-key)

    """
    Adds the item to the array.
    """
    def add(self, key):
        return self.heap.add(-key)

    """
    Removes the item from the array.
    """
    def remove(self, key):
        self.heap.remove(-key)
    """
    Returns the item at index index
    """
    def get(self, index):
        return -self.heap.get(len(self.heap.array) - index - 1)

