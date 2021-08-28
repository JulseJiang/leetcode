# Title     : lc526_优美数列.py
# Created by: julse@qq.com
# Created on: 2021/8/16 17:12
# des : TODO

class Solution1:
    def countArrangement(self, n: int) -> int:
        nums = list(range(1, n + 1))
        ans =[0]
        def DFS(i):
            if i>0 and not (nums[i-1]%(i)==0 or i% nums[i-1]==0):return
            if i ==len(nums):
                print(nums)
                ans[0] +=1
                return
            for j in range(i,len(nums)):
                nums[i],nums[j] = nums[j],nums[i]
                DFS(i+1)
                nums[i],nums[j] = nums[j],nums[i]

        DFS(0)
        return ans[0]

class Solution2:
    def countArrangement(self, n: int) -> int:
        nums = list(range(1, n + 1))
        ly = [set() for _ in range(n+1)]
        for i in range(1,n+1): # 位置
            for j in range(1,n+1):  # 数值
                if (i % j == 0 or j % i == 0):
                    ly[i].add(j)
        ans =[0]
        def solve1(n):
            DFS(0)
        def DFS(i):
            if i ==len(nums):
                ans[0] +=1
                return
            for j in range(i,len(nums)):
                if nums[j] not in ly[i+1]:continue
                nums[i],nums[j] = nums[j],nums[i]
                DFS(i+1)
                nums[i],nums[j] = nums[j],nums[i]
        solve1(n)
        return ans[0]

# dp[mask] = sum (dp[mask-2^i) if i % j == 0 or j % i == 0

class Solution3:
    def countArrangement(self, n: int) -> int:
        f = [0] * (1 << n)
        f[0] = 1  # dp 数组初始值
        for mask in range(1, 1 << n):
            num = bin(mask).count("1")
            for i in range(n):
                if mask & (1 << i) and (num % (i + 1) == 0 or (i + 1) % num == 0):
                    f[mask] += f[mask ^ (1 << i)]
        return f[(1 << n) - 1]



ans = Solution2().countArrangement(4)
