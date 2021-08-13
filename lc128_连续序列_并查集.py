# Title     : lc128_连续序列_并查集.py
# Created by: julse@qq.com
# Created on: 2021/8/10 17:37
# des : TODO

'''
o(n^2)  超时
'''
def solve1(nums):
    if len(nums)==0:return 0
    mark={}
    for idx,e in enumerate(nums):
        mark[e]=idx
    dad = list(mark.keys())
    nums = dad[:]
    mark={}
    for idx,e in enumerate(nums):
        mark[e]=idx
    flag = True
    while flag:
        flag = False
        for i in range(len(dad)):
            if nums[i]+1 in mark and dad[i]!= dad[mark[nums[i]+1]]:
                flag = True
                dad[i] = dad[mark[nums[i]+1]]
    return maxCount(dad)
def maxCount(dad):
    dic = {}
    for elem in dad:
        if elem not in dic:dic[elem] = 0
        dic[elem]+=1
    temp = float('-inf')
    for value in dic.values():
        temp = max(value,temp)
    return temp

def solve2(nums):
    nums = set(nums)
    dic = {}
    for i in nums:
        dic[i] = node(i,None,None)
    for i in nums:
        if i+1 in dic:
            dic[i].next = dic[i+1]
            dic[i + 1].pre = dic[i]
    ans = 0
    for i in dic:
        temp = 1
        if dic[i].pre == None:
            while(dic[i].next):
                i+=1
                temp+=1
        ans = max(ans,temp)
    return ans

class node:
    def __init__(self,value,pre,next):
        self.value = value
        self.pre = pre
        self.next = next

def solve3(nums):
    nums = set(nums)
    ans = 0
    for i in nums:
        temp = 1
        if i-1 not in nums:
            while(i+1 in nums):
                i+=1
                temp+=1
        ans = max(ans,temp)
    return ans



# def find(dad,x):
#     return x if dad[x]==x else find(dad,x)
#
# def union(dad,x,y):
#     dad[find(dad,x)]=find(dad,y)


nums = [0,3,7,2,5,8,4,6,0,1]
# ans = solve1(nums)
ans = solve3(nums)