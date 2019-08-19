#2.编写程序，生成一个大写字母 A-Z 及其对应的ASCII码值的字典
dict1 = {}

#chr   ord

for num in range(ord("A"),ord("Z") + 1):
    dict1[chr(num)] = num

print(dict1)
