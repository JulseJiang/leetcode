# Title     : 牛客网热题_反转链表.py
# Created by: julse@qq.com
# Created on: 2021/7/17 10:02
# des : TODO
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:return pHead
        qhead = ListNode(None)
        while(pHead):
            # 原链上删除，并移动头指针
            temp = pHead
            pHead = pHead.next
            # 插入到反转后的链上
            temp.next = qhead.next
            qhead.next = temp
        return qhead.next


if __name__ == '__main__':
    #  输入：
    # {1,2,3}
    # 返回值：
    # {3,2,1}

    inputs = [1,2,3]
    ans = [3,2,1]
    pHead = ListNode(None)
    temp = pHead
    for input in inputs:
        a = ListNode(input)
        temp.next = a
        temp = a
    qHead = Solution().ReverseList(pHead.next)

