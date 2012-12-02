# The main file

import bisect

from DS import *
from arr import *
from sarr import *
from bst import *
from minheap import *
from maxheap import *

TIME_TO_REEVAL = 100

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

        self.which = which
        self.contains_ctr = 0
        self.add_ctr = 0
        self.remove_ctr = 0
        self.get_ctr = 0
        self.get_min_ctr = 0
        self.extract_ctr = 0
        self.extract_min_ctr = 0
        self.num_ops = 0

        self.is_peak = True

        self.isTesting = isTesting
        self.len = 0

    def contains(self, key):
        self.contains_ctr += 1
        self.num_ops += 1
        self.time_to_reeval()
        return self.struct.contains(key)

    def add(self, key):
        self.struct.add(key)
        self.len += 1
        self.add_ctr += 1
        self.num_ops += 1
        self.time_to_reeval()

    def remove(self, key):
        self.struct.remove(key)
        self.len -= 1
        self.num_ops += 1
        self.remove_ctr += 1
        self.time_to_reeval()

    def get(self, index):
        self.get_ctr += 1
        self.num_ops += 1
        self.time_to_reeval()
        return self.struct.get(index)

    def get_min(self):
        self.get_min_ctr += 1
        self.num_ops += 1
        self.time_to_reeval()
        return self.get(self, 0)

    def get_max(self):
        self.get_max_ctr += 1
        self.num_ops += 1
        self.time_to_reeval()
        return self.get(self, len - 1)

    def extract(self, index):
        toReturn = get(self, index)
        remove(self, index)
        self.extract_ctr += 1
        self.num_ops += 1
        self.time_to_reeval()
        return toReturn

    def extract_min(self):
        extract(self, 0)
        self.extract_min_ctr += 1
        self.num_ops += 1
        self.time_to_reeval()

    def extract_max(self):
        extract(self, self.len - 1)
        self.extract_max_ctr += 1
        self.num_ops += 1
        self.time_to_reeval()

    def size(self):
        return self.len

    def reeval(self):
        if self.isTesting:
            return
        else:
            new_data_structure = self.best_datastructure()
            if new_data_structure != self.which:
                self.use_new_datastructure(new_data_structure)

    def use_new_datastructure(self, new):
        if new == DS.ARRAY:
            temp = Arr()
        elif new == DS.SORTED_ARRAY:
            temp = SArr()
        elif new == DS.MAX_HEAP:
            temp = MaxHeap()
        elif new == DS.MIN_HEAP:
            temp = MinHeap()
        elif new == DS.BINARY_SEARCH_TREE:
            temp = Balanced_BST()
        else:
            temp = Arr()
        for x in range(self.size()):
            if which == DS.MAX_HEAP:
                item = self.extract_max()
                temp.add(item)
            else:
                item = self.extract(x)
                temp.add(item)
        self.struct = temp

    def best_datastructure(self)
        s = self.size()
        log = math.log(s, 2)
        arr = add_ctr + s * contains_ctr + s * remove_ctr + s * get_ctr
        sarr = log * contains_ctr + s * add_ctr + remove_ctr * s + s
        bst = log * contains_ctr + log * add_ctr + remove_ctr * log + get_ctr * log
        htable = 3 * s + s * get_ctr
        heap = contains_ctr * s + log * add_ctr + log * remove_ctr + log * get_ctr
        array = [arr, sarr, bst, htable, heap]
        mini = min(array)
        counter = 0
        smallest = array[0]
        if mini < val * .75:
            for val in array:
                if mini == val:
                    smallest = counter
                counter += 1
            return counter
        return self.which


    def time_to_reeval(self):
        if self.num_ops >= TIME_TO_REEVAL:
            self.reeval()

