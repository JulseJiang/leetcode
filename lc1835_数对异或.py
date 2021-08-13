# Title     : lc1835_数对异或.py
# Created by: julse@qq.com
# Created on: 2021/7/21 9:55
# des : 1835. 所有数对按位与结果的异或和
# &
#  与
# 两个位都为1时，结果才为1     （统计奇数）                      全1为1
# |
#  或
# 两个位都为0时，结果才为0       （统计偶数）                     全0为0
# ^
# 异或
# 两个位相同为0，相异为1      (常用统计不相同数）               不同为1
# ~
# 取反
# 0变1，1变0
# <<
# 左移
# 各二进位全部左移若干位，高位丢弃，低位补0
# >>
# 右移



class Solution:
    '''
    穷举超时
    '''
    # def getXORSum(self, arr1,arr2):
    #     mystr = ''
    #     ans_xor = 0
    #     for i in arr1:
    #         for j in arr2:
    #             ans_and = i & j
    #             ans_xor ^= ans_and
    #             # mystr = mystr.join('%d & %d ^'%(i,j))
    #             mystr += '%d & %d ^ '%(i,j)
    #     return ans_xor,mystr

    '''
    map reduce 的暴力破解 超时
    '''
    # def getXORSum(self, arr1,arr2):
    #     from functools import reduce
    #     return reduce(lambda x,y:x^y,[(i & j) for i in arr1 for j in arr2],0)

    '''
    pass
    '''

    def getXORSum(self, arr1, arr2):
        from functools import reduce
        from operator import xor
        tot1 = reduce(xor, arr1)
        tot2 = reduce(xor, arr2)
        return tot1 & tot2






if __name__ == '__main__':
    # 0
    arr1 = [1,2,3]
    arr2 = [6,5]

    #4
    # arr1 = [12]
    # arr2 = [4]
    ans_xor,mystr = Solution().getXORSum(arr1,arr2)
