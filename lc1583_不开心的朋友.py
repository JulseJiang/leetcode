# Title     : lc1538_不开心的朋友.py
# Created by: julse@qq.com
# Created on: 2021/8/25 10:31
# des : TODO
import collections


class Solution:
    def unhappyFriends(self, n: int, preferences, pairs) -> int:
        mydic = {}
        ans = 0
        for i in range(n):
            mydic[i] = {}
            for idx, x in enumerate(preferences[i]):
                mydic[i][x]= n - idx
        gs = {}
        for x,y in pairs:
            gs[x]=y
            gs[y]=x
        for x in range(n):
            y = gs[x]
            uvs = set(range(n)) ^ set([x, y])
            for u in uvs:
                v= gs[u]
                if mydic[x][u]>mydic[x][y] and mydic[u][x]>mydic[u][v]:
                    ans +=1
                    break
        return ans
# n = 4
# preferences = [[1,3,2],[2,3,0],[1,0,3],[1,0,2]]
# pairs = [[2,1],[3,0]]


# n = 4
# preferences = [[1,3,2],[2,3,0],[1,3,0],[0,2,1]]
# pairs = [[1,3],[0,2]]
# ans = 4


n,preferences,pairs = [6,
[[3,2,4,5,1],[3,4,2,0,5],[5,0,3,1,4],[2,0,4,5,1],[2,3,5,0,1],[1,4,3,0,2]],
[[5,3],[4,2],[0,1]]]
ans = 4

ans = Solution().unhappyFriends(n,preferences,pairs)
print(ans)