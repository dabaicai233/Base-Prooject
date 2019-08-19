#3.从控制台输入一个三位数，如果是水仙花数就打印“是水仙花数”，否则打印“不是水仙花数”例如：153=1^3+5^3+3^3
#注意：水仙花数指的是三位数[100~999]

import math
while True:
    num = int(input("请输入一个水仙花数："))
    if num >= 100 and num <= 999:
        gw = num % 10
        sw = num % 100 // 10
        bw = num // 100

        #result = gw ** 3 + sw ** 3 + bw ** 3
        result = math.pow(gw,3) + math.pow(bw,3) + math.pow(sw,3)

        if num == result:
            print("是水仙花数")
        else:
            print("不是")
    else:
        print("输入有误")

