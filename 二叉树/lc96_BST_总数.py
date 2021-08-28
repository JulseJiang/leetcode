# Title     : lc96_BST_总数.py
# Created by: julse@qq.com
# Created on: 2021/8/20 15:54
# des : TODO

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1]*(n+1)
        for i in range(2,n+1):
            dp[i] = sum([dp[j-1]*dp[i-j] for j in range(1,i+1)])
        return dp[n]

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1]*(n+1)
        dp[2] = 2
        for i in range(3,n+1):
            rest = dp[i//2+1-1]*dp[i-i//2-1]  if i%2==1 else 0
            dp[i] = sum([dp[j-1]*dp[i-j] for j in range(1,i//2+1)])*2 + rest
        return dp[n]
# dp[1] = 1
# dp[2] = 2

# n = 6
# n = 3
# ans = Solution().numTrees(n)
# print(ans)

mydict = {5:9,1:2,3:4}
ans = sorted(mydict)
print()
print([mydict[key] for key in sorted(mydict)])
