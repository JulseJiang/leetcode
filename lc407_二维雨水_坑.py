# Title     : lc407.py
# Created by: julse@qq.com
# Created on: 2021/7/13 16:21
# des : 二维雨水
# class Solution:
#
#     def solve(self, height):
#         # 找最大的桶，装水
#         ans = 0
#         # 找墙 小于3*3 只有墙，没有容器
#         if len(height)<3:return 0
#         if len(height[0])<3:return 0
#         m = len(height)
#         n = len(height[0])
#         import heapq
#         w = []
#         # v =  [[0]*n]*m  # 会是一个相同的地址被存储n遍，每次修改其中一个的时候，其他的也会被改掉。
#         v = [[True for i in range(n)] for i in range(m)]
#         i = 0
#         for j in range(n):
#             v[i][j] = False
#             heapq.heappush(w,(height[i][j],i,j))
#         i = m-1
#         for j in range(n):
#             v[i][j] = False
#             heapq.heappush(w,(height[i][j],i,j))
#         j = 0
#         for i in range(1,m-1):
#             v[i][j] = False
#             heapq.heappush(w,(height[i][j],i,j))
#         j = n-1
#         for i in range(1,m-1):
#             v[i][j] = False
#             heapq.heappush(w,(height[i][j],i,j))
#
#         # 找容器
#         # [1:m-2,1:n-2]
#         while(w!=[]):
#             min_w = heapq.heappop(w)
#             # 前后左右
#             i = min_w[1]
#             j = min_w[2]
#             # 非墙 有些地方会被算两遍
#             for p,q in [[1,0],[-1,0],[0,1],[0,-1]]:
#                 # if i+p>0 & j+q>0 & i+p<n-1 & j+q<m-1 & v[i+p][j+q] :
#                 if i+p>0 and j+q>0 and i+p<m-1 and j+q<n-1 and v[i+p][j+q]:
#                     if min_w[0] > height[i+p][j+q]:
#                         ans += min_w[0] - height[i+p][j+q]
#                         heapq.heappush(w, (min_w[0], i+p,j+q))
#                     else:
#                         heapq.heappush(w, (height[i+p][j+q], i+p,j+q))
#                     v[i+p][j+q] = False
#         return ans


# 坑




class Solution:
    dig = set()
    def solve(self, height):
        self.height = height
        # 找最大的桶，装水,能装水的是坑，坑和坑挨着算一个

        # 找墙 小于3*3 只有墙，没有容器
        if len(height)<3:return 0
        if len(height[0])<3:return 0
        m = len(height)
        n = len(height[0])
        import heapq
        w = []
        v = [[False for i in range(n)] for i in range(m)] # 图里面，一般未访问过的地方标记False

        i = 0
        for j in range(n):
            v[i][j] = True
            heapq.heappush(w,(height[i][j],i,j))
        i = m-1
        for j in range(n):
            v[i][j] = True
            heapq.heappush(w,(height[i][j],i,j))
        j = 0
        for i in range(1,m-1):
            v[i][j] = True
            heapq.heappush(w,(height[i][j],i,j))
        j = n-1
        for i in range(1,m-1):
            v[i][j] = True
            heapq.heappush(w,(height[i][j],i,j))

        # 找容器
        # [1:m-2,1:n-2]
        while(w!=[]):
            min_w = heapq.heappop(w)
            # 前后左右
            i = min_w[1]
            j = min_w[2]
            # 非墙 有些地方会被算两遍,所以要visit数组记录被访问过的地方
            for p,q in [[1,0],[-1,0],[0,1],[0,-1]]:
                new_i = i+p
                new_j = j+q
                # if i+p>0 & j+q>0 & i+p<n-1 & j+q<m-1 & v[i+p][j+q] :
                # if new_i>0 and new_j>0 and new_i<m-1 and new_j<n-1 and  v[new_i][new_j]:
                if 0<new_i<m-1 and 0<new_j<n-1 and not v[new_i][new_j]:
                    if min_w[0] > height[new_i][new_j] and height[new_i][new_j] not in self.dig:# 此处有坑，坑位号记录下来
                        # global dig
                        self.dig.add((new_i,new_j))
                        # ans += 1
                        heapq.heappush(w, (min_w[0], new_i,new_j))
                    else:
                        heapq.heappush(w, (height[new_i][new_j], new_i,new_j))
                    v[new_i][new_j] = True

        '''
        算坑的数目
        '''
        # ans = self.BFS(m,n)
        ans = self.DFS(m,n)
        return ans


    def BFS(self,m,n):
        '''
        广度优先
        :return:
        '''
        ans = 0 # 联通坑的数目
        v = [[False for i in range(n)] for i in range(m)]
        from queue import Queue
        for i in range(m):
            for j in range(n):
                if (i,j) not in self.dig or v[i][j]:continue
                que = Queue(maxsize=m*n)
                que.put((i, j))
                v[i][j] = True
                while(not que.empty()):
                    node = que.get()
                    for p,q in [[1,0],[-1,0],[0,1],[0,-1]]:
                        new_i = node[0]+p
                        new_j = node[1]+q
                        if 0<new_i<m-1 and 0<new_j<n-1 and not v[new_i][new_j] and (new_i,new_j) in self.dig:
                            que.put((new_i, new_j))
                            v[new_i][new_j] = True
                ans+=1
        return ans
    def DFS(self,m,n):
        '''
        深度优先
        :return:
        '''
        ans = 0 # 连通坑的数目
        self.v = [[False for i in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if (i, j) not in self.dig or self.v[i][j]:continue
                self.v[i][j] = True
                self.doDFS(i, j, m, n)
                ans+=1
        return ans

    def doDFS(self,i,j,m,n):
        for p, q in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            new_i = i + p
            new_j = j + q
            if 0 < new_i < m - 1 and 0 < new_j < n - 1 and not self.v[new_i][new_j] and (new_i, new_j) in self.dig:
                self.v[new_i][new_j] = True
                return self.doDFS(new_i, new_j, m, n)

if __name__ == '__main__':
    mydict = {}
    # prices =  [0,1,0,2,1,0,1,3,2,1,2,1]

    # dig = 2, 深度优先算出来是3，还要改
    # prices =  [
    #   [1,4,3,1,3,2],
    #   [3,2,1,3,2,4],
    #   [2,3,3,2,3,1],
    # ]

    # dig = 2
    prices = [
        [1, 4, 3, 1, 3, 2],
        [3, 2, 1, 0, 2, 4],
        [2, 3, 3, 2, 3, 1],
    ]
    ans = Solution().solve(prices)
    print(ans)
