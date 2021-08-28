# Title     : lc541_字符串反转2k.py
# Created by: julse@qq.com
# Created on: 2021/8/23 22:08
# des : TODO

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        p = 0
        ss = list(s)
        n = len(s)
        while p+k<=len(s):
            for i in range(k//2):
                ss[i+p],ss[k-i+p-1] = ss[k-i+p-1], ss[i+p]
            p+=2*k

        for i in range(p,p+(n-p)//2):
            ss[i],ss[n-i+p-1] = ss[n-i+p-1], ss[i]
        return ''.join(ss)
s = "abcd"
k = 2
ans = Solution().reverseStr(s,k)
print(ans)