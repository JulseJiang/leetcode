# Title     : lc1884_扔鸡蛋.py
# Created by: julse@qq.com
# Created on: 2021/7/29 14:44
# 楼高固定 = 扔鸡蛋不会碎的楼层 + 扔鸡蛋会碎的楼层

# 1884. 鸡蛋掉落-两枚鸡蛋

# 给你 2 枚相同 的鸡蛋，和一栋从第 1 层到第 n 层共有 n 层楼的建筑。
#
# 已知存在楼层 f ，满足 0 <= f <= n ，任何从 高于 f 的楼层落下的鸡蛋都 会碎 ，从 f 楼层或比它低 的楼层落下的鸡蛋都 不会碎 。
#
# 每次操作，你可以取一枚 没有碎 的鸡蛋并把它从任一楼层 x 扔下（满足 1 <= x <= n）。如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎，则可以在之后的操作中 重复使用 这枚鸡蛋。
#
# 请你计算并返回要确定 f 确切的值 的 最小操作次数 是多少？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/egg-drop-with-2-eggs-and-n-floors
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 定义dp数组
# dp[0] = 0 不碎
# dp[i] 在第i层扔鸡蛋不掉
# dp[f] 在第f层扔鸡蛋不会碎，在dp[f+1] 扔鸡蛋碎了


# dp[0][2] 第0层有2个鸡蛋
# dp[i][j] = dp[i-1][j-1]+1 碎了
# dp[i][j] = dp[N-i][j]+1 没碎
# dp[i][j] = max(dp[i-1][j-1],dp[N-i][j])+1
# 定义转移函数
# if i< f: dp[i] = [0]
# 定义终止条件

# def eggTwo(N):
#     '''
#     :param N: 楼层总数
#     :return:
#     '''
#     # N = 100
#     dp = [[float('inf') for i in range(3)] for j in range(N + 1)]
#     dp[0][2] = 0
#     for i in range(N):
#         dp[i][1] = i
#     for n in range(1, N + 1):
#         for i in range(2, n + 1):
#             dp[n][2] = min(dp[n][2], max(dp[i - 1][1], dp[n - i][2]) + 1)  # (1<=i<=n)
#     print(dp[N][2])
#     return dp[N][2]


'''
K个鸡蛋，超时
'''
# def eggK(N,K):
#     dp = [[float('inf') for i in range(K+1)] for j in range(N + 1)]
#     dp[0][K] = 0
#     for i in range(N):
#         dp[i][1] = i
#     for k in range(K):
#         dp[0][k] = 0
#     for n in range(1, N + 1):
#         for i in range(2, n + 1):
#             for k in range(1,K+1):
#                 dp[n][k] = min(dp[n][k], max(dp[i - 1][k-1], dp[n - i][k]) + 1)  # (1<=i<=n)
#     return dp[N][K]
#     # return dp

'''
二分 K个鸡蛋
'''
count_dp =0
def eggK_dp(N,K):
    dp = [[float('inf') for i in range(K+1)] for j in range(N + 1)]
    dp[0][K] = 0
    for i in range(N+1):
        dp[i][1] = i
    for k in range(K):
        dp[0][k] = 0
        dp[1][k] = 1
    for n in range(2, N + 1):
        for k in range(2, K + 1):
            if k >n:
                dp[n][k]=dp[n][n]
                break
            start = 2
            end = n
            while(start <= end):
                global count_dp #98248
                count_dp +=1
                mid = (start+end)//2
                y = dp[mid - 1][k-1] - dp[n - mid][k]
                if y>0:
                    end = mid-1
                elif y<0:
                    start = mid + 1
                else:
                    start = end = mid
                    break
            dp[n][k] = min(max(dp[start - 1][k-1],dp[n - start][k]),
                           max(dp[end - 1][k-1],dp[n - end][k])) +1
    # return dp[N][K]
    return dp[N][K]

# D(i,7,3) = max(dp[i - 1][k-1], dp[n - i][k]
'''
输出扔鸡蛋方案
'''
# def eggK(N,K):
#     dp = [[float('inf') for i in range(K+1)] for j in range(N + 1)]
#     dp[0][K] = 0
#     for i in range(N):
#         dp[i][1] = i
#     for k in range(K):
#         dp[0][k] = 0
#     for n in range(1, N + 1): # 选最小
#         ri = 0
#         rk = 0
#         for i in range(1, n + 1): # 任意选一个楼层扔鸡蛋
#             for k in range(1,K+1): # 鸡蛋个数
#                 if dp[i - 1][k-1] >= dp[n - i][k]:
#                     ri = i - 1
#                     rk = k-1
#                     rm = dp[i - 1][k-1]
#                 else:
#                     ri = n - i
#                     rk = k
#                     rm = dp[n - i][k]
#                 if rm + 1<=dp[n][k]:
#                     dp[n][k] = rm + 1
#                 else:
#                     ri = n
#                     rk = k
#         print(ri,rk)
#     return dp[N][K]
    # return dp




'''
递归来做  leetcode 上超时，在pycharm上超出最大递归深度
  File "E:/githubcode/leetcode/lc1884_扔鸡蛋.py", line 113, in eggK
    tp = min(tp,max(eggK(n-i,k),eggK(i-1,k-1))+1)
  [Previous line repeated 2976 more times]
  File "E:/githubcode/leetcode/lc1884_扔鸡蛋.py", line 112, in eggK
    for i in range(1,n+1):
RecursionError: maximum recursion depth exceeded in comparison


    N=100
    K=10
    n<=k/2 
    # # ans = 8 预期 7 
    n<k/2 
    # # ans = 7 预期 7 
'''
# memor = {}
# def eggK(n,k):
#     if (n,k) in memor:return memor[(n,k)]
#     if k == 1 or n== 0:
#         memor[(n,k)] = n
#         return n
#     if n == 1:
#         memor[(n,k)] = 1
#         return 1
#     tp = float('inf')
#     for i in range(1,n+1):
#         tp = min(tp,max(eggK(n-i,k),eggK(i-1,k-1))+1)
#     memor[(n,k)] = tp
#     return tp

# count =0
# memor = {}
# def eggK(n,k):
#     if (n,k) in memor:return memor[(n,k)]
#     if k == 1 or n== 0:
#         memor[(n,k)] = n
#         return n
#     if n == 1:
#         memor[(n,k)] = 1
#         return 1
#     start = 2
#     end = n
#     while (start <= end):
#         global count #22853
#         count += 1
#         mid = (start + end) // 2
#         y = eggK(mid - 1,k - 1) - eggK(n - mid,k)
#         if y > 0:
#             end = mid - 1
#         elif y < 0:
#             start = mid + 1
#         else:
#             start = end = mid
#             break
#     tp = min(max(eggK(start - 1,k - 1), eggK(n - start,k)),
#                    max(eggK(end - 1,k - 1), eggK(n - end,k))) + 1
#     memor[(n,k)] = tp
#     return tp
'''
自底向上
'''
memor = {}

def eggK(n,k):
    for j in range(n):
        for i in range(1, k + 1):
            doEggK(j,i)
    return doEggK(n, k)
def doEggK(n,k):
    if (n,k) in memor:return memor[(n,k)]
    if k == 1 or n==0:
        memor[(n,k)] = n
        return n
    tp = float('inf')
    for i in range(1,n+1):
        tp = min(tp,max(memor[(n-i,k)],memor[(i-1,k-1)])+1)
    memor[(n,k)] = tp
    return tp

'''
K个鸡蛋
给定楼层数目和鸡蛋个数，求最坏情况最小操作次数 => 给定操作次数，和鸡蛋个数，最多可以检测多少层楼
f(t,k)=1+f(t−1,k−1)+f(t−1,k)
'''
memor = {}
def eggK2(n,k):
    for t in range(1,n+1):
        cn = doEggK2(t, k)
        if cn>=n:return t
def doEggK2(t,k):
    if (t,k) in memor:return memor[(t,k)]
    if t==1 or k==1:return t
    cn = 1+doEggK2(t-1,k-1)+doEggK2(t-1,k)
    memor[(t, k)] = cn
    return cn

# # D(i,7,3) = max(dp[i - 1][k-1], dp[n - i][k]
# dp[n][k] = min(max(dp[i - 1][k-1], dp[n - i][k])+1) 1<=i<=n

def plotEggKvaryN():
    N = 15
    K = 4
    # ans = 4
    eggK(N, K)
    import matplotlib.pyplot as plt
    ans = []
    for k in range(K):
        ans.append([])
    for n,k in memor:
        ans[k-1].append(memor[(n,k)])
    fig,ax = plt.subplots(2,2)
    for i in range(4):
        ax[i//2][i%2].plot(ans[i])
        ax[i//2][i%2].set_title('k=%d'%(i+1))
    plt.show()


def plotEggKvaryK():
    N = 100
    K = 10
    # ans = 4
    eggK(N, K)
    import matplotlib.pyplot as plt
    ans = []
    varyN = [10,30,50,90]
    for k in varyN:
        ans.append([])
    for n, k in memor:
        if n in varyN:
            ans[varyN.index(n)].append(memor[(n, k)])
    fig, ax = plt.subplots(2, 2)
    for i in range(4):
        ax[i // 2][i % 2].plot(ans[i])
        ax[i // 2][i % 2].set_title('n=%d' % (varyN[i]))
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    # N=100
    # K=2
    # # ans = 14
    # N=2
    # K=3
    # # ans = 2

    # N=7
    # K=3
    # # ans = 3

    # N=15
    # K=4
    # # ans = 4

    N=100
    K=10
    # ans = 7

    # N=100
    # K=300
    # # ans = 7

    # N=2
    # K=1
    # # # ans = 7

    # N=5000
    # K=4
    # ans = 19
    # ans = eggTwo(N)
    # ans = eggK(N,K)
    # ans_dp = eggK_dp(N,K)

    # plotEggKvaryK()
    #
    # 逆向 通过操作次数求能检验的楼层高度
    ans = eggK2(N, K)













