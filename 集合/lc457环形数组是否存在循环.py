# Title     : lc457环形数组是否存在循环.py
# Created by: julse@qq.com
# Created on: 2021/8/7 20:42
# des : TODO

def solve1(nums):
    n = len(nums)
    N = 2**n-1
    for i in range(n):
        visited = set()
        cover = 0
        while cover<=N:
            if i in visited:return True
            visited.add(i)
            # cover|= 1<<i
            j = (i+nums[i])%n
            if nums[i] * nums[j] < 0 or i==j: break
            i = j
    return False

'''
快慢指针
'''
def solve2(nums):
    n = len(nums)
    if n==1:return False
    for i in range(n):  # i  # 慢
        j = (i+nums[i]) % n  # 快
        if i==j:continue
        while True:
            if i==j:return True
            j1 = (j+nums[j])%n
            if nums[j1] * nums[j] < 0 or j1 == j: break
            j = j1
            j1 = (j + nums[j]) % n
            if nums[j1] * nums[j] < 0 or j1 == j: break
            i1 = (i+nums[i])%n
            if nums[i1] * nums[i] < 0 or i1==i: break
            i,j = i1,j1
    return False

'''
快慢指针 优化（不合法部分置0） 提升不大
'''
def solve3(nums):
    n = len(nums)
    if n==1:return False
    for i in range(n):  # i  # 慢
        j = (i+nums[i]) % n  # 快
        if i==j:
            nums[j] = 0
            continue
        add = 0
        while True:
            if i==j:return True
            if nums[i] ==0:break
            j1 = (j+nums[j])%n
            if nums[j1] * nums[j] < 0 or j1 == j:
                add = j
                break
            j = j1
            j1 = (j + nums[j]) % n
            if nums[j1] * nums[j] < 0 or j1 == j:
                add = j
                break
            i1 = (i+nums[i])%n
            if nums[i1] * nums[i] < 0 or i1==i:
                add = i
                break
            i,j = i1,j1
        while nums[add]*nums[(add+nums[add])%n]>0:
            temp = (add+nums[add])%n
            nums[add] = 0
            add = temp

    return False
'''
快慢指针官方
'''
def solve4(nums):
    n = len(nums)

    def next(cur: int) -> int:
        return (cur + nums[cur]) % n  # 保证返回值在 [0,n) 中

    for i, num in enumerate(nums):
        if num == 0:
            continue
        slow, fast = i, next(i)
        # 判断非零且方向相同
        while nums[slow] * nums[fast] > 0 and nums[slow] * nums[next(fast)] > 0:
            if slow == fast:
                if slow == next(slow):
                    break
                return True
            slow = next(slow)
            fast = next(next(fast))
        add = i
        while nums[add] * nums[next(add)] > 0:
            tmp = add
            add = next(add)
            nums[tmp] = 0
    return False
'''
三色擦除
'''
# def solve4(nums):
#     pass
# def solve2(nums):
#     pass

# nums = [2,-1,1,2,2]
# nums = [-1,2]
# nums = [-2,1,-1,-2,-2]
# nums = [3,1,2]
nums = [-1,2,1,2]
# nums = [-2,1,-1,-2,-2]
# nums = [1,1]
# ans = solve1(nums)
# ans = solve2(nums)
# ans = solve3(nums)
ans = solve4(nums)
print(ans)
