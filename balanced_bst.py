from btree import *

class Balanced_BST:

 """
    Creates an array.
    """
    def __init__(self):
        self.btree = BTree(20)

    """
    True iff the item is in the array.
    """
    def contains(self, key):
        return self.btree.__contains__(key)

    """
    Adds the item to the array.
    """
    def add(self, key):
        self.btree.insert(key)

    """
    Removes the item from the array.
    """
    def remove(self, key):
        self.btree.remove(key)

    """
    Returns the item at index index
    """
    def get(self, index):


