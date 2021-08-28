# Title     : lc95_二叉树种数2.py
# Created by: julse@qq.com
# Created on: 2021/8/26 17:28
# des : TODO
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
有问题
'''
# class Solution:
#     def generateTrees(self, n: int):
#         ans = []
#         usedNode = [n]
#
#         def dfs(node, nodes, curt, curroot):
#             if usedNode[0] == 0:
#                 ans.append(cptr(curroot))
#                 return
#             lnode = []
#             rnode = []
#             for i, d in enumerate(nodes):
#                 if d < node:
#                     lnode.append(d)
#                 else:
#                     rnode.append(d)
#             if lnode == []: lnode = [-1]
#             for i, d in enumerate(lnode):
#                 if d != -1:
#                     lnode.pop(i)
#                     usedNode[0] -= 1
#                     root = TreeNode(d)
#                     curt.left = root
#                     dfs(d, lnode, root, curroot)
#
#                 for i1, d1 in enumerate(rnode):
#                     rnode.pop(i1)
#                     usedNode[0] -= 1
#                     root = TreeNode(d1)
#                     curt.right = root
#                     dfs(d1, rnode, root, curroot)
#                     rnode.insert(i1, d1)
#                     usedNode[0] += 1
#                 if d!=-1:
#                     lnode.insert(i, d)
#                     usedNode[0] += 1
#         def cptr(root):
#             if root == None: return None
#             cproot = TreeNode(root.val)
#             cproot.left = cptr(root.left)
#             cproot.right = cptr(root.right)
#             return cproot
#
#         nodes = list(range(1, n + 1))
#         for i in range(n):
#             i = 2
#             node = nodes.pop(i)
#             usedNode[0] -= 1
#             root = TreeNode(node)
#             dfs(node, nodes, root, root)
#             nodes.insert(i, node)
#             usedNode[0] += 1
#         return ans


# class Solution:
#     def generateTrees(self, n: int):
#         usedNode = [n]
#         def dfs(node,lnodes,rnodes):
#             for i in range(node):
#
#         def cptr(root):
#             if root == None: return None
#             cproot = TreeNode(root.val)
#             cproot.left = cptr(root.left)
#             cproot.right = cptr(root.right)
#             return cproot

n = 3
n = 4
# ans = Solution().generateTrees(n)