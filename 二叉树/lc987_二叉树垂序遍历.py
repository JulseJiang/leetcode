# Title     : lc987_二叉树垂序遍历.py
# Created by: julse@qq.com
# Created on: 2021/8/28 18:52
# des : TODO
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode):
        mydic = {}
        def layer(root):
            q = [(0,0,root)]
            while q:
                tp = []
                for a,b,x in q:
                    if b not in mydic:mydic[b]={}
                    if a not in mydic[b]:mydic[b][a] = []
                    mydic[b][a].append(x.val)
                    if x.left:tp.append((a+1,b-1,x.left))
                    if x.right:tp.append((a+1,b+1,x.right))
                q = tp[:]
        layer(root)
        ans = []
        for b in sorted(mydic):
            tp = []
            for a in sorted(mydic[b]):
                for x in sorted(mydic[b][a]):
                    tp.append(x)
            ans.append(tp)
        return ans


def bfs(btree,i):
    if i >= len(btree):return None
    if btree[i] == None:return None
    root = TreeNode(btree[i])
    root.left = bfs(btree, 2*i+1)
    root.right = bfs(btree, 2 * i + 2)
    return root

btree = [3,9,20,None,None,15,7]
btree = [0,None,1]
root = bfs(btree,0)
ans = Solution().verticalTraversal(root)
print(ans)