# Title     : lc42_接雨水.py
# Created by: julse@qq.com
# Created on: 2021/7/12 11:09
# des :

'''
穷举 超时
'''
# class Solution:
#     def solve(self, height):
#         sum_area = 0
#         n = len(height)
#         for i in range(1,n-1):
#             left_edge = height[0]
#             right_edge = height[n - 1]
#             for j in range(n):
#                 if j<i:left_edge = max(left_edge,height[j])
#                 else:right_edge = max(right_edge,height[j])
#             m_area = min(right_edge,left_edge)-height[i]
#             sum_area += m_area if m_area >0 else 0
#             print(i,sum_area,left_edge,right_edge)
#         return sum_area

'''
找左右墙 通过
'''

# class Solution:
#     def solve(self, height):
#         sum_area = 0
#         n = len(height)
#         lw = [0]*n # lw[i] 第i根柱子的左墙高度
#         rw = [0]*n # lw[i] 第i根柱子的左墙高度
#         for i in range(1,n-1):
#             # 找左墙
#             lw[i] = max(lw[i-1],height[i-1])
#         for i in range(n-2,0,-1):
#             # 找右墙
#             rw[i] = max(rw[i+1],height[i+1])
#
#         for i in range(1,n-1):
#             m_area = min(lw[i], rw[i]) - height[i]
#             sum_area += m_area if m_area >0 else 0
#         return sum_area

''' 
双指针  通过
'''
class Solution:
    def solve(self, height):
        ans = 0
        left = 0
        right = len(height)-1
        if right<=0:
            return 0
        lw = height[left]
        rw = height[right]
        while(left<right):
            if lw<=rw:
                left += 1
                if lw<=height[left]:
                    lw = height[left]
                else:
                    ans += lw-height[left]
            else:
                right -= 1
                if rw<=height[right]:
                    rw = height[right]
                else:
                    ans += rw-height[right]
        return ans

if __name__ == '__main__':
    mydict = {}
    # prices =  [0,1,0,2,1,0,1,3,2,1,2,1]
    prices =  [4,2,0,3,2,5] #7 答案是 9
    ans = Solution().solve(prices)
    print(ans)