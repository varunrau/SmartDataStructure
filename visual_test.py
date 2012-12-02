# Test File

from SmartDataStructure import *
import itertools, random, threading, LiveGraph, time
from sarr import *
from minheap import *
from maxheap import *
from bst import *

def clear():
    s_data.len = 0

def addTest():
    s_data.len = 0

    for x in range(100):
        y = random.randint(0, 1000000)
        s_data.add(y)

    if s_data.len != 100:
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

def addAlot():
  for i in range(1000):
    y = random.randint(0, 1000)
    s_data.add(y)
  
def containsRemAlot():
  for i in range (1000):
    x = random.randint(0, 1000) 
    if s_data.contains(x):
       s_data.remove(x)

def containsAddRem():
  for i in range (1000):
    x = random.randint(0, 1000) 
    if s_data.contains(x):
       s_data.add(x)
       s_data.remove(x)
       s_data.remove(x)  


s_data = SD(False,0)
s_data.setPeak(False)

graphThread = LiveGraph.LiveGraph()
graphThread.start()

startBias = 50
bias = startBias

for i in range(10):
  addAlot()
  time.sleep(0.1)

for i in range(15):
  x = random.randint(0 + bias, 60 + bias)
  time.sleep(0.1)
  if x < 20:
    addAlot()
  elif x < 120:
    containsRemAlot()
  elif x < 150:
    containsAddRem()
  else:
    time.sleep(0.01)
    bias += 10
    if bias > 200:
      bias = startBias

while 1:
  s_data.get_min()
  
  
  
  
  
  
  



