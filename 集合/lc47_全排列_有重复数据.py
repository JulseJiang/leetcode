# Title     : lc47_全排列_有重复数据.py
# Created by: julse@qq.com
# Created on: 2021/7/27 11:42
# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/permutations-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def permuteUnique(self,nums):
        self.nums = nums
        self.all_subs = []
        self.memor = set()
        self.DFS([0 for i in range(len(nums))],[])
        return self.all_subs

    def DFS(self,visited,subset):
        if tuple(subset) in self.memor:return
        self.memor.add(tuple(subset[:]))
        if len(subset)==len(self.nums):
            self.all_subs.append(subset[:])
            return
        for i in range(len(self.nums)):
            if visited[i] == 1:continue
            visited[i] = 1
            elem = self.nums[i]
            subset.append(elem)
            self.DFS(visited,subset)
            subset.pop()
            visited[i] = 0
if __name__ == '__main__':
    nums = [1,1,2]
    ans = Solution().permuteUnique(nums)