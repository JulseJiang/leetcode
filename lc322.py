# # Title     : dynamic_programming.py
# # Created by: julse@qq.com
# # Created on: 2021/7/4 22:25
# # des : 零钱凑整 -- 超时


class Solution:
    def coinChange(self, coins,amount):
        coins = coins
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin,amount+1):
                dp[x] = min(dp[x-coin]+1,dp[x])
        return dp[amount] if dp[amount]!=float('inf') else -1





if __name__ == '__main__':
    # coins = [1,2,5]
    # amount = 11
    mydict = {}
    # ans = Solution().dp(amount)
    ans = Solution().coinChange([1,2,5],11)
    ans = Solution().coinChange([1,2,5],6)
    # ans = Solution().coinChange([2],3)
    print(ans)

