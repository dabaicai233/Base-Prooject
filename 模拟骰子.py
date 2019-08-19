import random
a  = random.choice(range(1,7))  #range(包含：起，终，步长，其中范围是包头不包尾)                               #也可以用 random.randint(1,6)【包头包尾】
print(a)
if a == 1:
    print("唱")
elif a == 2:
    print("跳")
elif a == 3:
    print("跑")
elif a == 4:
    print("吃")
elif a == 5:
    print("喝")
else:
    print("滚")