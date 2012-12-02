# Implementation of a HashTable
# A wrapper of a Python Dictionary

class Hashtable:

    def __init__(self, loadFactor = 100):
        self.numBuckets = 100
        self.buckets = []
        for x in range(self.numBuckets):
            self.buckets.append([0])
        self.loadFactor = loadFactor
        self.numKeys = 0

    def add(self, key):
        self.numKeys += 1
        if self.numKeys / self.numBuckets > self.loadFactor:
            print "buckets: " + str(self.numBuckets)
            print "keys: " + str(self.numKeys)
            self.resize(self.numBuckets * 2)
        key_hash = hash(key)
        self.buckets[key_hash % self.numBuckets].append(key_hash)

    def resize(self, newSize):
        self.numBuckets = newSize
        self.numKeys = 0
        oldBuckets = self.buckets
        for x in range(newSize):
            self.buckets.append([0])
        print "resize"

    def contains(self, key):
        key_hash = hash(key)
        for x in self.buckets[key_hash % self.numBuckets]:
            if x == key:
                return True
        return False

    def remove(self, key):
        self.numKeys -= 1
        key_hash = hash(key)
        self.buckets[key_hash % self.numBuckets].remove(key)

    def get(self, index):
        full_list = []
        for bucket in self.buckets:
            if bucket is not None:
                full_list.append(bucket)

        return full_list.sort()[full_list.sort() is not None].index(index)
