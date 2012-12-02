# The main file

import bisect

from DS import *
from arr import *
from sarr import *

class SD:

    """
    The data structure object that will be put into a heap to determine
    which data structure to use. The higher the weight the better this
    data structure.
    """
    def __init__(self, isTesting, which = None):

        if which == DS.ARRAY:
            self.struct = Arr()
        elif which == DS.SORTED_ARRAY:
            self.struct = SArr()
        elif which == DS.MAX_HEAP:
            self.struct = MaxHeap()
        elif which == DS.MIN_HEAP:
            self.struct = MinHeap()
        elif which == DS.BINARY_SEARCH_TREE:
            self.struct = Balanced_BST()
        else:
            print "Default to Array"
            self.struct = Arr()

        self.contains_ctr = 0
        self.add_ctr = 0
        self.remove_ctr = 0
        self.get_ctr = 0
        self.get_min_ctr = 0
        self.extract_ctr = 0
        self.extract_min_ctr = 0

        self.len = 0

    def contains(self, key):
        return self.struct.contains(key)

    def add(self, key):
        self.struct.add(key)
        self.len += 1

    def remove(self, key):
        self.struct.remove(key)
        self.len -= 1

    def get(self, index):
        return self.struct.get(index)

    def get_min(self):
        return self.get(self, 0)

    def get_max(self):
        return self.get(self, len - 1)

    def extract(self, index):
        toReturn = get(self, index)
        remove(self, index)
        return toReturn

    def extract_min(self):
        extract(self, 0)

    def extract_max(self):
        extract(self, self.len - 1)

    def size(self):
        return self.len
