# Title     : lc3_无重复子串.py
# Created by: julse@qq.com
# Created on: 2021/8/26 11:08
# des : TODO


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        n = len(s)
        if n<2:return n
        s = list(s)
        i = 0
        j = 0
        while j<n:
            zc = set()
            while j<n and s[j] not in zc:
                zc.add(s[j])
                j+=1
            ans = max(ans,j-i)
            i+=1
            j=i
        return ans

s = "au"
# s = "bbbbb"
# s = "abcabcbb"
# s = "aab"
ans = Solution().lengthOfLongestSubstring(s)
print(ans)