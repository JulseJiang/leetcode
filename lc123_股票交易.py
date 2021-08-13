# Title     : lc123.py
# Created by: julse@qq.com
# Created on: 2021/7/5 22:25
# des : 股票交易

# 123. 买卖股票的最佳时机 III
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
#
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


class Solution:
    def solve_nolimit(self, prices):
        dpi_11 = -prices[0]
        dpi_10 = dpi_11+prices[0]
        if len(prices) <2:return 0
        for p in prices:
            dpi0 = max(dpi_10,dpi_11+p) # 第i天不持有的最大收益：第i天卖掉，或者 i-1天没有
            dpi1 = max(dpi_11,dpi_10-p) # 第i天不持有的最大收益：第i-1天卖掉，或者 i-1天没有，今天也不买
            dpi_10 = dpi0
            dpi_11 = dpi1
        return dpi_10
    def solve(self, prices,K):
        n = len(prices)
        if K>n/2:
            return self.solve_nolimit(prices)
        import numpy as np
        dp = np.zeros((n,(K+1),2))
        for i in range(2,n):
            dp[i][0][0] = 0
            dp[i][0][1] = -float('inf')  # 非法交易
            for k in range(K+1):
                if i ==0:
                    dp[0][k][0] = 0
                    dp[0][k][1] = -prices[0]
                dp[i][k][0] = max(dp[i-1][k][0],dp[i-1][k][1]+prices[i])
                dp[i][k][1] = max(dp[i-1][k][1],dp[i-1][k-1][0]-prices[i])
        return dp[n-1][K][0]



if __name__ == '__main__':
    # prices = [3,3,5,0,0,3,1,4] # 6
    prices = [1,2,3,0,2] # 6
    K = 2
    ans = Solution().solve(prices,K)
    print(ans)


