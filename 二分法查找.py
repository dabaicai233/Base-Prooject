list1 = [4, 6, 6, 32, 54, 80, 99, 554]
#待查找的元素
key = 554
#下标的初始值
left = 0
right = len(list1) - 1
#当查找的过程中，left和right根据不同的条件进行慢慢靠拢，
# 当left == right的时候，说明整个列表已经被搜索了一遍
#如果还没有获取到key，则说明该元素在列表中不存在
while left <= right:
    #计算中间下标的值
    middle = (left + right) // 2
    #比较两个数的大小
    if list1[middle] < key:
        #修改left的值
        left = middle + 1
    elif list1[middle]  > key:
        #修改right的值
        right = middle - 1
    else:
        print("%s在列表中的位置为%d" % (key,middle))
        #在条件还成立的情况下，有可能已经得到了结果，则可以提前结束循环
        break
#注意：二分法查找一定要注意列表是降序还是升序的，区别在于left和right的取值


