#第一题:1.设计一个函数，传入两个代表日期的字符串，
# 如“2018-2-26”、“2017-12-12”，计算两个日期相差多少天
def main(str1,str2):
    import datetime
    str1 = "2018-2-26"
    str2 = "2017-12-12"
    str1 = str1.split("-")
    str2 = str2.split("-")
    days =abs(datetime.datetime(int(str2[0]), int(str2[1]), int(str2[2])) - datetime.datetime(int(str1[0]), int(str1[1]),int(str1[2])))
    return days
print(main("2018-2-26","2017-12-12"))
#
# #第二题:2.反转密码
	#例如：‘123456’ ——> “654321”
	#要求：不得利用系统提供的反转方法，逻辑思路自己写
#方式一
str1="123456"
print(str1[::-1])
#方式二
str1="123456"
str2=""
for i in range(len(str1)):
    str2+=str1[len(str1)-1-i]
print(str2)
# #第三题:有5个人坐在一起，问第五个人多少岁？
# 他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。
# 问第三个人，又说比第2人大两岁。问第2个人，
# 说比第一个人大两岁。最后问第一个人，他说是10岁。
# 请问第五个人多大？
def func(per):
    if per==1:
        return 10
    else:
        return func(per-1)+2
print(func(5))

#第四题:4.给定一个字符串 返回对字符串进行压缩的结果
	#例如：“aaabcaaddbbc” ——> “a3b1c1a2d2b2c1”

def zip(str1):# 声明一个变量记录个数：
    count = 1# 从第一个字符开始记录
    ch = str1[0]# 声明一个变量用于记录最后的压缩结果
    res = ""# 从第二个字符开始遍历字符串开始
    for index in range(1, len(str1)):
        if str1[index] == ch:
            count += 1
        else:# 把结果拼接在 res 上
            res = "%s%s%d" % (res, ch, count) # 继续向下查询下一个字符
            ch = str1[index] # 计数器归1
            count = 1# 将最后一个遍历的字符添加上
            res = "%s%s%d" % (res, ch, count)

    return res

print(zip("aabbccaabcd"))

#第五题：
"""
设计一个函数，对传入的字符串（假设字符串中只包含小写字母和空格）
进行加密操作，
加密的规则是a变d，b变e，c变f，……，x变a，y变b，z变c，
空格不变，返回加密后的字符串
97 98 99 100   x = 120(97) y = 121(98) z = 122(99)
"""
def encryption(str1):
    #声明一个字符串用于接收最后的结果
	res = ""
    #遍历每一个字符  x y  z 之前都是+3
	for s in str1:
		value = ord(s)
		if 97 <= value < 120:
			res += chr(value + 3)
		elif 120 <= value < 123:
			res += chr(value - 23)
		else:
			res += chr(value)
	return res
print(encryption("abcdxyz efg"))

#第六题
import random
str1=""
for i in range(4):
    n=random.randrange(0,3)
    if n==0:
        num=random.randrange(65,91)
        str1+=chr(num)
    elif n==1:
        j=random.randrange(97,123)
        str1+=chr(j)
    else:
        k=random.randrange(0,10)
        str1+=str(k)
print(str1)

#第七题
def func1(str1):
    dict1={}
    for i in str1:
        if i not in dict1:
            dict1[i]=1
        else:
            dict1[i]+=1
    for k in dict1.keys():
        if dict1[k]==max(dict1.values()):
            return k,max(dict1.values())
print(func1("aaaaahuuph"))
#第八题
import re
#方式一
def getsum(str1):
    #对字符串使用非数字进行切割
    pattern = re.compile(r"[^0-9]")
    #切割完成的列表
    res_list = pattern.split(str1)
    #去除列表中的空字符
    count = res_list.count("")
    for i in range(count):
        res_list.remove("")
    #对列表中的数字进行拼接
    res = res_list[0]
    #记录最后的和
    sum = int(res_list[0])
    for i in range(1, len(res_list)):
        res = "%s + %s" % (res, res_list[i])
        sum += int(res_list[i])

    return  "%s = %d" % (res, sum)

print(getsum("12agdas34hjhfa67"))


#方式二
def getsum(str1):
   list1 = re.split(r"[a-zA-Z]+",str1)
   s = 0
   for num in list1:
      if num != "":
          s += int(num)

#第九题：
'''
利用装饰器单例模式完成如下程序：（10分）
	声明一个用户单例类：
		特征描述：用户名，密码，性别
		行为描述：发说说，上传照片 点赞 【函数内部功能使用 print 语句打印即可】
	实例化对象，调用对应的功能
'''

def single(cls):
    instances = {}
    def wrapper(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return wrapper

@single
class User():
    def __init__(self, username, password, sex):
        self.username = username
        self.password = password
        self.sex = sex

    def say(self):
        print("发表说说")

    def upload_pic(self):
        print("上传照片")

    def price(self):
        print("点赞")

user = User("杨阳", "123456", "女")
user.say()
user.upload_pic()
user.price()














