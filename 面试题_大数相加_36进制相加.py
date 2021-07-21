# Title     : 面试题_大数相加.py
# Created by: julse@qq.com
# Created on: 2021/7/17 11:21


'''
字符串相加
'''
# class Solution:
#     def add(self,a,b,jinwei):
#         c = (int(a)+int(b)+jinwei)%10
#         jinwei = (int(a)+int(b)+jinwei)//10
#         return str(c),jinwei
#     def addStrings(self, num1: str, num2: str) -> str:
#         import itertools
#         ans = []
#         jinwei = 0
#         for a,b in itertools.zip_longest(num1[::-1],num2[::-1],fillvalue=0):
#             c,jinwei = self.add(a,b,jinwei)
#             ans.append(c)
#         if jinwei!=0:ans.append(str(jinwei))
#         return ''.join(ans)[::-1]
'''
k进制加法
'''
class Solution:
    def add(self,a,b,jinwei,k):
        a = int(a,k) if a!=0 else 0
        b = int(b,k) if b!=0 else 0
        c = (a+b+jinwei)%k
        jinwei = (a+b+jinwei)//k
        c = c if c<10 else chr(ord('a')+c-9)
        return str(c),jinwei
    def addStrings(self, num1: str, num2: str,k:int) -> str:
        import itertools
        ans = []
        jinwei = 0
        for a,b in itertools.zip_longest(num1[::-1],num2[::-1],fillvalue=0):
            c,jinwei = self.add(a,b,jinwei,k)
            ans.append(c)
        if jinwei!=0:ans.append(str(jinwei))
        return ''.join(ans)[::-1]
if __name__ == '__main__':
    '''
    字符串相加
    '''
    # num1 = '2345678'
    # num2 = '987654'
    # ans = '2333333'

    # num1 = "1"
    # num2 = "9"
    # ans = '10'

    # num1 = "1"
    # num2 = "5"
    # ans = '6'

    # num1 = "9"
    # num2 = "99"
    # # ans = '10'

    '''
    二进制相加
    '''
    # 输入: a = "1010", b = "1011"
    # 输出: "10101"
    # num1 = '1010'
    # num2 = '1011'
    # ans = '10101'
    '''
    16进制
    18be+6784
    '''
    num1 = '18be'
    num2 = '6784'
    k=16
    # ans = '8042'

    # num1 = '123ab'
    # num2 = 'ab'
    # ans = '10101'
    # k = 12
    ans = Solution().addStrings(num1,num2,k)
    print(ans)


