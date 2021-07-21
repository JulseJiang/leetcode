# Title     : lc16_25_LRU缓存.py
# Created by: julse@qq.com
# Created on: 2021/7/16 22:51
#
# lru design
# @param operators int整型二维数组 the ops
# @param k int整型 the k
# @return int整型一维数组
#

class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.next = None
        self.pre = None


class Solution:
    def __init__(self):
        self.capacity = None
        self.containers = {}
        self.count = 0
        self.header = Node(None, 0)
        self.tail = Node(None, 0)

        self.header.next = self.tail
        self.tail.pre = self.header

    def LRU(self, operators, k):
        self.capacity = k
        # write code here
        ans = []
        for opr in operators:
            if opr[0] == 1:
                self.set(opr[1], opr[2])
            else:
                ans.append(self.get(opr[1]))
        return ans

    def get(self, key: int) -> int:
        if key in self.containers.keys():
            node = self.containers[key]
            if self.header.next == node: return self.containers[key].v
            self.delete(node)
            node = self.insert(node)
            self.containers[key] = node
            return self.containers[key].v
        else:
            return -1

    def set(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key in self.containers.keys():
            old_node = self.containers[key]
            self.delete(old_node)
            node = self.insert(node)
        else:
            if self.count < self.capacity:
                self.count += 1
            else:
                # delete node near tail
                delete_node = self.delete(self.tail.pre)
                self.containers.pop(delete_node.k)
            node = self.insert(node)
        self.containers[key] = node

    def delete(self, node: Node):
        node.pre.next = node.next
        node.next.pre = node.pre
        return node

    def insert(self, node: Node):
        node.next = self.header.next
        node.pre = self.header
        self.header.next = node
        node.next.pre = node
        return node


#
if __name__ == '__main__':
    opr =  ["LRUCache", "put", "put", "get", "put", "put", "get"]
    data = [[2], [2, 1], [2, 2], [2], [1, 1], [4, 1], [2]]
    # [null,null,null,2,null,null,-1]


    # 输入：
    # [[1,1,1],[1,2,2],[1,3,2],[2,1],[1,4,4],[2,2]],3
    # 返回值：
    # [1,-1]
    operators = [[1,1,1],[1,2,2],[1,3,2],[2,1],[1,4,4],[2,2]]
    k = 3
    ans = Solution().LRU(operators, k)
    print(ans)



