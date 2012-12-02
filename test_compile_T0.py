# Test File

from SmartDataStructure import *
import itertools, random, threading, LiveGraph
from sarr import *
from minheap import *
from maxheap import *
from bst import *

def clear():
    s_data.len = 0

def addTest():
    s_data.len = 0

    for x in range(100000):
        y = random.randint(0, 1000000)
        s_data.add(y)

    if s_data.len != 100000:
        print "Add FAILED"
    else:
        print "Add PASSED"

def containsTest():
    test = []
    for x in range(10):
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
    for x in range(10):
        y = random.randint(0, 1000000)
        test.append(y)
        s_data.add(y)


    for x in range(10):
        s_data.remove(test[x])

    if s_data.len:
        print "Remove FAILED"
    else:
        print "Remove PASSED"

s_data = SD(True, 0)
s_data.add(1)
s_data.add(3)
print "done"
#addTest()
#clear()
#containsTest()
#clear()
#removeTest()
#clear()

