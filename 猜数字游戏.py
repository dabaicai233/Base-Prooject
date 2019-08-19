import random
#练习：猜数字游戏
"""
计算机出一个1~100之间的随机数，由人来猜，
计算机根据人给出的数做出一个判断，做出提示大了/小了/猜对了
"""
answer = random.randint(1,100)

counter = 0

while True:
    counter += 1
    number = int(input("请输入一个数："))

    if number < answer:
        print("大一点,请重新输入")
    elif number > answer:
        print("小一点，请重新输入")
    else:
        print("恭喜猜对了")
        #在死循环中，在某个合适的时机跳出循环
        break

print("你总共猜了%d次" % (counter))

if counter >= 7:
    print("你的智商余额明显不足，请充值")