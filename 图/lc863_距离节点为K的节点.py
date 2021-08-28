# Title     : lc863_距离节点为K的节点.py
# Created by: julse@qq.com
# Created on: 2021/8/23 23:26
# des : TODO

    # Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
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

def layer(btree):
    if len(btree) == 0 :return None
    i=0
    root = TreeNode(btree[i])
    qs = [root]
    while qs:
        q = qs.pop(0)
        i+=1
        if len(btree)<= i : return root
        q.left = TreeNode(btree[i])
        if btree[i]:qs.append(q.left)
        i+=1
        if len(btree) <= i: return root
        q.right = TreeNode(btree[i])
        if btree[i]: qs.append(q.right)
    return root
# class Solution:
#     def distanceK(self, root, target, k: int):
#         ans = []
#         # 找到每个节点距离target的距离，如果等于K 则返回
#
#         # 找到目标节点target
#         # 找到目标节点相距K的节点
#         def dfs(root,l,r,ad = True):
#             if not root: return
#             if l+r == k:
#                 ans.append(root.val)
#                 return
#             if root == target:l = r = k
#             dfs(root.left,l-1,r)
#             dfs(root.right,l,r-1)
#             if ad:adjust(root)
#
#         def adjust(root):
#             if root.left == target:
#                 root.left = None
#                 target.left = None
#                 target.right = root
#             if root.right == target:
#                 root.right = None
#                 target.right = None
#                 target.left = root
#
#
#         dfs(root,-1,-1)
#         dfs(target,-1,-1,ad=False)
#         return ans

'''
通过
'''
class Solution:
    def distanceK(self, root, target, k: int):
        if k==0:return [target.val]
        ans = []
        # 找到每个节点距离target的距离，如果等于K 则返回

        # 找到目标节点target
        # 找到目标节点相距K的节点
        def dfs(root,l,r,papa,ad = True):
            if not root: return False
            if l+r == k:
                ans.append(root.val)
                return False
            if root == target:l = r = k
            f1 = dfs(root.left,l-1,r,root)
            f2 = dfs(root.right,l,r-1,root)
            if ad:
                adjust(root,papa)
                if f1:root.left = papa
                if f2:root.right = papa
                if root==target:
                    root.left = None
                    root.right = papa
            if root == target or f1 or f2:return True
            return False

        def adjust(root,papa):
            if root == target:
                target.left == None
                target.right = papa
        if k == 0:return [target]
        if root!=target:dfs(root,-1,-1,None)
        dfs(target,-1,-1,None,ad=False)
        return ans

# btree = [3,5,1,6,2,0,8,None,None,7,4]
# btree = [0,2,1,None,None,3]
btree = [0,1,None,None,2,None,3,None,4]
# btree = [1,2,3,None,None,4,5,None,None,None,None,None,None,6,7]
p = 3
k = 1
root = layer(btree)
# root = bfs(btree,0)
p = bfs_f(root,p)
ans = Solution().distanceK(root,p,k)
print(ans)