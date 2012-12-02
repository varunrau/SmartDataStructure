# Test File

from SmartDataStructure import *
import itertools
import random
from sarr import *
from minheap import *
from maxheap import *
from bst import *

def clear():
    s_data.len = 0

def addTest():
    s_data.len = 0

    for x in range(10000):
        y = random.randint(0, 1000000)
        s_data.add(y)

    if s_data.len != 10000:
        print "Add FAILED"
    else:
        print "Add PASSED"

def containsTest():
    test = []
    for x in range(1000):
        y = random.randint(0, 1000000)
        s_data.add(y)
        test.append(y)

    def cont(arr, key):
        toReturn = False
        for x in arr:
            if x == key:
                return True
        return False


    for x in range(s_data.len):
        if not s_data.contains(x) and cont(test, x):
            print "Contains FAILED"
    print "Contains PASSED"

def removeTest():
    test = []
    for x in range(1000):
        y = random.randint(0, 1000000)
        test.append(y)
        s_data.add(y)


    for x in range(1000):
        s_data.remove(test[x])

    if s_data.len:
        print "Remove FAILED"
    else:
        print "Remove PASSED"

s_data = SD()
addTest()
clear()
containsTest()
clear()
removeTest()
clear()

