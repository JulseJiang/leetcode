# Title     : 0728排序算法.py
# Created by: julse@qq.com
# Created on: 2021/7/27 16:12
# des : 归并排序，希尔排序

'''
归并排序
'''
# def mergeSort(nums):
#     if len(nums)==1:
#         return nums
#     s = len(nums)//2
#     sa,sb = mergeSort(nums[:s]),mergeSort(nums[s:])
#     ans = doMerge(sa,sb)
#     return ans
# def doMerge(sa,sb):
#     ans = []
#     i = j = 0
#     while(i<len(sa) and j <len(sb)):
#         if sa[i]<=sb[j]:  # 保证排序稳定（元素相等的时候，sb中的元素插在后面）
#             elem = sa[i]
#             i+=1
#         else:
#             elem = sb[j]
#             j+=1
#         ans.append(elem)
#     ans.extend(sa[i:])
#     ans.extend(sb[j:])
#     return ans

'''
堆排序 -- 自底向上调整
目前时间复杂度：O(n^2)
目标：O(n* log2(n))
'''
# def heapSort(nums):
#     for end in range(len(nums)-1,-1,-1):
#         doheapSort(nums,end)
#     return nums
#
# def doheapSort(nums,end):
#     root = (end-1) // 2  # 最后一个非叶节点的下标
#     while(root>=0):
#         left = root*2+1
#         right = root*2+2
#         if nums[left]>nums[root]:
#             nums[left], nums[root] = nums[root],nums[left]
#         if nums[right] > nums[root] and right<=end:
#             nums[right], nums[root] = nums[root], nums[right]
#         root-=1
#     # root -1 # 倒数第二个非叶节点的下标
#     nums[0], nums[end] = nums[end], nums[0]

'''
n*log2(n)
'''
# def heapSort(nums):
#     generateBigheap(nums)
#     for end in range(len(nums)-1,-1,-1):
#         nums[0], nums[end] = nums[end], nums[0]
#         down_adjust(nums,0,end-1)
#     return nums
#
# def generateBigheap(nums):
#     for root in range((len(nums)-2)//2,-1,-1):
#         print(root)
#         left = root*2+1
#         right = left+1
#         maxelem = left if right>len(nums)-1 or nums[right]<nums[left] else right
#         if nums[root]>nums[maxelem]:continue
#         nums[maxelem], nums[root] = nums[root], nums[maxelem]
#         down_adjust(nums, maxelem,len(nums)-1)
# def down_adjust(nums,root,end):
#     while root * 2 + 1 <end:
#         left = root * 2 + 1
#         right = left + 1
#         maxelem = left if right>end or nums[right]<nums[left] else right
#         if nums[root] > nums[maxelem]: break
#         nums[maxelem], nums[root] = nums[root], nums[maxelem]
#         root = maxelem


'''
快排
'''

# def quickSort(nums,start,end):
#     i = start
#     j = end
#     if start>=end:return
#     base = i
#     b = nums[base]
#     while i<j:
#         while nums[j] >= b and i<j:j-=1
#         nums[i] = nums[j]
#         while nums[i]<=b and i<j:i+=1
#         nums[j] = nums[i]
#     nums[i] = b
#     quickSort(nums,start,j-1)
#     quickSort(nums,j+1,end)


###################### 快速实现  ######################


# def mergeSort(nums):
#     if len(nums)==1:return nums
#     s = len(nums)//2
#     sa = mergeSort(nums[:s])
#     sb = mergeSort(nums[s:])
#     ans = doMerge(sa,sb)
#     return ans
# def doMerge(sa,sb):
#     sc = []
#     i = 0
#     j = 0
#     while(i<len(sa) and j <len(sb)):
#         if sa[i]<= sb[j]:
#             sc.append(sa[i])
#             i+=1
#         else:
#             sc.append(sb[j])
#             j+=1
#     sc.extend(sa[i:])
#     sc.extend(sb[j:])
#     return sc


# def heapSort(nums):
#     generateBigheap(nums)
#     for end in range(len(nums)-1,-1,-1):
#         nums[0], nums[end] = nums[end], nums[0]
#         downAdjust(nums, 0, end-1)
#     return nums
# def generateBigheap(nums):
#     end = len(nums)-1
#     for root in range((end-1)//2,-1,-1):
#         left = root * 2 + 1
#         right = left + 1
#         maxelem = right if right<end and nums[right]>nums[left] else left
#         if nums[maxelem]<=nums[root]:continue
#         nums[root],nums[maxelem] = nums[maxelem],nums[root]
#         downAdjust(nums, maxelem, end)
#         root -=1
# def downAdjust(nums,root,end):
#     while root * 2 + 1<end:
#         left = root * 2 + 1
#         right = left + 1
#         maxelem = right if right < end and nums[right] > nums[left] else left
#         if nums[maxelem] <= nums[root]:break
#         nums[root], nums[maxelem] = nums[maxelem], nums[root]
#         downAdjust(nums, maxelem, end)
#         root = maxelem

# def quickSort(nums,start,end):
#     if start>=end:return
#     i = start
#     j = end
#     b = nums[i]
#     while(i<j):
#         while nums[i] <= nums[j] and i<j:j-=1
#         nums[i],nums[j] = nums[j],nums[i]
#         while nums[j]>nums[i] and i<j:i+=1
#         nums[j] = nums[i]
#     nums[i] = b
#     quickSort(nums,start,i-1)
#     quickSort(nums,i+1,end)
#     return nums


# def heapSort(nums):
#     generateBigheap(nums)
#     for end in range(len(nums)-1,-1,-1):
#         nums[0],nums[end] = nums[end],nums[0]
#         downAdjust(nums,0,end-1)
#     return nums
# def generateBigheap(nums):
#     end = len(nums)-1
#     for root in range((end-1)//2,-1,-1):
#         left = root * 2 +1
#         right = left +1
#         maxelem = left if right>end or nums[left]>nums[right] else right
#         if nums[root]>nums[maxelem]:continue
#         nums[root],nums[maxelem] = nums[maxelem],nums[root]
#         downAdjust(nums,maxelem,end)
# def downAdjust(nums,root,end):
#     if root * 2 +1<=end:
#         left = root * 2 +1
#         right = left +1
#         maxelem = left if right>end or nums[left]>nums[right] else right
#         if nums[root]>nums[maxelem]:return
#         nums[root],nums[maxelem] = nums[maxelem],nums[root]
#         downAdjust(nums,maxelem,end)

# def downAdjust(nums,root,end):
#     while root * 2 +1<=end:
#         left = root * 2 +1
#         right = left +1
#         maxelem = left if right>end or nums[left]>nums[right] else right
#         if nums[root]>nums[maxelem]:return
#         nums[root],nums[maxelem] = nums[maxelem],nums[root]
#         root = maxelem

'''
优化后
'''
# def heapSort(nums):
#     generateBigheap(nums)
#     for end in range(len(nums)-1,-1,-1):
#         nums[0],nums[end] = nums[end],nums[0]
#         downAdjust(nums,0,end-1)
#     return nums
# def generateBigheap(nums):
#     end = len(nums)-1
#     for root in range((end-1)//2,-1,-1):
#         downAdjust(nums,root,end)
# def downAdjust(nums,root,end):
#     while root * 2 +1<=end:
#         left = root * 2 +1
#         right = left +1
#         maxelem = left if right>end or nums[left]>nums[right] else right
#         if nums[root]>nums[maxelem]:return
#         nums[root],nums[maxelem] = nums[maxelem],nums[root]
#         root = maxelem

# def julseSort(nums):
#     for i in range(len(nums)-1):
#         for j in range(i+1,len(nums)):
#             if nums[i]>nums[j]:nums[i],nums[j] = nums[j],nums[i]
#     return nums


# def bubbleSort(nums):
#     for i in range(len(nums)-1):
#         flag = False
#         for j in range(len(nums)-i-1):
#             if nums[j]>nums[j+1]:
#                 nums[j],nums[j+1] = nums[j+1],nums[j]
#                 flag = True
#         if not flag:break
#     return nums

# def insertSort(nums):
#     for i in range(len(nums)):
#

# def selectSort(nums):
#     for i in range(len(nums)-1):
#         mi = i
#         for j in range(i,len(nums)):
#             if nums[mi]>nums[j]:
#                 mi = j
#         nums[i],nums[mi] = nums[mi],nums[i]
#     return nums

# def insertSort(nums):
#     for i in range(1,len(nums)): # 第i个待插入的元素，可选择的位置 [0,i]
#         for j in range(i,0,-1):
#             if nums[j]<nums[j-1]:
#                 nums[j-1],nums[j] = nums[j],nums[j-1]
#             else:break
#     return nums

# def shellSort(nums):
#     for s in gap(len(nums)):
#         for i in range(len(nums)-s):
#             if nums[i]>nums[i+s]:nums[i],nums[i+s] = nums[i+s],nums[i]
# def gap(n):
#     gaps = []
#     i = 1
#     while pow(2,i)-1<n:
#         gaps.append(pow(2,i)-1)
#         i+=1
#     gaps.reverse()
#     return gaps

'''
桶排序
把数组分成指定上下界的几组，然后把未排序数组放入对应区间，区间内用链表实现排序
https://zhuanlan.zhihu.com/p/125737294
'''
def bucketSort(nums):
    pass
'''
基数排序，从低位到高位，按位排序，固定好每一位的元素之后，用链表实现
https://baike.baidu.com/item/%E5%9F%BA%E6%95%B0%E6%8E%92%E5%BA%8F/7875498
'''
def radixSort(nums):
    pass
if __name__ == '__main__':
    # nums = [5,1,8,3,5,2,3,1]x
    # nums = [5,4,3,2,1]
    nums = [1,5,4,3,2,1]
    # nums = [1,3,5,4,2]
    # ans = mergeSort(nums)
    # ans = heapSort(nums)
    # ans = quickSort(nums,0,len(nums)-1)
    # ans = bubbleSort(nums)
    # ans = julseSort(nums)
    # ans = selectSort(nums)
    # ans = shellSort(nums)

    # sa = [1,2,8,10]
    # sb = [3,5]
    # ans = doMerge(sa, sb)

    import pandas as pd
    fin = '3human_predict.tsv' # 2k条
    limit = 1000
    df = pd.read_table(fin,header=None)
    df1 = df.sort_values(by=2,ascending=False,inplace=True)





