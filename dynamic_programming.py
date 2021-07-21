# Title     : dynamic_programming.py
# Created by: julse@qq.com
# Created on: 2021/7/4 22:25
# des : 零钱凑整 -- 超时
import functools
import sys
class Solution:
    def coinChange(self, coins,amount):
        self.coins = coins
        self.mydict = {}
        @functools.lru_cache(amount)
        def dp(amount):
            if amount==0:return 0
            elif amount<0:return -1
            min_tp = sys.maxsize
            for c in coins:
                tp = dp(amount-c)+1
                mydict[amount] = tp
                if (tp>0):min_tp=min(tp,min_tp)
            return -1 if min_tp==sys.maxsize else min_tp

if __name__ == '__main__':
    # coins = [1,2,5]
    # amount = 11
    mydict = {}
    # ans = Solution().dp(amount)
    ans = Solution().coinChange([1,2,5],11)
    print(ans)

