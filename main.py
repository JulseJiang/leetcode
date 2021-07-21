class Solution:
    def solve(self, prices):
        min_tp = prices[0]
        max_tp = 0
        for idx,p in enumerate(prices):
            max_tp = max(max_tp,p-min_tp)
            min_tp = min(min_tp,p)
        return max_tp


if __name__ == '__main__':
    mydict = {}
    prices = [7,1,5,3,6,4]
    ans = Solution().solve(prices)
    print(ans)