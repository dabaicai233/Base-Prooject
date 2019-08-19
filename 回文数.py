num = int(input("请输入一个五位数："))
#方式一
if num >= 10000 and num <= 99999:
    s1 = num // 10000
    s2 = (num % 10000) // 1000
    s3 = (num % 1000) // 100
    s4 = (num % 100) // 10
    s5 = num % 10

    if s1 == s5 and s2 == s4:
        print("是回文数")
    else:
        print("不是")
else:
    print("输入有误")


#方式二
num = input("请输入一个五位数：")
print(num)
#字符串，如果要获取其中的每个字符，字符串名称[索引/下标/角标]
#print(num[0],num[1],num[2],num[3],num[4])
#len()用于获取一个字符串的长度
if len(num) == 5:
    if num[0] == num[len(num) - 1] and num[1] == num[3]:
        print("是回文数")
    else:
        print("不是")
else:
    print("输入有误")