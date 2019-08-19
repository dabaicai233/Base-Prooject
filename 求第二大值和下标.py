#求一个列表中的第二大值和对应的下标
list1 = [32,4,54,554,6,6,554,554,554]
list2 = list1.copy()

for i in range(len(list2) - 1):
    for j in range(len(list2) - 1 - i):
        if list2[j] > list2[j + 1]:
            list2[j],list2[j + 1] = list2[j + 1],list2[j]

print(list2)
print(list1)

# secondValue = list2[len(list2) - 2]
#
# for index in range(len(list1)):
#     if list1[index] == secondValue:
#         print(index,secondValue)


#问题：最大值可能有多个
#优化：考虑到最大值的个数，要确定第二大值，需要将所有的最大值除掉
maxValue = list2[len(list2) - 1]
print(maxValue)

maxCount = list2.count(maxValue)
print(maxCount)

secondValue = list2[-(maxCount + 1)]
print(secondValue)

for index in range(len(list1)):
    if list1[index] == secondValue:
        print(index,secondValue)