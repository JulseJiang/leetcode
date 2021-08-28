# Title     : lc345_反转元音字母.py
# Created by: julse@qq.com
# Created on: 2021/8/19 16:08
# des : TODO

'''
双指针
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        i = 0
        j = n-1
        s = list(s)
        yy = {'a','e','i','o','u','A','E','I','O','U'}
        while i<j:
            if s[i] not in yy:
                i+=1
            if s[j] not in yy:
                j-=1
            if s[i] in yy and s[j] in yy:
                s[i],s[j] = s[j],s[i]
                # TypeError: 'str' object does not support item assignment
                i+=1
                j-=1
        return ''.join(s)
s = "aA"
ans = Solution().reverseVowels(s)
print(ans)