#练习：求1~某个数之间的和，用递归实现
#循环求和
def add1(num):
    sum = 0
    # for i in range(1,101):
    #     sum += i
    n = 1
    while n <= num:
        sum += n
        n += 1

    return sum
print(add1(100))

#递归求和
"""
1+2+3+4.。。。。+100


临界值：1
公式：func(n - 1) + n

分析：求1~4之间的整数的和
func(4) = func(3) + 4
func(3) = func(2) + 3
func(2) = func(1) + 2

....

func(n) = func(n - 1) + n
"""
def add2(num):
    if num == 1:
        return 1
    else:
        return add2(num - 1) + num

print(add2(100))

#练习：求某个数的阶乘
def add2(num):
    if num == 1:
        return 1
    else:
        return add2(num - 1) *num

print(add2(100))