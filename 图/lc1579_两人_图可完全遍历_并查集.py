# Title     : lc1579_两人_图可完全遍历_并查集.py
# Created by: julse@qq.com
# Created on: 2021/8/11 14:44
# des : Alice 和 Bob 共有一个无向图，其中包含 n 个节点和 3  种类型的边：

# https://blog.csdn.net/Julse/article/details/119335917?spm=1001.2014.3001.5502
# leetcode 743. 网络延迟时间- 有向图 - 图的一些小知识点
# Dijkstra and Floyd


'''
有问题：只考虑了能连通，没有考虑从某个节点开始能走通
'''
# from copy import deepcopy
# def solve1(n,edges):
#     ans = 0
#
#     C,ans= walk(edges,set(),3,ans)
#     B,ans= walk(edges,deepcopy(C),2,ans)
#     A,ans= walk(edges,deepcopy(C),1,ans)
#
#     return ans if len(list(filter(lambda x:isinstance(x,int),A)))==len(list(filter(lambda x:isinstance(x,int),B)))==n else -1
#
# def walk(edges,C,type,ans):
#     for _,n1,n2 in filter(lambda x:x[0]==type,edges):
#         if n1 in C and n2 in C and ((n1,n2) in C or (n2,n1) in C):ans+=1
#         else:
#             if n1 not in C:
#                 C.add(n1)
#             if n2 not in C:
#                 C.add(n2)
#             if (n1,n2) not in C and (n2,n1) not in C:
#                 C.add((n1,n2))
#     return C,ans


# from copy import deepcopy
# '''
# Floyd 找多源最短路径
# '''
# def solve2(n,edges):
#      pass
# def Floyd(graph):
#     '''
#     图的邻接矩阵,节点之间有边是1，没边是 inf
#     :param graph:
#     :return:
#     '''
#     N = len(graph)
#     dist = deepcopy(graph)
#     path = deepcopy(graph)
#     for i in range(N):
#         for j in range(N):
#             if graph[i][j]!=float('inf'):
#                 path[i][j] = j
#     for k in range(1,N+1):
#         for i in range(1,N):
#             for j in range(i+1,N+1):
#                 if i == k or j == k:continue
#                 if dist[i][k]+dist[k][j]<dist[i][j]:
#                     dist[i][j] = dist[i][k]+dist[k][j]
#                     path[i][j] = k


from copy import deepcopy
def solve3(n,edges):
    ans = 0
    A = [i for i in range(n+1)]
    C = A[:]
    ans = walk(edges, C, 3, ans)
    B = C[:]
    ans = walk(edges, B, 2, ans)
    A = C[:]
    ans = walk(edges, A, 1, ans)

    for i in range(1,n+1):
        find(A,i)
        find(B,i)
    return ans if len(set(A[1:]))==1 and len(set(B[1:]))==1 else -1

def find(A,x):
    if A[x]!=x:
        A[x] = find(A,A[x])
    return A[x]

def union(A,x,y):
    A[find(A,x)] = find(A,y)
def walk(edges,A,type,ans):
    for _,i,j in filter(lambda row:row[0]==type,edges):
        if find(A,i) == find(A,j):ans+=1
        else:
            union(A,i,j)
    return ans
# n = 4
# edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]

# n = 4
# edges = [[3,2,3],[1,1,2],[2,3,4]]

# n = 4
# edges = [[3,1,2], [3,3,4], [1,1,3],[2,2,4]]


# n = 4
# edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]

# n = 4
# edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]

n = 13
edges = [[1,1,2],[2,2,3],[2,3,4],[1,3,5],[3,2,6],[2,3,7],[3,7,8],[3,2,9],[2,4,10],[2,9,11],[1,2,12],[3,4,13],[2,2,7],[1,1,9],[1,2,13],[2,7,13],[3,2,3],[1,7,10],[2,8,11],[1,2,7],[2,1,9],[2,2,9],[1,5,6],[2,4,9],[1,7,8],[1,4,6],[1,4,9],[3,7,13],[2,2,8],[2,2,6],[1,1,10],[1,1,11],[2,5,10],[1,2,9],[2,1,2],[1,3,4],[3,6,8],[3,6,13],[1,3,8],[1,1,6],[3,3,9],[1,2,3],[1,11,13]]
# ans = solve1(n,edges)
# ans = solve2(n,edges)
# ans = solve3(n,edges)
# print(ans)



# def jiecheng(n):
#     if n ==1:return 1
#     return n*jiecheng((n-1))
# ans = jiecheng(5)