#选择排序


#以升序为例

list1 = [23,43,34,12,100,66]


#外层循环：控制比较的轮数
for i in range(len(list1) - 1):
    #内层循环：控制参与比较的下标和每一轮比较的次数
    for j in range(i + 1,len(list1)):
        #比较
        #思路：以升序为前提，如果下标小的元素   比   下标大的元素   大 ，则交换位置
        if list1[i] > list1[j]:
            list1[i],list1[j] = list1[j],list1[i]

print(list1)