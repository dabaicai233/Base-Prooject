# 需求：随机生成一个1到100之间的数，从控制台输入一个数与之比较误差：
"""
import random
while True:
    m = random.randint(1,100)#randint的使用，randint的后面必须跟范围（包头包尾 ）
    print(m)
    n = int(input("请输入一个数："))
    if m >= n :
        if m-n <10:
            print("aaaa")
        elif m-n < 30:
            print("bbbb")
        elif m-n <50:
            print("cccc")
        else:
            print("dddd")
    else:
        if n-m <10:
            print("eeeee")
        elif n-m < 30:
            print("bbbbe")
        elif n-m <50:
            print("cccce")
        else:
            print("dddde")
            """
#另一种写法
import random
while True:
    m=random.randint(1,100)
    print(m)
    n = int(input("请输入一个数："))
    if m-n < 10  and m-n >-10:
        print("你很聪明，但还要努力")
    elif m-n < 30 and m-n >-30:
        print("有点吃力，多补补")
    elif m-n <50 and m-n>-50:
        print("没有太多机会了")
    else:
        print("误差太大，没机会了")