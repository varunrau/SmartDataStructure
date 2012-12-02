# The main file

import bisect

from DS import *
from arr import *
from sarr import *
from bst import *
from minheap import *
from maxheap import *
from hashtable import *
import math
import globalz

TIME_TO_REEVAL = 1

class SD:

    """
    The data structure object that will be put into a heap to determine
    which data structure to use. The higher the weight the better this
    data structure.
    """
    def __init__(self, isTesting, which = DS.ARRAY):
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
        elif which == DS.HASHTABLE:
            self.struct = Hashtable()
        else:
            self.struct = Arr()
        self.which = which
        self.contains_ctr = 0
        self.add_ctr = 0
        self.remove_ctr = 0
        self.get_ctr = 0
        self.get_min_ctr = 0
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

    def setPeak(self, peak):
        self.is_peak = peak

    def add(self, key):
        self.struct.add(key)
        self.len += 1
        self.add_ctr += 1
        self.num_ops += 1
        self.time_to_reeval()

    def add_new(self, key):
        self.struct.add(key)
        self.len += 1

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
        toReturn = self.get(index)
        self.remove_new(toReturn)
        self.num_ops += 1
        self.time_to_reeval()
        return toReturn

    def remove_new(self, key):
        print self.struct
        self.struct.remove(key)

    def extract_min(self):
        self.extract(0)
        self.extract_min_ctr += 1
        self.num_ops += 1
        self.time_to_reeval()

    def extract_new(self, index):
        toReturn = self.get_new(index)
        self.remove_new(toReturn)
        return toReturn

    def get_new(self, index):
        return self.struct.get(index)

    def extract_min_new(self):
        self.extract_new(0)

    def extract_max(self):
        self.extract(self.len - 1)
        self.extract_max_ctr += 1
        self.num_ops += 1
        self.time_to_reeval()

    def size(self):
        return self.len

    def reeval(self):
        if self.isTesting:
            return
        else:
            new = self.best_datastructure()
            #if new != self.which:
            self.use_new_datastructure(0)
            #self.use_new_datastructure(5)

    def use_new_datastructure(self, new):
        self.isTesting = True
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
        elif new == DS.HASHTABLE:
            temp = Hashtable()
        else:
            temp = Arr()
        for x in range(self.size()):
            if self.which == DS.MAX_HEAP:
                item = self.extract_max_new()
                temp.add(item)
            else:
                item = self.extract_min_new()
                temp.add(item)
        self.which = new
        self.struct = temp
        self.isTesting = False

    def best_datastructure(self):
        s = self.size()
        if not s:
            return self.which
        log = math.log(s)
        arr = self.add_ctr + s * self.contains_ctr + s * self.remove_ctr + s * self.get_ctr
        sarr = log * self.contains_ctr + s * self.add_ctr + self.remove_ctr * s + s
        bst = log * self.contains_ctr + log * self.add_ctr + self.remove_ctr * log + self.get_ctr * log
        htable = 3 * s + s * self.get_ctr
        minheap = self.contains_ctr * s + log * self.add_ctr + log * self.remove_ctr + log * self.get_ctr
        maxheap = self.contains_ctr * s + log * self.add_ctr + log * self.remove_ctr + log * self.get_ctr
        array = [arr, sarr, bst, minheap, maxheap, htable]
        mini = min(array)
        counter = 0
        smallest = 0
        if mini < array[self.which] * .75:
            for val in array:
                if mini == val:
                    smallest = counter
                counter += 1
            return smallest
        return self.which

    def time_to_reeval(self):
        if self.num_ops >= TIME_TO_REEVAL:
            self.reeval()


    def counters():
        return [contains_ctr, add_ctr, remove_ctr, get_ctr]
