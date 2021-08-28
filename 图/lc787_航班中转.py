# Title     : lc787_航班中转.py
# Created by: julse@qq.com
# Created on: 2021/8/24 16:21
# des : TODO

'''
超时
'''
# import functools
#
#
# class Solution:
#     def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int) -> int:
#         # 转图
#         graph = {}
#         for u,v,e in flights:
#             if u not in graph:graph[u]={}
#             graph[u][v] = e
#         @functools.lru_cache()
#         def dfs(node,via=-1):
#             if via == k:return float('inf')
#             if node == dst:return 0
#             if node not in graph:return float('inf')
#             return min([graph[node][tpnode]+(dfs(tpnode,via+1) if tpnode!=dst else 0) for tpnode in graph[node]])
#         ans = dfs(src)
#         return -1 if ans ==float('inf') else ans


# n = 3
# flights = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0
# dst = 2
# k = 0

# class Solution:
#     def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int) -> int:
#         if k==0:return -1
#         graph = {}
#         for u,v,e in flights:
#             if v not in graph:graph[v]={}
#             graph[v][u] = e
#         if k==1:return graph[dst][src]
#         # f[t][i] 表示通过恰好 t 次航班，从出发城市 src 到达城市i需要的最小花费
#         # f[t][i] = f[t-1][j]+cost(j->i)
#         f = [[float('inf')]*n for _ in range(k)]
#         f[0] = [graph[i][src] if i in graph and src in graph[i] else float('inf') for i in range(n)]
#         for t in range(1,k):
#             for i in range(n):
#                 if i not in graph:continue
#                 f[t][i] = min([f[t-1][j]+graph[i][j] for j in graph[i]],default=float('inf'))
#         return f[k-1][dst]

class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int) -> int:
        graph = {}
        for u,v,e in flights:
            if v not in graph:graph[v]={}
            graph[v][u] = e
        # f[t][i] 表示通过恰好 t 次航班，从出发城市 src 到达城市i需要的最小花费
        # f[t][i] = f[t-1][j]+cost(j->i)
        f = [[float('inf')]*n for _ in range(k+1)]
        f[0] = [graph[i][src] if i in graph and src in graph[i] else float('inf') for i in range(n)]
        for t in range(1,k+1):
            for i in graph:
                f[t][i] = min([graph[i][j]+(f[t-1][j] if j!=src else 0) for j in graph[i]],default=float('inf'))
        ans = f[k][dst]
        return -1 if ans == float('inf') else ans
n = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1

# n = 5
# edges = [[0,1,10],[1,2,10],[1,3,2000],[2,4,10],[4,3,10],[2,3,10]]
# src = 0
# dst = 4
# k = 0


# n = 3
# edges = [[0,1,2],[1,2,1],[2,0,10]]
# src = 1
# dst = 2
# k = 1
# ans = Solution().findCheapestPrice(n,edges, src,dst, k)
# print(ans)

ln = 10
print(str(ln))
print()