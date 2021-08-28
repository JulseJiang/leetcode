# Title     : lc552_学生出勤.py
# Created by: julse@qq.com
# Created on: 2021/8/18 20:45
# des : TODO
'''
DFS
'''
# class Solution:
#     def checkRecord(self, n: int) -> int:
#         import functools
#         @functools.lru_cache(None)
#         def DFS(i,ca,cl):
#             if ca == 2:return 0
#             if cl == 3:return 0
#             if i == n :return 1
#             return sum(
#                 [DFS(i+1,ca+1,0),
#                 DFS(i+1,ca,cl+1),
#                 DFS(i+1,ca,0)]
#             )%(pow(10,9)+7)
#         return DFS(0,0,0)

'''
DP


安全状态


A   第i天缺席
L with L0 with A0       第i天迟到，在0次缺席，前一天未迟到的情况下
L with L1 with A0       第i天迟到，在0次缺席，前一天迟到的情况下
L with L0 with A1       第i天迟到，在1次缺席，前一天未迟到的情况下
L with L1 with A1       第i天迟到，在1次缺席，前一天迟到的情况下
P with A0               第i天出席，在0次缺席的情况下
P with A1               第i天出席，在1次缺席的情况下
'''
class Solution:
    def checkRecord(self, n: int) -> int:
        dp = [[0]*7 for _ in range(n)]
        # dp[0] = [1,1,0,0,0,1,0]
        dpi_1 = [1,1,0,0,0,1,0]
        for i in range(1,n):
            dpi = [sum([dpi_1[j] for j in [1,2,5]])%(pow(10,9)+7),
                   dpi_1[5],
                   dpi_1[1],
                   sum([dpi_1[j] for j in [0,6]])%(pow(10,9)+7),
                   dpi_1[3],
                   sum([dpi_1[j] for j in [1,2,5]])%(pow(10,9)+7),
                   sum([dpi_1[j] for j in [0,3,4,6]])%(pow(10,9)+7)]
            dpi_1 = dpi[:]
        return sum(dpi_1)%(pow(10,9)+7)

n = 2 # 8
n = 10101 # 183236316
ans = Solution().checkRecord(n)
print(ans)
