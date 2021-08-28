# Title     : lc443_压缩字符串.py
# Created by: julse@qq.com
# Created on: 2021/8/25 9:22
# des : TODO


class Solution:
    def compress(self, chars) -> int:
        i = j = 0
        while(j<len(chars)):
            c = 0
            chars[i] = chars[j]
            while j<len(chars) and chars[i] == chars[j]:
                c+=1
                j+=1
            i+=1
            if c ==1:continue
            strc = list(str(c))
            for cn in strc:
                chars[i] = cn
                i+=1
        return i

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
ans = Solution().compress(chars)
print(ans,chars)