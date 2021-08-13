# Title     : lc847最短路径_无向图_重复节点.py
# Created by: julse@qq.com
# Created on: 2021/8/2 23:33
# des : https://leetcode-cn.com/problems/shortest-path-visiting-all-nodes/
# '''
# 比特位状态+BFS+动态规划 通过
# '''
import collections


def solve1(graph):
    N = len(graph)
    q = collections.deque([[1<<i,i] for i in range(N)])
    dist = collections.defaultdict(lambda :N*N)
    for i in range(N):dist[1<<i,i]=0
    while q:
        cover,i = q.popleft()
        d = dist[cover,i]
        if cover==2**N-1:
            # print(showCover(cover),i,d)
            return d
        for c in graph[i]:
            cover2 = cover | 1<<c
            # print('########################')
            # print(showCover(cover),i,d)
            # print(showCover(cover2),c,min(d+1,dist[cover2, c]))
            if d+1<dist[cover2,c]:
                dist[cover2, c] = d+1
                q.append([cover2,c])

'''
比特位状态+DFS+动态规划 超时
'''
import collections
def solve2(graph):
    N = len(graph)
    dist = collections.defaultdict(lambda :N*N)
    for i in range(N):dist[1<<i,i]=0
    for i in range(N):
        DFS(graph, dist, 1 << i, i)
    distance = [dist[2**N-1, i] for i in range(N)]
    return min(distance)
def DFS(graph,dist,cover,i):
    N = len(graph)
    if cover == 2 ** N - 1: return
    d = dist[cover, i]
    for c in graph[i]:
        cover2 = cover | 1 << c
        if d + 1 <= dist[cover2, c]:
            dist[cover2, c] = d + 1
            DFS(graph,dist,cover2, c)

'''
带备忘录递归
@lru_cache

得出错误结果：原因可能如下：

缓存不是很合理，这道题一直在更新dist,这样直接根据cover i 进行剪枝不太合理
'''
# import collections
# from functools import lru_cache
# graph = [[]]
# dist = {}
# def solve3(graph1):
#     global graph,dist
#     graph = graph1
#
#     N = len(graph)
#     dist = collections.defaultdict(lambda :N*N)
#     for i in range(N):dist[1<<i,i]=0
#     DFS(0,0)
#     distance = [dist[2**N-1, i] for i in range(N)]
#     return min(distance)
# @lru_cache(None)
# def DFS(cover,i):
#     N = len(graph)
#     if cover == 0:
#         for i in range(N):
#             DFS(1 << i, i)
#         return
#     if cover == 2 ** N - 1: return
#     d = dist[cover, i]
#     for c in graph[i]:
#         cover2 = cover | 1 << c
#         if d + 1 <= dist[cover2, c]:
#             dist[cover2, c] = d + 1
#             DFS(cover2, c)

'''
打印cover情况
'''
def showCover(cover):
    bicover = bin(cover)[2:]
    bicovers = []
    for j in range(len(bicover)):
        if bicover[j] == '1': bicovers.append(len(bicover)-j-1)
    return bicovers
# main
'''
狼牙数组表示图
'''
# graph = [[1],[0]] #1
# graph = [[1,2,3],[0],[0],[0]] #4
graph = [[1,2,3],[0,2],[0],[0]] #3
# graph = [[1],[0,2,4],[1,3,4],[2],[1,2]] #4
ans1 = solve1(graph)
# ans2 = solve2(graph)
# ans3 = solve3(graph)   # graph = [[1,2,3],[0,2],[0],[0]] #5 错误



