# Title     : lc19_秋叶红黄.py
# Created by: julse@qq.com
# Created on: 2021/8/19 17:39
# des : TODO

class Solution:
    def minimumOperations(self, leaves: str) -> int:
        # dp[i] 表示第i个位置是r，ry，ryr
        # dp[i][j] 表示把原字符串转换成当前状态的最小操作次数
        dp = [[float('inf')]*3 for _ in range(len(leaves))]
        dp[0][0] = 0 if leaves[0] == 'r' else 1
        for i in range(1,len(leaves)):
            isRed = 1 if leaves[i] == 'r' else 0
            dp[i][0] = dp[i-1][0] + 1-isRed
            dp[i][1] = min(dp[i-1][0],dp[i-1][1])+isRed
            dp[i][2] = min(dp[i-1][1],dp[i-1][2])+1-isRed
        return dp[len(leaves)-1][2]


leaves = "rrryyyrryyyrr"
leaves = "rry"
ans = Solution().minimumOperations(leaves)
print(ans)
