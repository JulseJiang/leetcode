# Title     : lc881_救生艇.py
# Created by: julse@qq.com
# Created on: 2021/8/26 10:34
# des : TODO


class Solution:
    def numRescueBoats(self, people, limit) -> int:
        ans = 0
        people.sort()
        i = 0
        j = len(people)-1
        while i<=j:
            if people[i]<=limit-people[j]:
                i+=1
            ans +=1
            j-=1
        return ans
people = [3,2,2,1]
limit = 3
ans = Solution().numRescueBoats(people, limit)
print(ans)