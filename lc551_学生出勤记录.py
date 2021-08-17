# Title     : lc551_学生出勤记录.py
# Created by: julse@qq.com
# Created on: 2021/8/17 16:33
# des : TODO

class Solution:
    def checkRecord(self, s: str) -> bool:
        ca = 0
        cl = 0
        for i in s:
            if i =='L':
                cl +=1
                if cl==3:return False
            elif i =='A':
                ca += 1
                cl=0
                if ca>= 2:return False
            else:
                cl = 0
        return True

s = "PPALLP"
ans = Solution().checkRecord(s)
print(ans)
