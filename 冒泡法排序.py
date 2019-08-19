#以升序为例
list1 = [23,43,34,12,100,66]
#外层循环：控制比较的轮数
for i in range(len(list1) - 1):
    #内层循环：控制每一轮比较的次数兼顾参与比较的下标
    for j in range(len(list1) - i - 1):   #-1是为了避免列表越界
        #比较两个数的大小
        #思路：以升序为前提，如果下标小的元素   比   下标大的元素   大 ，则交换位置
        if list1[j] < list1[j + 1]:
            list1[j],list1[j + 1] = list1[j + 1],list1[j]
print(list1)
"""
问题：
if list1[j] > list1[j + 1]:
IndexError: list index out of range
原因：
    for i in range(len(list1) - 1):   0,1,2,3,4
     for j in range(0,len(list1) - i):

     当i = 0时，j的取值范围：0 ~ 5 ，j + 1的取值范围：1~6，j + 1整体代表的是一个索引，
     当取值为6的时候，则下标越界
解决：
    j :0~4
    j + 1:0~5
"""