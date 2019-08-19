#2.列表list1 = [0,1,2,3],list2 = ["a","b","c","d"],
# 以list1中的元素作为key，以list2中的元素作为value，
  #生成一个新的字典dict1 = {0:"a",1：“b”,,,,}
list1 = [0,1,2,3,4,3]
list2 = ["a","b","c","d","e","f"]
dict2 = {}

#前提条件：两个列表的长度相等
if len(list1 ) <= len(list2):
    for index in range(len(list1)):
        #字典中的key不存在时，赋值，相当于向字典中添加键值对
        if list1[index] not in dict2:
            dict2[list1[index]] = list2[index]

    print("长度相等或者小于：",dict2)
else:
    for index in range(len(list2)):
        if list1[index] not in dict2:
            dict2[list1[index]] = list2[index]

    print("list1大于list2:",dict2)
