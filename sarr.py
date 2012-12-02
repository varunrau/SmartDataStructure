import bisect

class SArr:
    def __init__(self):
        self.list = []
        self.sort()

    def sort(self):
        l = []
        for i in range(len(self.list)):
            bisect.insort(l, self.list[i])
        self.list = l

    def insert(self, key):
        bisect.insort(self.list, key)
        self.len += 1

    def get(self, index):
        left = bisect.bisect_left(self.list, index)
        length = len(self.list)
        if abs(self.list[min([left,length-1])] - index) >= abs(self.list[left-1] - index):
            return self.list[left-1]
        else:
            return self.list[left]

    def add(self, key):
        bisect.insort_right(self.list, key)

    def contains(self, x, lo=0, hi = None):
        if hi is None:
            hi = len(self.list)
        while lo < hi:
            mid = (lo+hi)//2
            midval = self.list[mid]
            if midval < x:
                lo = mid+1
            elif midval > x:
                hi = mid
            else:
                return True
        return False

    def remove(self, key):
        self.list.remove(key)
