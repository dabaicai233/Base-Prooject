#1.封装函数功能，判断年的平润性
"""
def isleapyear(year):
    if (year % 4 == 0 and year % 100 != 0)  or  year % 400 == 0:
        #print("闰年")
        #return True
        return  "闰年"
    else:
        #print("平年")
        #return  False
        return  "平年"
"""


#2.封装函数功能，统计1~某个数范围内能被3整除的数的个数，并返回结果
"""
def getcount(num):
    c = 0
    for i in range(num + 1):
        if i % 3 == 0:
            c += 1
    #print(c)
    return  c


"""
#3.封装函数功能，统计2~某个数范围内质数的个数，并返回结果
#判断一个数是否是质数
def isprime(num):
    if num <= 1:
        return False
    else:
        result = True
        for i in range(2,num):
            if num % i == 0:
                result = False
                break

        return result

def getprimecount(n):
    c = 0
    for m in range(2,n + 1):
        r = isprime(m)
        if r:
            c += 1
    return c

print(getprimecount(100))