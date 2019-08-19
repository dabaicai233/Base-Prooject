"""
#1.从控制台输入一个单词，判断在一句英文中出现的次数
str1 = "this is a good thing this is a bad thing this is a nice thing"
#a.获取字符串中的所有的单词
wordList = str1.split(" ")

wordDict = {}    #worDict["this"] = 3
#b.遍历列表，结合字典，单词作为key，出现的次数作为value
for word in wordList:
    #添加键值对：如果key存在，则重新赋值，如果key不存在，则添加键值对
    r = wordDict.get(word)
    if r == None:
        #key不存在
        wordDict[word] = 1
    else:
        #key存在
        wordDict[word] += 1
#print(wordDict)

data = input("请输入要查找的单词：")
if wordDict.get(data):
    print(wordDict[data])
else:
    print("你查询的单词不存在")


#2.给定一个时分秒的时间，获取下一秒
#15:30:45------》15:30:46
#15:30:59-----》15:31:00
timeStr = input("请输入时分秒时间：")
timeList = timeStr.split(":")
h = int(timeList[0])
m = int(timeList[1])
s = int(timeList[2])

s += 1

if s == 60:
    s = 0
    m += 1
    if m == 60:
        m = 0
        h += 1
        if h == 24:
            h = 0

#print("{}:{}:{}".format(h,m,s))
print("%.2d:%.2d:%.2d" % (h,m,s))


#3.从控制台输入任意数据，如果涉及敏感词汇则将其用***替换.
list1 = ["aaa","bbbb","fff","dddd"]
data1 = input("请输入任意内容：")

for word in list1:
    #find、index:查找一个子字符串在原字符串中是否存在【第一次】
    #in
    if word in data1:
        #替换
        data1 = data1.replace(word,"*" * len(word))
print(data1)
"""

#4.从控制台输入任意的文本，将其中的数字挑出，拼接成数字类型输出，例如：“abc12cd87uuu999” ---->1287999
#isdigit
data2 = input("请输入任意内容：")

newStr = ""
#遍历字符串
for c in data2:
    if c.isdigit():
        #是数字
        newStr += c

    else:
        #不是数字
        pass
print(int(newStr))


#5.实现一个简单的购物车【实现商品的添加和删除】


