# Title     : lc581.py
# Created by: julse@qq.com
# Created on: 2021/8/3 19:02
# des : https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/
# 连续子数组

'''
方法1 sort之后找两端不同的位置
'''
def solve1(nums):
    # nums = [2,6,4,8,10,9,15] # 5
    # nums = [1,2,3,4]
    na = nums[:]
    na.sort()
    l = -1
    r = -1
    n = len(nums)
    for i in range(n):
        if l==-1 and nums[i]!=na[i]:l=i
        if r==-1 and nums[n-i-1]!=na[n-i-1]:r=n-i-1
    ans = 0 if r==-1 and l ==-1 else r-l+1
    print(ans)
    return ans


def solve2(nums):
    # nums = [2,6,4,8,10,9,15]
    l = -1
    r = -1
    lmin = float('-inf')
    rmax = float('inf')
    n = len(nums)
    for i in range(n):
        if nums[i]>=lmin:lmin = nums[i]
        else:l=i
        if nums[n-i-1]<=rmax:rmax = nums[n-i-1]
        else:r=n-i-1
    ans = 0 if r==-1 and l ==-1 else l-r+1
    print(ans)
    return ans


# nums = [2,6,4,8,10,9,15]
# nums = [1,2,3,4]
nums = [1,2,3,3,3]
 # ans = solve1(nums)
ans = solve2(nums)