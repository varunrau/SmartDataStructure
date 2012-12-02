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
        globalz.which = which
        globalz.contains_ctr = 0
        globalz.add_ctr = 0
        globalz.remove_ctr = 0
        globalz.get_ctr = 0
        self.get_min_ctr = 0
        self.extract_min_ctr = 0
        globalz.num_ops = 0

        self.is_peak = True

        self.isTesting = isTesting
        self.len = 0

    def contains(self, key):
        globalz.contains_ctr += 1
        globalz.num_ops += 1
        self.time_to_reeval()
        return self.struct.contains(key)

    def setPeak(self, peak):
        self.is_peak = peak

    def add(self, key):
        self.struct.add(key)
        self.len += 1
        globalz.add_ctr += 1
        globalz.num_ops += 1
        self.time_to_reeval()

    def add_new(self, key):
        self.struct.add(key)
        self.len += 1

    def remove(self, key):
        self.struct.remove(key)
        self.len -= 1
        globalz.num_ops += 1
        globalz.remove_ctr += 1
        self.time_to_reeval()

    def get(self, index):
        globalz.get_ctr += 1
        globalz.num_ops += 1
        self.time_to_reeval()
        return self.struct.get(index)

    def get_min(self):
        self.get_min_ctr += 1
        globalz.num_ops += 1
        self.time_to_reeval()
        return self.get(self, 0)

    def get_max(self):
        self.get_max_ctr += 1
        globalz.num_ops += 1
        self.time_to_reeval()
        return self.get(self, len - 1)

    def extract(self, index):
        toReturn = self.get(index)
        self.remove_new(toReturn)
        globalz.num_ops += 1
        self.time_to_reeval()
        return toReturn

    def remove_new(self, key):
        self.struct.remove(key)

    def extract_min(self):
        self.extract(0)
        self.extract_min_ctr += 1
        globalz.num_ops += 1
        self.time_to_reeval()

    def extract_new(self, index):
        toReturn = self.get_new(index)
        print str(toReturn) + " to return"
        self.remove_new(toReturn)
        return toReturn

    def get_new(self, index):
        return self.struct.get(index)

    def extract_min_new(self):
        self.extract_new(0)

    def extract_max(self):
        self.extract(self.len - 1)
        self.extract_max_ctr += 1
        globalz.num_ops += 1
        self.time_to_reeval()

    def size(self):
        return self.len

    def reeval(self):
        if self.isTesting:
            return
        else:
            new = self.best_datastructure()
            print "best ds: " + str(new)
            if globalz.which != new:
                self.use_new_datastructure(newjj)

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
            print x
            if globalz.which == DS.MAX_HEAP:
                item = self.extract_min_new()
                temp.add(item)
            else:
                item = self.get(x)
                self.remove_new(item)
                temp.add(item)
        globalz.which = new
        self.struct = temp
        self.isTesting = False

    def best_datastructure(self):
        s = self.size()
        if not s:
            return globalz.which
        log = math.log(s)
        arr = globalz.add_ctr + s * globalz.contains_ctr + s * globalz.remove_ctr + s * globalz.get_ctr
        sarr = log * globalz.contains_ctr + s * globalz.add_ctr + globalz.remove_ctr * s + s
        bst = log * globalz.contains_ctr + log * globalz.add_ctr + globalz.remove_ctr * log + globalz.get_ctr * log
        htable = 3 * s + s * globalz.get_ctr
        minheap = globalz.contains_ctr * s + log * globalz.add_ctr + log * globalz.remove_ctr + log * globalz.get_ctr
        maxheap = globalz.contains_ctr * s + log * globalz.add_ctr + log * globalz.remove_ctr + log * globalz.get_ctr
        array = [arr, sarr, bst, minheap, maxheap, htable]
        mini = min(array)
        counter = 0
        smallest = 0
        if mini < array[globalz.which] * .75:
            for val in array:
                if mini == val:
                    smallest = counter
                counter += 1
            return smallest
        return globalz.which

    def time_to_reeval(self):
        if globalz.num_ops >= TIME_TO_REEVAL:
            self.reeval()


    def counters():
        return [contains_ctr, add_ctr, remove_ctr, get_ctr]
