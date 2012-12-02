# The main file

import bisect

from arr import *
from sarr import *

class SD:

    """
    The data structure object that will be put into a heap to determine
    which data structure to use. The higher the weight the better this
    data structure.
    """
    def __init__(self):
        self.struct = SArr()
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
