# Title     : lc141_链表找环.py
# Created by: julse@qq.com
# Created on: 2021/7/16 16:43
# des : 141,142 单链表找环，找相遇点，找环入口
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def solve(self, head: ListNode) -> ListNode:
        if not head:return None
        if not head.next:return None
        temp = head
        p = head
        q = head.next
        while(p.next and p.next.next):
            print(p.val,q.val,temp.val)
            if p == q:
                while(temp!=p.next):
                    temp = temp.next
                    p = p.next
                return q.next
            p = p.next
            q = q.next.next
        return None


if __name__ == '__main__':
    nodes = [-1,-7,7,-4,19,6,-9,-5,-2,-5]
    pos = 5
    head = ListNode(nodes[0])
    tail = head
    for x in nodes[1:]:
        newnode = ListNode(x)
        tail.next = newnode
        tail = newnode
    entry = head
    for i in range(pos):
        entry = entry.next
    tail.next = entry

    ans = Solution().solve(head)
    print(ans.val,nodes[pos])