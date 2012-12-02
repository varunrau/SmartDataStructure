# Test File

from main import *
import itertools
from random import *
from sarr import *
from minheap import *
from maxheap import *
from bst import *

def test():
    s_data.len = 0

    for x in choice([x for x in itertools.permutations(range(10))]):
        s_data.add(x)

    print(str(s_data.contains(3)) + " should be true")

    s_data.remove(3)
    print(str(s_data.contains(3)) + " should be false")

    print(str(s_data.get(0)) + " should be 0")

s_data = SD(0, True)
test()
