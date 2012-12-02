# Implementation of a HashTable
# A wrapper of a Python Dictionary

def HashTable:

    def __init__(self, loadFactor = 10):
        self.numBuckets = 10
        self.buckets = []
        for x in range(self.numBuckets):
            self.buckets[] = [0]
        self.loadFactor = loadFactor
        self.numKeys = 0

    def add(self, key):
        self.numKeys += 1
        if self.numKeys / self.numBuckets > self.loadFactor:
            self.resize(self.numBuckets * 2)
        key_hash = hash(key)
        buckets[key_hash % numBuckets].append(key_hash)

    def resize(self, newSize):
        self.numBuckets = newSize
        numKeys = 0
        oldBuckets = self.buckets
        for x in range(newSize):
            buckets.append([0])
        for bucket in oldBuckets:
            for key in bucket:
                self.add(key)

    def contains(self, key):
        key_hash = hash(key)
        for x in bucket[key_hash % self.numBuckets]:
            if x == key:
                return True
        return False

    def remove(self, key):
        self.numKeys -= 1
        key_hash = hash(key)
        buckets[key_hash % self.numBuckets].remove(key)

    def get(self, index):
        full_list = []
        for bucket in self.buckets:
            full_list.append(bucket)
        return full_list.sort().index(index)
