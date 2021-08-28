# Title     : lc199_二叉树右视图_层次_RLH.py
# Created by: julse@qq.com
# Created on: 2021/8/23 20:56
# des : TODO


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        memor = {}
        def RLH(root,h):
            if not root:return root
            RLH(root.right,h+1)
            RLH(root.left,h+1)
            if h not in memor:memor[h] = root.val
        RLH(root,0)
        return [memor[x] for x in sorted(memor.keys())]

class Solution:
    def rightSideView(self, root) -> list[int]:
        ans = []
        def layer(root):
            qs = [root]
            while qs:
                ans.append(qs[-1].val)
                child = []
                for q in qs:
                    if q.left:child.append(q.left)
                    if q.right:child.append(q.right)
                qs = child
        layer(root)
        return ans

def bfs(btree,i):
    if i >= len(btree):return None
    if btree[i] == None:return None
    root = TreeNode(btree[i])
    root.left = bfs(btree, 2*i+1)
    root.right = bfs(btree, 2 * i + 2)
    return root

btree = [1,2,3,None,5,None,4]
root = bfs(btree,0)

ans = Solution().rightSideView(root)
print(ans)