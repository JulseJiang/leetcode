# Title     : lc576_出界的路径数.py
# Created by: julse@qq.com
# Created on: 2021/8/17 16:44
# des :

# '''
# 超时
# '''
# class Solution:
#     def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
#         # mask = [0]
#         ans = [0]
#         move = [0]
#         # i 行 j 列: i * n +j
#         def DFS(m,n,i,j):
#             if i==m or j == n or i==-1 or j == -1:
#                 ans[0] = (ans[0]+1)% (pow(10,9) + 7)
#                 return
#             # if mask[0] & 1 << (i * n + j) != 0: return
#             if move[0]>=maxMove:return
#             # mask[0] |= 1<<(i * n +j) # visited
#             for diri,dirj in [[0,1],[0,-1],[1,0],[-1,0]]:
#                 ni =i+diri
#                 nj =j+dirj
#                 move[0] += 1
#                 DFS(m, n, ni, nj)
#                 move[0] -= 1
#         DFS(m,n,startRow,startColumn)
#         return ans[0]




# '''
# 通过
# '''
# class Solution:
#     def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
#         memor = {}
#         def DFS(m,n,i,j,move):
#             if (i,j,move) in memor: return memor[(i,j,move)]
#             if move == -1:return 0
#             if i==m or j == n or i==-1 or j == -1:
#                 return 1
#             ans = 0
#             for diri,dirj in [[0,1],[0,-1],[1,0],[-1,0]]:
#                 ni =i+diri
#                 nj =j+dirj
#                 ans += DFS(m, n, ni, nj,move-1)
#             memor[(i, j, move)] = ans % (pow(10,9) + 7)
#             return ans % (pow(10,9) + 7)
#         return DFS(m,n,startRow,startColumn,maxMove)
'''
通过
'''
# import functools
#
# class Solution:
#     def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
#         @functools.lru_cache(None)
#         def DFS(m,n,i,j,move):
#             if move == -1:return 0
#             if i==m or j == n or i==-1 or j == -1:
#                 return 1
#             ans = 0
#             for diri,dirj in [[0,1],[0,-1],[1,0],[-1,0]]:
#                 ni =i+diri
#                 nj =j+dirj
#                 ans += DFS(m, n, ni, nj,move-1)
#             return ans % (pow(10,9) + 7)
#         return DFS(m,n,startRow,startColumn,maxMove)

'''
推导式
'''
# import functools
# class Solution:
#     def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
#         @functools.lru_cache(None)
#         def DFS(m,n,i,j,move):
#             return 0 if move == -1 else 1 if i==m or j == n or i==-1 or j == -1 else (sum([DFS(m, n, i+1, j,move-1),DFS(m, n, i-1, j,move-1),DFS(m, n, i, j+1,move-1),DFS(m, n, i, j-1,move-1)]))% (pow(10,9) + 7)
#         return DFS(m,n,startRow,startColumn,maxMove)
'''
动态规划
'''
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        maxMove+=1
        dp = [[[0]*maxMove for _ in range(n+2)] for _ in range(m+2)]
        for i in range(m+2):
            for j in range(maxMove):
                dp[i][0][j] = dp[i][n+1][j] = 1
        for i in range(n+2):
            for j in range(maxMove):
                dp[0][i][j] = dp[m+1][i][j] = 1
        for mm in range(1, maxMove):
            for i in range(1,m+1):
                if mm == maxMove-1 and i>startRow+1:break
                for j in range(1,n+1):
                    if mm == maxMove - 1 and j > startColumn + 1: break
                    for diri, dirj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        dp[i][j][mm] += dp[i+diri][j+dirj][mm-1]
                    dp[i][j][mm] %= (pow(10, 9) + 7)
        return (dp[startRow+1][startColumn+1][maxMove-1])


# m = 2
# n = 2
# maxMove = 2
# startRow = 0
# startColumn = 0

m = 1
n = 3
maxMove = 3
startRow = 0
startColumn = 1

# ans = 12

ans = Solution().findPaths(m,n,maxMove,startRow,startColumn)
print(ans)