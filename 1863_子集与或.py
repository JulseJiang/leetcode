# Title     : 1477_子集与或.py
# Created by: julse@qq.com
# Created on: 2021/7/20 16:24
# des : TODO



# class Solution:
#     '''
#     先把所有子集找出来，再遍历一次求异或
#
#     suba not in dp2：是在集合里面查找，比较费时，改成集合试试
#     列表,set,是可变内容，无法作为键
#     tuple是不可变的内容-- 失败
#     tuple 里面1，2，3和2，3，1这种重复没法去掉
#     '''
#     def merge(self,dp0,dp1,n):
#         dp2 = []
#         for subi in dp0:
#             for subj in dp1:
#                 suba = set(subi) | set(subj)
#                 if len(suba) == n and suba not in dp2:dp2.append(suba)
#         return dp2
#
#     # 求子集
#     def subsetXORSum(self, nums):
#         subsets = []
#         ans = 0
#         dp = []
#         dp.append([]) # dp[0]
#         subsets.extend(dp[0])
#         dp.append([])
#         for i in range(len(nums)):
#             dp[1].append([i])
#         subsets.extend(dp[1])
#         for i in range(2,len(nums)+1):
#             dp.append([])
#             dp[i] = self.merge(dp[i-1],dp[1],i)
#             subsets.extend(dp[i])
#
#         for set in subsets:
#             tp = 0
#             for s in set:
#                 tp ^= nums[s]
#             ans += tp
#         return ans

'''
仅仅是减少了变量占用空间，且提升不显著
'''
# class Solution:
#     '''
#     求子集的同时求异或
#     dpi 不用都保存下来
#     '''
#     # 求子集
#     def subsetXORSum(self, nums):
#         ans = 0
#         dp1 = []
#         for i in range(len(nums)):
#             dp1.append([i])
#             ans += nums[i]
#         dpi_1 = dp1
#         for i in range(2, len(nums) + 1):
#             dpi,tp = self.merge(dpi_1,dp1, i,nums)
#             ans +=tp
#             dpi_1 = dpi
#         return ans
#     def merge(self, dp0, dp1, n,nums):
#         result = 0
#         dp2 = []
#         for subi in dp0:
#             for subj in dp1:
#                 suba = set(subi) | set(subj)
#                 if len(suba) == n and suba not in dp2:
#                     dp2.append(suba)
#                     tp = 0
#                     for s in suba:
#                         tp ^=nums[s]
#                     result += tp
#         return dp2,result


# class Solution:
#     '''
#     求子集的同时求异或
#     dpi 不用都保存下来
#     '''
#     # 求子集
#     def subsetXORSum(self, nums):
#         n = len(nums)
#         dp = []
#         dp.append([[i] for i in range(len(nums))])
#         for i in range(1,n):
#             dp.append([])
#             dp[i] =self.merge(nums,dp[i-1])
#             # dp 数组
#             # j 是 长度为j+1的子集
#             # 子集列表 [i for j in dp for i in j]
#             # k 是每一个子集
#         # return [[nums[v] for v in k] for k in [i for j in dp for i in j]]
#         subset =  [[nums[v] for v in k] for k in [i for j in dp for i in j]]
#         ans = 0
#         for sub in subset:
#             tp = 0
#             for s in sub:
#                 tp ^= s
#             ans += tp
#         return ans
#     def merge(self,nums,dppi):
#         return [j+[k] for j in dppi for k in range(j[-1]+1,len(nums))]


# from functools import reduce
# from itertools import combinations
# from operator import xor
# class Solution:
#     def subsetXORSum(self,nums):
#         # [i for i in range(len(nums))]   i : 每一个下标 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#         # [combination for combination in combinations(nums, i + 1)] combination = nums 里面选择i+1个形成的子集   [(10,), (5,), (8,), (3,), (6,), (12,), (2,), (4,), (11,), (7,), (1,), (9,)]
#         # reduce(lambda x, y: x ^ y, combination) 异或结果
#         # [m for m in map(lambda combination: reduce(lambda x, y: x ^ y, combination), combinations(nums, i + 1))] [10, 5, 8, 3, 6, 12, 2, 4, 11, 7, 1, 9]
#         #
#
#         return sum([sum(map(lambda combination: reduce(lambda x, y: x ^ y, combination), combinations(nums, i + 1))) for i in range(len(nums))])


# class Solution:
#     def subsetXORSum(self,nums):
#         ans = 0
#         for i in range(len(nums)):
#             ans += nums[i]
#             ans += self.DFS(nums,nums[i],i+1)
#         return ans
#
#     def DFS(self,nums,xo,k):
#         if k >len(nums)-1:return 0
#         else:
#             sum = 0
#             for i in range(k,len(nums)):
#                 sum += xo^nums[i]
#                 sum += self.DFS(nums,xo^nums[i],i+1)
#             return sum

# from copy import deepcopy
# from functools import reduce
# from operator import xor
# class Solution:
#     def subsetXORSum(self,nums):
#         self.all_subs = []
#         self.xor = 0
#         # self.DFS(nums,-1,len(nums),[])
#         self.BFS(nums)
#         # print(self.all_subs)
#         # return self.all_subs
#         return sum(map(lambda x: reduce(xor, x), self.all_subs))
#
#     def DFS(self,nums,index,n,cur_sub):
#         '''
#         深度优先
#         :param nums: 目标数组
#         :param index: 起始下标
#         :param n: 子集长度
#         :param cur_sub: 当前子集
#         :return:
#         nums = [0,1,2,3]
#         [0],[0, 1],[0, 1, 2],[0, 1, 2, 3],[0, 1, 3],[0, 2],[0, 2, 3],[0, 3],[1],[1, 2],[1, 2, 3],[1, 3],[2],[2, 3],[3]
#         '''
#         if index == n-1:return
#         for i in range(index+1,n):
#             cur_sub.append(nums[i])
#             self.all_subs.append(deepcopy(cur_sub))
#             # print(cur_sub,end=',')
#             self.DFS(nums,i,n,cur_sub)
#             cur_sub.pop()
#
#     def BFS(self,nums):
#         '''
#         宽度优先
#         如：nums = [0,1,2,3]
#         得到集合的顺序为：[0],[1],[2],[3],[0, 1],[0, 2],[0, 3],[1, 2],[1, 3],[2, 3],[0, 1, 2],[0, 1, 3],[0, 2, 3],[1, 2, 3],[0, 1, 2, 3]
#         :param nums:
#         :return:
#         '''
#         q = []
#         q.append([-1])
#         while len(q)>0:
#             indexs = q.pop(0)
#             i_s =indexs[-1]
#             if i_s ==-1:indexs = []
#             else:self.all_subs.append([nums[i] for i in indexs])
#             for i in range(i_s + 1, len(nums)):
#                 indexs.append(i)
#                 q.append(deepcopy(indexs))
#                 # print(indexs,end=',')
#                 indexs.pop()
#     '''
#     队列实现宽度优先
#     '''
#     def BFS_1(self,nums):
#         from queue import Queue
#         q = Queue()
#         q.put([-1])
#         while not q.empty():
#             indexs = q.get()
#             i_s = indexs[-1]
#             if i_s ==-1:indexs = []
#             else:self.all_subs.append([nums[i] for i in indexs])
#             for i in range(i_s+1,len(nums)):
#                 indexs.append((i))
#                 q.put(indexs[:])
#                 q.put(deepcopy(indexs))
#                 indexs.pop()


# from itertools import combinations
# class Solution:
#     def subsetXORSum(self, nums):
#         # subset for subset in combinations(nums,i+1)) for i in range(len(nums))
#         # return [[(subset for subset in combinations(nums,i+1))] for i in range(len(nums))]
#         # ans = []
#         # for i in range(len(nums)):
#         #     for c in combinations(nums,i+1):
#         #         ans.append(list(c))
#         # return ans
#         # return [c for c in [combinations(nums,i+1) for i in range(len(nums))]]
#         return [c for i in range(len(nums)) for c in combinations(nums,i+1)]
#         # return [[x for x in combinations(nums, i + 1)] for i in range(len(nums))]



# from copy import deepcopy
#
# '''
# 动态规划2
# '''
#
# class Solution:
#     def subsetXORSum(self, nums):
#         allset = []
#         for i in nums:
#             cur_set = deepcopy(allset)
#             for j in range(len(cur_set)):
#                 cur_set[j] = cur_set[j] +[i]
#             cur_set.append([i])
#             allset.extend(deepcopy(cur_set))
#         return allset
from functools import lru_cache

'''
剪枝后的深度优先
'''
class Solution:
    def subsetXORSum(self,nums):
        self.nums = nums
        self.all_subs = []
        self.xor = 0
        self.memor = set() # 备忘录
        return self.DFS(-1)
    def DFS(self,start):
        if start in self.memor: return [] # 检查是否被备忘录记录
        else:
            dset = []
            if start == -1:dset = []
            else:
                dset.append([start])
            for i in range(start+1, len(self.nums)):
                ans = self.DFS(i)
                if start!=-1:
                    dset.extend([x+[start] for x in ans])
                dset.extend(ans)
            self.memor.add(start) # 记录，表示该节点已经被使用过
        return dset




if __name__ == '__main__':
    # nums = [1,3] # 6
    nums = [10,5,8,3,6,12,2,4,11,7,1,9] # 4095个集合，结果是 30720
    # nums = [5,1,6] # 28
    # nums = [0,1,2,3]
    ans = Solution().subsetXORSum(nums)
    # print(ans)


    # # 导入reduce
    # from functools import reduce
    # # 定义函数
    # def f(x,y):
    #     return x+y
    # # 定义序列，含1~10的元素
    # items = range(1,11)
    # # 使用reduce方法
    # result = reduce(f,items,100)
    # print(result)

