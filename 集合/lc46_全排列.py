# Title     : lc46_全排列.py
# Created by: julse@qq.com
# Created on: 2021/7/23 23:56
# des : TODO

# '''
# 内置函数超时
# 7.26日再次运行通过
# '''
# import itertools
# class Solution:
#     def permute(self, nums):
#         return [x for x in itertools.permutations(nums)]


'''
节点加入：深度优先 DFS
候选者用集合表示
当 nums = [0,-1,1] 时，pycharm编译器和网站提交时给出的结果不一样

pycharm

# DFS  {0, 1, -1}, DFS  {1, -1}, DFS  {-1}, DFS  set(),[0, 1, -1]
# DFS  {1}, DFS  set(),[0, -1, 1]
# DFS  {0, -1}, DFS  {-1}, DFS  set(),[1, 0, -1]
# DFS  {0}, DFS  set(),[1, -1, 0]
# DFS  {0, 1}, DFS  {1}, DFS  set(),[-1, 0, 1]
# DFS  {0}, DFS  set(),[-1, 1, 0]

leetcode

# DFS  {0, 1, -1},DFS  {1, -1},DFS  {-1},DFS  set(),[0, 1, -1]
# DFS  {1},DFS  set(),[0, -1, 1]
# DFS  {0, -1},DFS  {-1},DFS  set(),[1, 0, -1]
# DFS  {-1},DFS  set(),[1, 0, -1]                                   ##### 此处调用不一致
# DFS  {0, 1},DFS  {1},DFS  set(),[-1, 0, 1]
# DFS  {0},DFS  set(),[-1, 1, 0]
'''
# from copy import deepcopy
#
#
# class Solution:
#     def permute(self,nums):
#         self.nums = nums
#         self.all_subs = []
#         self.DFS(set(nums),[])
#         return self.all_subs
#     def DFS(self,candidates,subset):
#         if len(subset)==len(self.nums):
#             self.all_subs.append(subset[:])
#             return
#         n = len(candidates)
#         for i in range(n):
#             elem = candidates.pop()
#             subset.append(elem)
#             self.DFS(deepcopy(candidates),subset)
#             candidates.add(elem)
#             subset.pop()



'''
节点加入：深度优先 DFS
'''

# class Solution:
#     def permute(self,nums):
#         self.nums = nums
#         self.all_subs = []
#         self.DFS([0 for i in range(len(nums))],[])
#         return self.all_subs
#
#     def DFS(self,visited,subset):
#         if len(subset)==len(self.nums):
#             self.all_subs.append(subset[:])
#             return
#         for i in range(len(self.nums)):
#             if visited[i] == 1:continue
#             visited[i] = 1
#             elem = self.nums[i]
#             subset.append(elem)
#             self.DFS(visited,subset)
#             subset.pop()
#             visited[i] = 0


'''
节点加入：BFS
'''
# from queue import Queue
# class Solution:
#     def permute(self,nums):
#         self.nums = nums
#         self.all_subs = []
#         self.BFS()
#         return self.all_subs
#     def BFS(self):
#         q = Queue()
#         q.put([])
#         while(not q.empty()):
#             node = q.get()
#             if len(node)==len(self.nums):
#                 self.all_subs.append(node[:])
#                 continue
#             for i in range(len(self.nums)):
#                 if self.nums[i] in node:continue
#                 node.append(self.nums[i])
#                 q.put(node[:])
#                 node.pop()



'''
交换 BFS
'''

# class Solution:
#     def permute(self,nums):
#         self.nums = nums
#         self.all_subs = []
#         self.DFS(0)
#         return self.all_subs
#
#     def DFS(self,i):
#         if i == len(self.nums)-1:
#             self.all_subs.append(self.nums[:])
#             return
#         for j in range(i,len(self.nums)):
#             self.nums[i],self.nums[j] = self.nums[j],self.nums[i]
#             self.DFS(i+1)
#             self.nums[i],self.nums[j] = self.nums[j],self.nums[i]

'''
交换 DFS

长度为3
i=0 n_ndoe = 1 j = 0,1,2
i=1 n_node = n_ndoe * len(j) = 1*3 = 3, j= 1,2
i=2 n_node = n_node * len(j) = 3 * 2 = 6 , j = 2
'''
# class Solution:
#     def permute(self,nums):
#         self.nums = nums
#         self.all_subs = []
#         self.BFS()
#         return self.all_subs
#
#     def BFS(self):
#         from queue import Queue
#         q = Queue()
#         q.put(self.nums)
#         i = 0
#         n_node = len(self.nums) # 第i+1层结点数目
#         if n_node ==1:
#             self.all_subs.append(self.nums[0])
#             return
#         while not q.empty():
#             subset = q.get()
#             for j in range(i,len(subset)):
#                 subset[i],subset[j] = subset[j],subset[i]
#                 if i == len(self.nums)-2:self.all_subs.append(subset[:])
#                 else:
#                     q.put(subset[:])
#                 subset[i],subset[j] = subset[j],subset[i]
#             if q.qsize() == n_node:
#                 i+=1
#                 n_node = n_node * (len(self.nums) - i)

if __name__ == '__main__':
    # nums = ['a', 'b', 'c']
    nums = [0,-1,1]
    # nums = [1,2,3]
    ans = Solution().permute(nums)

    # myset = set(nums)
    # while(myset):
    #     print(myset.pop(),end=',')
    # print('\n###############')
    # myset = set(nums)
    # for x in nums:
    #     myset.add(x)
    # while(myset):
    #     print(myset.pop(),end=',')



