# Title     : 1477_子集与或.py
# Created by: julse@qq.com
# Created on: 2021/7/20 16:24
# des : TODO

class Solution:
    '''
    先把所有子集找出来，再遍历一次求异或

    suba not in dp2：是在集合里面查找，比较费时，改成字典试试
    '''
    def merge(self,dp0,dp1,n):
        dp2 = []
        for subi in dp0:
            for subj in dp1:
                suba = set(subi) | set(subj)
                if len(suba) == n and suba not in dp2:dp2.append(suba)
        return dp2
    # 求子集
    def subsetXORSum(self, nums):
        subsets = []
        ans = 0
        dp = []
        dp.append([]) # dp[0]
        subsets.extend(dp[0])
        dp.append([])
        for i in range(len(nums)):
            dp[1].append([i])
        subsets.extend(dp[1])
        for i in range(2,len(nums)+1):
            dp.append([])
            dp[i] = self.merge(dp[i-1],dp[1],i)
            subsets.extend(dp[i])

        for set in subsets:
            tp = 0
            for s in set:
                tp ^= nums[s]
            ans += tp
        return ans



if __name__ == '__main__':
    ans = Solution().subsetXORSum([1,3])
    print(ans)

    # dp0 = [[1,2],[2,3]]
    # dp1 = [[3],[1]]
    # ans = Solution().merge(dp0, dp1)
