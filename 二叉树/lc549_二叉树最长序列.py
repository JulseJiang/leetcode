# Title     : lc549_二叉树最长序列.py
# Created by: julse@qq.com
# Created on: 2021/8/20 18:08
# des : TODO

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# Definition for a binary tree node.
class MapNode:
    def __init__(self, x,left=None,right=None,papa=None):
        self.val = x
        self.left = left
        self.right = right
        self.papa = papa
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode'):
#         rootmap = MapNode(root.val)
#         def dfs(root: 'TreeNode',papa: 'MapNode',isleft:int):
#             if not root:return
#
#             mn = MapNode(root.val,papa = papa)
#             if isleft == 1:papa.left = mn
#             elif isleft ==2: papa.right = mn
#
#             dfs(root.left)
#             dfs(root.right)
#         dfs(root,rootmap,0)


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode'):
        rootmap = MapNode(root.val)
        maxtp = [float('-inf')]
        maps = []
        '''
        双向改成三向
        treenode -> mapnode
        '''
        def dfs(root: 'TreeNode', papa: 'MapNode'):
            if not root:return None
            mn = MapNode(root.val, papa=papa)
            mn.left = dfs(root.left,mn)
            mn.right = dfs(root.right,mn)
            if mn:maps.append(mn)
            return mn
        def search(start: 'MapNode',preval,culen:int):
            '''
            :param start: 起始节点
            :param preval: 上一个值
            :param acend: 升序 True 还是降序 False
            :return:
            '''
            if not start:return
            cuval = start.val
            if preval - cuval == 1:
                search(start.papa, cuval,culen+1)
                search(start.left, cuval,culen+1)
                search(start.right, cuval,culen+1)
            else:
                maxtp[0] = max(maxtp[0],culen)
        # mn = dfs(root, rootmap, 0)
        dfs(root, rootmap)
        for m in maps:
            search(m, m.val+1,0)
        return maxtp[0]




# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(3)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(5)


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

ans = Solution().lowestCommonAncestor(root)
print(ans)