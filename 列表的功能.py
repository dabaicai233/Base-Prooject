# #1.逐一显示列表list1 = ["aaa","bbb","ccc","ddd","eee"]中索引为奇数的元素
list1 = ["aaa","bbb","ccc","ddd","eee"]
# # #直接操作元素，缺点：无法操作索引
 # for element in list1:
 #     print(element)
#
# #直接操作索引
for index in range(len(list1)):
     if index % 2 == 1:
         print("第%d个元素是%s" % (index,list1[index]))

#2.将属于列表l1 = ["aaa","bbb","ccc","ddd","eee"],但不属于列表l2 = ["aaa","ddd","eee","fff"]
  #的所有元素定义为一个新的列表l3
l1 = ["aaa","bbb","ccc","ddd","eee"]
l2 = ["aaa","ddd","eee","fff"]
l3 = []

#2.1遍历l1
for str1 in l1:
    #2.2将l1中的元素判断在l2中是否存在
    if str1 not in l2:
        #2.3将符合条件的str1添加到l3中
        l3.append(str1)
print(l3)

#3.已知列表l1 = ["aaa","bbb","ccc","ddd","eee","aaa","aaa","fff"]，去除其中的重复元素"aaa"
l1 = ["aaa","bbb","ccc","ddd","eee","aaa","aaa","ffff"]
repeatValue = "aaa"
#3.1统计指定元素的出现次数
count1 = l1.count(repeatValue)
print(count1)

# l1.remove(repeatValue)
# print(l1)
# l1.remove(repeatValue)
# print(l1)
# l1.remove(repeatValue)
# print(l1)
n1 = 0
while n1 < count1:
    l1.remove(repeatValue)
    n1 += 1
print(l1)

#4.已知列表nameList = ["stu1","stu2","stu3","stu4","stu5","stu6"]，删除列表removeList = ["stu3","stu5","stu9"]，
   #将属于removeList中的每个元素从nameList中移除
nameList = ["stu1","stu2","stu3","stu4","stu5","stu6","stu5","stu5"]
removeList = ["stu3","stu5","stu9"]

#问题说明：移除元素的时候，对原列表已经做了修改，但是遍历的过程中，索引还使用的是原索引，导致有的元素未参与遍历
# for name in nameList:
#     print("~~~~~")
#     if name in removeList:
#         nameList.remove(name)
#         print("%%%%%%%%")
# print(nameList)

#优化代码，方式一
newList = []
for name in nameList:
    if name not in removeList:
        newList.append(name)
print(newList)


#方式二
nameList = ["stu1","stu2","stu3","stu4","stu5","stu6","stu5","stu5"]
removeList = ["stu3","stu5","stu9"]
n2 = 0
while n2 < len(removeList):
    if removeList[n2] in nameList:
        #统计出现的次数
        c = nameList.count(removeList[n2])
        n1 = 0
        while n1 < c:
            nameList.remove(removeList[n2])
            n1 += 1
    n2 += 1
print(nameList)
