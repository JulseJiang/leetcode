# Title     : lc236_最近公共祖先.py
# Created by: julse@qq.com
# Created on: 2021/8/20 16:59
# des : TODO


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         nums = []
#         def f(root,p,q):
#             if not root:return 0
#             r1 = f(root.left,p,q)
#             if r1 == 3: return 3
#             r2 = f(root.right,p,q)
#             if r2 == 3: return 3
#             ans = 1 if root == p else 2 if root == q else 0
#             r3 = r1+r2 + ans
#             if r3 == 3:nums.append(root)
#             return r1+r2 + ans
#         f(root, p, q)
#         return nums[0]


# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         def f(root,p,q):
#             if not root:return 0
#             r1 = f(root.left,p,q)
#             if not isinstance(r1,int): return r1
#             r2 = f(root.right,p,q)
#             if not isinstance(r2,int): return r2
#             ans = 1 if root == p else 2 if root == q else 0
#             r3 = r1+r2 + ans
#             if r3 == 3:return root
#             return r1+r2 + ans
#         return f(root, p, q)


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def f(root,p,q):
            if not root:return None
            if root == p or root == q:return root
            r1 = f(root.left,p,q)
            if not r1:return None
            r2 = f(root.right,p,q)
            if not r2:return None
            return root
        return f(root, p, q)



def bfs(btree,i):
    if i >= len(btree):return None
    if btree[i] == None:return None
    root = TreeNode(btree[i])
    root.left = bfs(btree, 2*i+1)
    root.right = bfs(btree, 2 * i + 2)
    return root
def bfs_f(root,val):
    if not root:return None
    if root.val == val:return root
    r1 = bfs_f(root.left,val)
    if r1: return r1
    r2 = bfs_f(root.right,val)
    if r2:return r2

# root = TreeNode(1)
# root.right = TreeNode(2)


btree = [3,5,1,6,2,0,8,None,None,7,4]
p = 5
q = 4
root = bfs(btree,0)

p = bfs_f(root,p)
q = bfs_f(root,q)
ans = Solution().lowestCommonAncestor(root,p,q)
print(ans.val)