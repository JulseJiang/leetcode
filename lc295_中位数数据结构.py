# Title     : lc295_中位数数据结构.py
# Created by: julse@qq.com
# Created on: 2021/8/27 16:18
# des : TODO

'''
最小堆和最大堆 - 通过
'''
import heapq
from functools import reduce


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lh = []
        self.rh = []

    def addNum(self, num: int) -> None:
        if len(self.lh) == 0 or num > 0-self.lh[0]:
            heapq.heappush(self.rh,num)
        else:
            heapq.heappush(self.lh, 0-num)

        ln = len(self.lh)
        rn = len(self.rh)

        if ln-rn==2:
            heapq.heappush(self.rh,0-heapq.heappop(self.lh))
        elif rn - ln==1:
            heapq.heappush(self.lh,0-heapq.heappop(self.rh))
        else:pass


    def findMedian(self) -> float:
        ln = len(self.lh)
        rn = len(self.rh)
        return (0-self.lh[0] + self.rh[0]) / 2 if ln ==rn else float(0-self.lh[0])
'''
有序列表
'''

from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = SortedList()
        self.left = 0
        self.right = 0


    def addNum(self, num: int) -> None:
        nums_ = self.nums
        nums_.add(num)



    def findMedian(self) -> float:
        n = len(self.nums)
        return (self.nums[n//2]+self.nums[n//2-1])/2 if n%2 ==0 else float(self.nums[n//2])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(3)
# obj.addNum(4)
# obj.addNum(5)


# obj.addNum(-1)
# obj.addNum(2)
# obj.addNum(2)
# param_2 = obj.findMedian()
# print(param_2)


# del self._lists[:]
# del self._maxes[:]
# del self._index[:]


# a = [1,4]
# a.clear()

# a = [3,4,8,9,7,10,9,15,20,13]
# b = a[:]
# c = a[:]
# heapq.heapify(a)
# heapq.heappush(b,2)
# heapq.heappop(c)
# print(a)
# print(b)
# print(c)

# [3, 4, 8, 9, 7, 10, 9, 15, 20, 13]
# [2, 3, 8, 9, 4, 10, 9, 15, 20, 13, 7]
# [4, 7, 8, 9, 13, 10, 9, 15, 20]


mydic = {0: {0: [3], 2: [15]}, -1: {1: [9]}, 1: {1: [20]}, 2: {2: [7]}}
# print([[mydic[b][a] for a in sorted(mydic[b])] for b in sorted(mydic)])

ans = []
for b in sorted(mydic):
    tp = []
    for a in sorted(mydic[b]):
        for x in sorted(mydic[b][a]):
            tp.append(x)
    ans.append(tp)
print(ans)






# [mydic[b][a] for a in sorted(mydic[b]) for b in sorted(mydic)]
# print([[mydic[b][a] for a in sorted(mydic[b])] for b in sorted(mydic)])

