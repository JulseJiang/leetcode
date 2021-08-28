# Title     : lc446.py
# Created by: julse@qq.com
# Created on: 2021/8/11 17:16
# des :https://leetcode-cn.com/problems/arithmetic-slices-ii-subsequence/
from collections import defaultdict

# count = 0
# cn = 0
# def solve1(nums):
#     nums.sort()
#     DFS(nums,0)
# def DFS(nums,i):
#     global count
#     if i == len(nums):return
#     for j in range(i,len(nums)):
#         if nums[i] > nums[j] or (i>0 and nums[i-1]>nums[j]):
#             continue
#         nums[i],nums[j] = nums[j],nums[i]
#         if i>=2:
#             count += check(nums,i)
#         DFS(nums,i+1)
#         nums[i],nums[j] = nums[j],nums[i]
# def check(nums,i):
#     global cn
#     cn +=1
#     for j in range(1,i):
#         if nums[j+1]-nums[j] != nums[j]-nums[j-1]:
#             return 0
#     return 1


'''
元素去重了已经
'''
# class Solution:
#     def numberOfArithmeticSlices(self, nums):
#         self.count = 0
#         memor = set()
#         def solve1(nums):
#             nums.sort()
#             DFS(nums,0)
#         def DFS(nums,i):
#             if i == len(nums):return
#             for j in range(i,len(nums)):
#                 if nums[i] > nums[j] or (i>0 and nums[i-1]>nums[j]):
#                     continue
#                 nums[i],nums[j] = nums[j],nums[i]
#                 if i>=2 and tuple(nums[:i]) not in memor and check(nums,i):
#                     self.count += 1
#                     memor.add(tuple(nums[:i]))
#                 DFS(nums,i+1)
#                 nums[i],nums[j] = nums[j],nums[i]
#         def check(nums,i):
#             for j in range(1,i):
#                 if nums[j+1]-nums[j] != nums[j]-nums[j-1]:
#                     return False
#             return True
#         solve1(nums)
#         return self.count

# '''
# 超时 O((2^n)-1) * O(n)
# '''
#
# class Solution:
#     def numberOfArithmeticSlices(self, nums):
#         self.count = 0
#         memor = set()
#         def solve1(nums):
#             nums.sort()
#             dnums = [(v,i) for i,v in enumerate(nums)]
#             DFS(dnums,0)
#             print()
#         def DFS(dnums,i):
#             if i == len(dnums):return
#             for j in range(i,len(nums)):
#                 if dnums[i][1] > dnums[j][1] or (i>0 and dnums[i-1][1]>dnums[j][1]):
#                     continue
#                 dnums[i],dnums[j] = dnums[j],dnums[i]
#                 if i>=2 and tuple(dnums[:i+1]) not in memor and check(dnums,i):
#                     self.count += 1
#                     memor.add(tuple(dnums[:i+1]))
#                 DFS(dnums,i+1)
#                 dnums[i],dnums[j] = dnums[j],dnums[i]
#         def check(dnums,i):
#             for j in range(1,i):
#                 if dnums[j+1][0]-dnums[j][0] != dnums[j][0]-dnums[j-1][0]:
#                     return False
#             return True
#         solve1(nums)
#         return self.count

'''
接近答案，但是中途误入歧途
'''
# class Solution:
#     def numberOfArithmeticSlices(self, nums):
#         self.count = 0
#         memor = {}
#         def jiecheng(n):
#             if n ==1 or n==0:return 1
#             return n*jiecheng((n-1))
#
#         def solve2(nums):
#             nums.sort()
#             for i in range(len(nums)-1):
#                 for j in range(i+1,len(nums)):
#                     step = nums[j]-nums[i]
#                     if step not in memor:memor[step]=0
#                     memor[step]+=1
#             for v in memor.values():
#                 if v < 3:continue
#                 n = 0
#                 for i in range(3,len(nums)):
#                     if jiecheng(i)/(jiecheng(3)*(jiecheng(i-3))) ==v:
#                         n = i
#                         self.count +=v
#                         break
#                 for i in range(4,n+1):
#                     self.count +=jiecheng(n)/(jiecheng(i)*(jiecheng(n-i)))
#         solve2(nums)
#         return self.count


'''
优化等差数列判断
'''

class Solution:
    def numberOfArithmeticSlices(self, nums):
        self.count = 0
        memor = set()
        def solve1(nums):
            nums.sort()
            dnums = [(v,i) for i,v in enumerate(nums)]
            DFS(dnums,0,False)
        def DFS(dnums,i,dc):
            if i == len(dnums):return
            for j in range(i,len(nums)):
                if dnums[i][1] > dnums[j][1] or (i>0 and dnums[i-1][1]>dnums[j][1]):
                    continue
                dnums[i],dnums[j] = dnums[j],dnums[i]
                dc = check(dnums,i,dc)
                if i>=2 and tuple(dnums[:i+1]) not in memor and dc:
                    self.count += 1
                    memor.add(tuple(dnums[:i+1]))
                DFS(dnums,i+1,dc)
                dnums[i],dnums[j] = dnums[j],dnums[i]
        def check(dnums,i,dc):
            if not dc and i>2:return False
            return dnums[i][0]-dnums[i-1][0] == dnums[i-1][0]-dnums[i-2][0]
        solve1(nums)
        return self.count

'''
列表打印出来看看， 和其他方法比较'''
def solve3(nums):
    f = [defaultdict(int) for _ in nums]
    f1 = [defaultdict(list) for _ in nums]
    ans = 0
    subset = []
    for i in range(len(nums)):
        for j in range(i):
            d = nums[i]-nums[j]
            ans += f[j][d]
            f[i][d] += f[j][d]+1
            for c in f1[j][d]:
                f1[i][d] = []
                f1[i][d].append(c+[nums[i]])
                if len(c+[nums[i]])>2:subset.append(c+[nums[i]])
            f1[i][d].append([nums[j],nums[i]])
    return ans

# nums = [2,4,6,8,10] #7
nums = [1,2,3,4,5,6,7] # 20
# nums = [2,4,6,8] #3
# nums = [7,7,7,7,7] #16
# nums = [7,7,7,7]
# nums = [2,4,6]
# nums = [2,3,4,6,7,8]

ans = solve3(nums)
# ans = Solution().numberOfArithmeticSlices(nums)
