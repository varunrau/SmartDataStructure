# The main file

import bisect

from DS import *
from arr import *
from sarr import *
from bst import *
from minheap import *
from maxheap import *

class SD:

    """
    The data structure object that will be put into a heap to determine
    which data structure to use. The higher the weight the better this
    data structure.
    """
    def __init__(self, isTesting, which = None):
        print(which)
        if which == DS.ARRAY:
            print "Array"
            self.struct = Arr()
        elif which == DS.SORTED_ARRAY:
            print "S Array"
            self.struct = SArr()
        elif which == DS.MAX_HEAP:
            print "M Heap"
            self.struct = MaxHeap()
        elif which == DS.MIN_HEAP:
            print "min heap"
            self.struct = MinHeap()
        elif which == DS.BINARY_SEARCH_TREE:
            print "bst"
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
        self.num_ops = 0

        self.isTesting = isTesting
        self.len = 0

    def contains(self, key):
        self.contains_ctr += 1
        self.num_ops += 1
        return self.struct.contains(key)

    def add(self, key):
        self.struct.add(key)
        self.len += 1
        self.add_ctr += 1
        self.num_ops += 1

    def remove(self, key):
        self.struct.remove(key)
        self.len -= 1
        self.num_ops += 1
        self.remove_ctr += 1

    def get(self, index):
        self.get_ctr += 1
        self.num_ops += 1
        return self.struct.get(index)

    def get_min(self):
        self.get_min_ctr += 1
        self.num_ops += 1
        return self.get(self, 0)

    def get_max(self):
        self.get_max_ctr += 1
        self.num_ops += 1
        return self.get(self, len - 1)

    def extract(self, index):
        toReturn = get(self, index)
        remove(self, index)
        self.extract_ctr += 1
        self.num_ops += 1
        return toReturn

    def extract_min(self):
        extract(self, 0)
        self.extract_min_ctr += 1
        self.num_ops += 1

    def extract_max(self):
        extract(self, self.len - 1)
        self.extract_max_ctr += 1
        self.num_ops += 1

    def size(self):
        return self.len

    def reeval(self):
        if self.isTesting:
            return
        else:
            print "NEED TO IMPLEMENT"


