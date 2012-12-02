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

    def contains(self, key):
        return self.struct.contains(key)

    def add(self, key):
        self.struct.add(key)

    def remove(self, key):
        self.struct.remove(key)

    def get(self, index):
        return self.struct.get(index)

