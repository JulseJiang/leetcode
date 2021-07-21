# Title     : lc11_盛水最多的容器.py
# Created by: julse@qq.com
# Created on: 2021/7/12 7:39
# des : TODO

class Solution:
    # def solve(self, height: List[int]) -> int:
    # def solve(self, height):
    #     n = len(height)
    #     max_area = 0
    #     for i in range(n):
    #         for j in range(i+1,n).__reversed__():
    #             # print(i,j)
    #             max_area = max(min(height[j],height[i])*(j-i),max_area)
    #     return max_area

    '''
    pass
    '''
    def solve(self, height):
        n = len(height)
        max_area = 0
        j = n-1
        i = 0
        while(i<j):
            max_area = max(min(height[j],height[i])*(j-i),max_area)
            if height[i]<height[j]:i +=1
            else:j-=1

        return max_area

    def solve(self, height):
        max_area = 0
        j = len(height)-1
        i = 0
        while(i<j):
            if height[i]<height[j]:
                max_area = max(height[i]*(j-i),max_area)
                i +=1
            else:
                max_area = max(height[j] * (j - i), max_area)
                j-=1
        return max_area


if __name__ == '__main__':
    mydict = {}
    prices = [1,8,6,2,5,4,8,3,7]
    # prices = [1,2,1] # 1
    ans = Solution().solve(prices)
    print(ans)