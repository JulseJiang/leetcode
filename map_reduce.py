# Title     : map_reduce.py
# Created by: julse@qq.com
# Created on: 2021/7/23 16:24
# des :


import time
from functools import reduce


def f(x):
    return x*2
if __name__ == '__main__':
    print('start', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    start = time.time()

    # nums = range(1,11)
    # ans = [x for x in map(f,nums)]
    # print(ans)

    # nums = range(1,11)
    # ans = [x for x in map(lambda x:x*2,nums)]
    # print(sum(ans))
    # print(ans)

    # nums = range(1,11)
    # ans = reduce(lambda x,y:x*2+y*0,nums)
    # print(ans)

    # nums = range(1, 10)
    # ans = reduce(lambda x,y: x+y, nums)
    # print(ans)


    data = [1,2,3,4]
    data = {1,2,3,2}


    print('stop', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    print('time', time.time() - start)


