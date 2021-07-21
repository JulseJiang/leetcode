# Title     : lc230_BST.py
# Created by: julse@qq.com
# Created on: 2021/7/6 21:35
# des : TODO

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def solve(self, root: TreeNode, k: int) -> int:
        self.count = 0
        self.mtree(root.right)
        return self.mtree(root,k)
    def mtree(self,root:TreeNode,k):
        if root==None:return None
        self.mtree(root.left)
        self.count = self.count +1
        if self.count==k:return root.val
        if self.count>k:return None
        self.mtree(root.right)


if __name__ == '__main__':
    mydict = {}
    prices = [3,1,4,0,2]
    ans = Solution().solve(prices)
    print(ans)
