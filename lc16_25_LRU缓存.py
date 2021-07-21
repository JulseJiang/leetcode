# Title     : lc16_25_LRU缓存.py
# Created by: julse@qq.com
# Created on: 2021/7/16 22:51
# des : TODO

class Node:
    def __init__(self,k,v):
        self.k = k
        self.v = v
        self.next = None
        self.pre = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.containers = {}
        self.count = 0
        self.header = Node(None,0)
        self.tail = Node(None,0)

        self.header.next = self.tail
        self.tail.pre = self.header


    def get(self, key: int) -> int:
        if key in self.containers.keys():
            node = self.containers[key]
            if self.header.next == node:return self.containers[key].v
            self.delete(node)
            node = self.insert(node)
            self.containers[key] = node
            return self.containers[key].v
        else:return -1

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key in self.containers.keys():
            old_node = self.containers[key]
            self.delete(old_node)
            node = self.insert(node)
        else:
            if self.count <self.capacity:
                self.count += 1
            else:
                # delete node near tail
                delete_node = self.delete(self.tail.pre)
                self.containers.pop(delete_node.k)
            node = self.insert(node)
        self.containers[key] = node

        pass
    def delete (self,node:Node):
        node.pre.next = node.next
        node.next.pre = node.pre
        return node
    def insert(self,node:Node):
        # if not self.header.next: # empyty
        #     self.header.next = node
        #     node.pre = self.header
        # else:
        node.next = self.header.next
        node.pre = self.header
        self.header.next = node
        node.next.pre = node
        return node
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


#
if __name__ == '__main__':
    opr =  ["LRUCache", "put", "put", "get", "put", "put", "get"]
    data = [[2], [2, 1], [2, 2], [2], [1, 1], [4, 1], [2]]
    # [null,null,null,2,null,null,-1]
    capacity = data[0][0]
    obj = LRUCache(capacity)
    print(None,end=',')
    for idx in range(1,len(data)):
        if opr[idx] == 'put': print(obj.put(data[idx][0],data[idx][1]),end=',')
        else:
            print(obj.get(data[idx][0]),end=',')


