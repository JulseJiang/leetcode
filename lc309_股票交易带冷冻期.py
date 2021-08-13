# Title     : lc309.py
# Created by: julse@qq.com
# Created on: 2021/7/5 21:07
# des : 股票交易 [买入, 卖出, 冷冻期, 买入, 卖出]

# 1. 1次交易
# 2. 无限交易 + 冷冻期
# 3. K次交易
# 4. 买入有手续费


class Solution:
    def solve(self, prices):
        dpi_11 = -prices[0]
        dpi_10 = dpi_11+prices[0]
        if len(prices) <2:return 0
        for p in prices:
            dpi0 = max(dpi_10,dpi_11+p) # 第i天不持有的最大收益：第i天卖掉，或者 i-1天没有
            dpi1 = max(dpi_11,dpi_10-p) # 第i天不持有的最大收益：第i-1天卖掉，或者 i-1天没有，今天也不买
            dpi_10 = dpi0
            dpi_11 = dpi1
        return dpi_10



if __name__ == '__main__':
    mydict = {}
    prices = [7,6,4,3,1]
    ans = Solution().solve(prices)
    print(ans)