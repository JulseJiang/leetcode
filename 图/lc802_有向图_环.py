# Title     : lc802_有向图_环.py
# Created by: julse@qq.com
# Created on: 2021/8/5 14:55
# des : https://leetcode-cn.com/problems/find-eventual-safe-states/
# 找环,在环上的节点排除之后,剩下的节点就是安全路径

def solve1(graph):
    N = len(graph)
    circle = 0
    for i in range(N):
        circle |= DFS(graph,0,i,circle)
    return showCover(2**N-1 ^ circle)
#
def DFS(graph,cover,i,circle):
    cover2 = cover | 1 << i
    if (circle | 1<<i )== circle or cover == cover2:return circle|cover
    for j in graph[i]:
        circle |= DFS(graph,cover2,j,circle)
    return circle


'''
三色标记
0,1,2,3
3 是否被访问过
'''
# visited = []
# def solve2(graph):
#     global visited,safe
#     N = len(graph)
#     visited = [0 for i in range(N)]
#     DFS(-1)
#     ans = []
#     for i in range(N):
#         if visited[i]==2:
#             ans.append(i)
#     return ans
# def DFS(i):
#     if i!=-1:
#         if visited[i] ==3:
#             visited[i] = 1
#             return visited[i]
#         if visited[i]!=0:
#             return visited[i]
#         visited[i] = 3
#     N = len(graph)
#     # if :
#     if i == -1:
#         gc = [j for j in range(N)]
#     else:
#         gc = graph[i]
#     s = 2
#     for j in gc:
#         if DFS(j)==1:
#             s = 1
#     if i==-1:return 0
#     visited[i] = s
#     return visited[i]


# visited = []
# graph=[]
# def solve3(graph1):
#     global visited,safe,graph
#     graph = graph1
#     N = len(graph)
#     ans = []
#     visited = [0 for i in range(N)]
#     for i in range(N):
#         if DFS(i) == 2:
#             ans.append(i)
#     return ans
# def DFS(i):
#     if visited[i] ==3:
#         visited[i] = 1
#         return visited[i]
#     if visited[i]!=0:
#         return visited[i]
#     visited[i] = 3
#     s = 2
#     for j in graph[i]:
#         if DFS(j)==1:
#             s = 1
#     visited[i] = s
#     return visited[i]
'''
打印cover情况
'''
def showCover(cover):
    bicover = bin(cover)[2:]
    bicovers = []
    for j in range(len(bicover)-1,-1,-1):
        if bicover[j] == '1': bicovers.append(len(bicover)-j-1)
    return bicovers

'''
拓扑排序
从一个顶点开始，给所有事件排序，找满足要求的路径
a->b
完成b的前提是要完成a
在图上找一条路径
'''
def solve4(graph):
    # 出度
    cd = [len(x) for x in graph]
    g = graphReverse(graph)
    flag = True
    while flag:
        flag = False
        for i in range(len(cd)):
            if cd[i]==0:
                cd[i] = -1
                for j in g[i]:cd[j]-=1
                flag = True
    # ans = []
    # for i,x in enumerate(cd):
    #     if x == 0:
    #         ans.append(i)

    ans = [i for i in range(len(cd)) if cd[i]<=0]
    return ans

def solve5(graph):
    # 出度
    cd = [len(x) for x in graph]
    g = graphReverse(graph)
    q = [x for x in range(len(cd)) if cd[x]==0]
    while q:list(map(lambda i:func(g,cd,i,q),q))
    ans = [i for i in range(len(cd)) if cd[i]==0]
    return ans
def func(g,cd,i,q):
    q.remove(i)
    list(map(lambda j:func2(j,cd,q),g[i]))
def func2(j,cd,q):
    cd[j] -= 1
    if cd[j] == 0:
        q.append(j)
'''
狼牙数组转置
'''
def graphReverse(graph):
    # a->b b->a
    # 出度换成入度
    p = [[] for i in range(len(graph))]
    # 遍历了一遍节点和边 n+m
    for i in range(len(graph)):
        for j in graph[i]:
            p[j].append(i)
    return p
'''
list 转置
'''
def listReverse(graph):
    return [list(y) for y in zip(*graph)]

def listReverse(graph):
    # return [x for x in map(lambda x:list(x),zip(*graph))]
    return list(map(lambda x:list(x),zip(*graph)))

graph = [[1, 2], [2, 3], [5], [0], [5], [], []] # : [2, 4, 5, 6]
# graph = [[0],[2,3,4],[3,4],[0,4],[]] #4
# graph = [[1,2],[2,3],[5],[0],[5],[],[]]
ans = solve1(graph)
# ans = solve2(graph)
# ans = solve3(graph)

# graph = [[1, 2, 10], [1, 3, 2], [3, 4, 1],[2,4,2],[4,5,3]]
# ans = solve5(graph)
# ans = listReverse(graph)

