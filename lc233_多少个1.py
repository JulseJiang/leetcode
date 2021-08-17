# Title     : lc233_多少个1.py
# Created by: julse@qq.com
# Created on: 2021/8/13 17:44
# des :
# 方法1:1个1 最多到哪个数字
# 方法2：按位考虑


def solve1(n):
    ab = n
    m = -1
    ans = 0
    while(ab!=0):
        b = ab%10
        ab //=10
        m+=1
        if b > 1:
            ans += 10 ** m
        if m > 0:
            ans += b * m * (10 ** (m - 1))
    ab = n
    while(ab!=0):
        a = ab//(10**m)
        if a==1:
            ans += ab%(10**m)+1
        ab %=(10**m)
        m-=1
    return ans

# n = 4551 # 2415
# n = 13
n = 12
# n = 1
# n = 21
# n = 23
# n = 10
# n = 111 # 35

for n in [4550,4551,4552,12,13,1,10,11,21,23,101]:
    n = 4015
    ans=solve1(n)
    print(n,ans)


