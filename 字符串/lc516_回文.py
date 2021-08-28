# Title     : lc516_回文.py
# Created by: julse@qq.com
# Created on: 2021/8/12 21:28
# des : TODO
def solve1(s):
    dp = [[0]*len(s) for _ in range(len(s))]

    for i in range(len(s)):
        for j in range(i,-1,-1):
            if i==j:dp[i][j] = 1
            else:
                if s[i] == s[j]:
                    dp[j][i] = dp[j + 1][i - 1] + 2
                else:
                    dp[j][i] = max(
                        dp[j][i-1],
                        dp[j+1][i]
                    )
    return dp[0][len(s)-1]


def solve2(s):
    dp = [[0]*len(s) for _ in range(len(s))]
    for i in range(len(s)-1,-1,-1):
        for j in range(i,len(s)):
            if i==j:dp[i][j] = 1
            else:
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(
                        dp[i][j-1],
                        dp[i+1][j]
                    )
    return dp[0][len(s)-1]


def solve3(s):
    n = len(s)
    dp = [1]*n
    for i in range(n-2,-1,-1):
        for j in range(i+1,n):
            dplij = dp[j]
            if s[i] == s[j]:
                dp[j] = dpij + 2 if i<j-1 else 2
            else:
                dp[j] = max(dp[j-1],dp[j])
            dpij = dplij
    return dp[n-1]

# s = "bbbab" # 4
s = "cbbd" # 2
# s = "abaaba"  #6
# s = 'a'
# ans = solve1(s)
# ans = solve2(s)
ans = solve3(s)