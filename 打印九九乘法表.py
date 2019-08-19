# 用for...in...打印九九乘法表：
for a in range(1,10):
    for b in range(1,a+1):
        print("%sx%s=%s" % (b,a,a*b),end = " ")
    print()

# 用 while 打印九九乘法表：
a = 1
while a < 10:
    b = 1
    while b < a+1 :
        print("%sx%s=%s" % (b,a,a*b),end = " ")
        b += 1
    a += 1
    print()