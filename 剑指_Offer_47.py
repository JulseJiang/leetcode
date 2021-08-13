# Title     : 剑指_Offer_47.py
# Created by: julse@qq.com
# Created on: 2021/8/1 20:38
# des : https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/

'''
方法1
超时
如果直接加备忘录，应该加入的是后续遍历的路径，或者是增量
'''
# price = 0
# ans = 0
# def DFS(grid,i,j):
#     global price
#     global ans
#     if i>= m or j >=n:return
#     price += grid[i][j]
#     if m==1 and n==1:
#         ans = price
#         return
#     if i+j ==m+n-2:
#         return
#     candi = [(1,0),(0,1)]
#     if i == m-1:
#         candi = [(0, 1)]
#     if j == n-1:
#         candi = [(1, 0)]
#     for a,b in candi:
#         i+=a
#         j+=b
#         DFS(grid,i,j)
#         ans = max(price,ans)
#         price -= grid[i][j]
#         i-=a
#         j-=b
from copy import deepcopy

'''
方法2
'''
# def solve(grid):
#     # grid = [[1,2,3],[4,5,6],[7,8,9]]
#     global m
#     global n
#     m = len(grid)
#     n = len(grid[0])
#     memor = {}
#     def DFS(grid, i, j):
#         '''
#         :return 某个结点后面产生的最大增量
#         :param grid:
#         :param i:
#         :param j:
#         :return:
#         '''
#         if (i, j) in memor: return memor[(i, j)]
#         if i >= m or j >= n: return 0
#         if i==m-1 and j==n-1:
#             return grid[i][j]
#         candi = [(1, 0), (0, 1)]
#         maxtp = 0
#         for a, b in candi:
#             elem = DFS(grid, i + a, j + b)
#             maxtp = max(maxtp, elem)
#         memor[(i, j)] = grid[i][j] + maxtp
#         return memor[(i, j)]
#     return DFS(grid,0,0)


'''
方法2 优化
'''
def solve(grid):
    # grid = [[1,2,3],[4,5,6],[7,8,9]]
    global m
    global n
    m = len(grid)
    n = len(grid[0])
    memor = {}
    def DFS(grid, i, j):
        '''
        :return 某个结点后面产生的最大增量
        :param grid:
        :param i:
        :param j:
        :return:
        '''
        if (i, j) in memor: return memor[(i, j)]
        if i >= m or j >= n: return 0
        if i==m-1 and j==n-1:
            return grid[i][j]
        maxtp = max(DFS(grid,i+1,j),DFS(grid,i,j+1),)+ grid[i][j]
        memor[(i, j)] = maxtp
        return memor[(i, j)]
    return DFS(grid,0,0)
'''
方法3
动态规划
'''
# def solve(grid):
#     # grid = [[1,2,3],[4,5,6],[7,8,9]]
#     global m
#     global n
#     m = len(grid)
#     n = len(grid[0])
#     dp = deepcopy(grid)
#     j=0
#     temp = 0
#     for i in range(m):
#         temp += grid[i][j]
#         dp[i][0]=temp
#     i=0
#     temp = 0
#     for j in range(n):
#         temp += grid[i][j]
#         dp[0][j]=temp
#     for i in range(1,m):
#         for j in range(1,n):
#             dp[i][j]= max(dp[i-1][j],dp[i][j-1])+grid[i][j]
#     return dp[m-1][n-1]



'''
动态规划，用原数组当作dp数组
'''
# def solve(grid):
#     # grid = [[1,2,3],[4,5,6],[7,8,9]]
#     global m
#     global n
#     m = len(grid)
#     n = len(grid[0])
#     dp = grid
#     j=0
#     temp = 0
#     for i in range(m):
#         temp += grid[i][j]
#         dp[i][0]=temp
#     i=0
#     temp = 0
#     for j in range(n):
#         temp += grid[i][j]
#         dp[0][j]=temp
#     for i in range(1,m):
#         for j in range(1,n):
#             dp[i][j]= max(dp[i-1][j],dp[i][j-1])+grid[i][j]
#     return dp[m-1][n-1]
if __name__ == '__main__':
#     grid = [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1],
#   [4,2,1]
# ]
#     # ans = 12

    grid = [
        [1]
    ]
    # ans = 1

    # grid = [[1,3,1],[1,5,1],[4,2,1]]
    # grid = [[1,3,1],[1,5,1],[4,2,1]] #12
    grid = [[1,2,5],[3,2,1]]
    # grid = [[1,2,3],[4,5,6]]
    ans = solve(grid)
    pass



