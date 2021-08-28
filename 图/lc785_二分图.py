# Title     : lc785.py
# Created by: julse@qq.com
# Created on: 2021/8/9 16:26
# des :
# '''
#
# solve 1 超时
# '''
# from copy import deepcopy
#
# memor = {}
# def solve1(graph):
#     A = set()
#     B = set()
#     return DFS(graph, A, B, 0)
#
# count =0
# def DFS(graph,A,B,i):
#     # print(i)
#     if i==37:
#         global count
#         count +=1
#         print(count)
#
#     if i==len(graph):return True
#     AA = deepcopy(A)
#     BB = deepcopy(B)
#     l=r=False
#
#     flag = True
#     for v in graph[i]:
#         if v in AA:
#             flag=False
#             break
#     if flag:
#         AA.add(i)
#         l = DFS(graph, AA, BB, i+1)
#         if l:return l
#
#     AA = deepcopy(A)
#     BB = deepcopy(B)
#
#     flag = True
#     for v in graph[i]:
#         if v in BB:
#             flag = False
#             break
#     if flag:
#         BB.add(i)
#         r = DFS(graph, AA, BB, i + 1)
#
#     return l or r

# '''
# 并查集
# solve 2
# '''
# def solve2(graph):
#     N = len(graph)
#     dad = [0]*N
#     # init
#     for i in range(N):
#         dad[i] = i
#     # 合并兄弟
#     for u in range(N):
#         for v in graph[u]:
#             if find(dad,u) == find(dad,v):return False
#             union(dad,graph[u][0],v) #
#     return True
#
# def find(dad,i):
#     if dad[i]!=i:
#         dad[i] = find(dad,dad[i])
#     return dad[i]
# def union(dad,x,y):
#     x = find(dad,x)
#     y = find(dad,y)
#     dad[y]=x

# box = [[],[]]
# def solve3(graph):
#     N = len(graph)
#     visited = [False] * N
#     for i in range(N): # 遍历多个子图
#         if visited[i]:continue
#         if not DFS(graph,visited,i,1):return False
#     return True
# def DFS(graph,visited,i,lr):
#     if visited[i]==True: return i in box[lr]
#     box[lr].append(i)
#     visited[i]=True
#     for v in graph[i]:
#         if not DFS(graph,visited,v,1-lr):return False
#     return True


box = [[],[]]
def solve4(graph):
    N = len(graph)
    visited = [False] * N
    from queue import Queue
    q = Queue()
    for i in range(N): # 遍历多个子图
        if visited[i]:continue
        lr =0
        q.put([i])
        while(not q.empty()):
            us = q.get()
            vs = []
            for u in us:
                if visited[u]:continue
                visited[u]=True
                box[lr].append(u)
                for v in graph[u]:
                    if not visited[v]:
                        vs.append(v)
                    else:
                        if v in box[lr]:return False
            if vs !=[]:q.put(vs)
            lr = 1 -lr
    return True


# graph = [[1,2,3],[0,2],[0,1,3],[0,2]]  # 合并成1个节点
graph = [[1,3],[0,2],[1,3],[0,2]] # 合并成2个节点
# 合并成4个节点
# graph = [[47],[48],[52,58,62],[77,84],[9,13,24,73],[15,41,47,49,55,68,83,85,88],[72],[10,37,57,79],[12,14,42,58],[4,26,65,74],[7,26,33,37],[41,53,83,90],[8],[4,68,81],[8,86],[5,19,51,54,96],[39,81],[47,74,76],[55,60,64,77],[15,23,44,74,88,90,91],[22,39,57,72],[59,77],[20,48],[19,59,90,92,98],[4,84,87],[43,63,81,90,91,92],[9,10,64,84,91],[42,54],[54,83,87],[36,45,77],[59],[32,40,52,57],[31,65],[10,79],[35,46,62,70,89,91],[34,70],[29,78],[7,10,43,75,99],[55,56],[16,20,65,74],[31,42,58,63],[5,11,45,63],[8,27,40,65,72,78],[25,37],[19,53],[29,41,66,97],[34],[0,5,17,59,66,91],[1,22,81],[5,55,64,78,98],[68,71],[15,52,87,97],[2,31,51,91],[11,44,54,66,70,74],[15,27,28,53],[5,18,38,49,63,83],[38,69,75],[7,20,31],[2,8,40,90],[21,23,30,47,67,96],[18,84],[],[2,34],[25,40,41,55],[18,26,49],[9,32,39,42],[45,47,53,96,99],[59,70,77],[5,13,50],[56,83,89,94],[34,35,53,67],[50,83,85],[6,20,42],[4,83],[9,17,19,39,53],[37,56],[17],[3,18,21,29,67,90],[36,42,49,83],[7,33,90],[90,91],[13,16,25,48,99],[],[5,11,28,55,69,71,73,78,90],[3,24,26,60],[5,71],[14],[24,28,51],[5,19,93],[34,69],[11,19,23,25,58,77,79,80,83,92],[19,25,26,34,47,52,80],[23,25,90],[88,95],[69,96],[93,99],[15,59,66,94],[45,51],[23,49],[37,66,81,95]]
# 合并成三个节点，根节点4和孤立节点1可以合并
# graph = [[4],[],[4],[4],[0,2,3]]
# 孩子没有兄的的时候没法合并
# graph = [[1],[0],[4],[4],[2,3]]
# graph = [[4,1],[0,2],[1,3],[2,4],[3,0]]
# graph = [[3],[2,4],[1],[0,4],[1,3]]
# ans = solve1(graph) # 超时
# ans = solve2(graph)
ans = solve4(graph)


