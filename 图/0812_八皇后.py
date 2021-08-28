# Title     : 0812_八皇后.py
# Created by: julse@qq.com
# Created on: 2021/8/6 17:50
# des : https://leetcode-cn.com/problems/eight-queens-lcci/
# # 面试题 08.12. 八皇后



# N = 0
# row = [True]*N
# col = [True]*N
# def solve1(N1):
#     global N
#     N = N1
#     ans = 0
#     marked = [[True] * N for i in range(N)]
#     hj = [j for j in range(N)]
#     D(0,hj)
# def D(k,hj): # 给第k个皇后找位置
#     if k==N:return
#     for j in hj:
#         hj1 = mark(k,j,hj)
#         D(k+1,hj1)
#
#
# '''
# 标记成不能用的
# # 1. i+j =D1
# # 2. j-i =D2
# # 3. i
# # 4. j
# '''
# def mark(i,j,hj):
#     hj1 = hj[:]
#     for j1 in hj:
#         hj1[j] = False
#     return


# N = 0
# A= []
# B = []
# C = [j for j in range(N)]
# ans = []
# def solve1(N1):
#     global N
#     N = N1
#     D(0,[])
#     return ans
# def D(k,hj): # 给第k个皇后找位置
#     global count
#     if k==N:
#         ans.append(hj[:])
#         return
#     for j in range(N):
#         if k+j not in A and j-k not in B and j not in C:
#             substr = []
#             for i in range(N):
#                 substr.append('Q' if i==j else '.')
#             hj.append(''.join(substr))
#
#             A.append(k+j)
#             B.append(j-k)
#             C.append(j)
#
#             D(k+1,hj)
#
#             A.pop()
#             B.pop()
#             C.pop()
#             hj.pop()


#
# solve1(4)
# print(ans)


class Solution:
    def solveNQueens(self, n: int):
        N = n
        A = [True]*2*N
        B = [True]*2*N
        C = [True]*N
        ans = []
        def D(k,hj): # 给第k个皇后找位置
            if k==N:
                ans.append([''.join(i) for i in hj])
                return
            for j in range(N):
                if A[k+j] and B[j-k] and C[j]:
                    hj[k][j]='Q'
                    A[k+j] = B[j-k] = C[j] = False
                    D(k+1,hj)
                    A[k+j] = B[j-k] = C[j] = True
                    hj[k][j]='.'
        D(0, [['.']*N for i in range(N)])
        return ans
ans = Solution().solveNQueens(4)
print(ans)