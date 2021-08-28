# Title     : lc530.py
# Created by: julse@qq.com
# Created on: 2021/7/6 22:19
# des : TODO

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def solve(self, root: TreeNode) -> int:
        self.ans = 0
        self.pre = 0
        self.mtree(root.right)
        return self.ans
    def mtree(self,root:TreeNode):
        if root==None:return None
        self.mtree(root.left)
        self.count = self.count +1
        self.ans = min(abs(self.pre - root.val),self.ans)
        self.pre = root.val
        self.mtree(root.right)
