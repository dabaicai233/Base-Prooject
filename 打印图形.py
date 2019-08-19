#打印固定行数的正三角形;
#用for打印
n = int(input("请输入行数："))
for b in range(n+1):
        print(" "*(n-b)+"*"*(2*b-1))

#用while打印正三角形
i=1
while i <= n:
    print(" " * (n - i) + "*" * (2 * i - 1))
    i+=1


#打印直角三角形：
for a in range(n+1):
    print("*"*a)


# 打印空心直角三角形
for a in range(n+1):
    for b in range(a+1):
        if a == n:
            print("*",end=" ")
            continue
        if b==0 or b==a:
            print("*",end=" ")
        else:
            print(" ",end =" ")
    print()

# 打印正方形
n = int(input("请输入行数："))
for i in range(n):
    print(" * " * n)
# 打印空心正方形：
n = int(input("请输入行数："))
i = k = 1
for i in range(1, n + 1):
    for k in range(1, i + 1):
        if i != 1 or i != n:
            if k == 1 or k == n:
                print(" * " * n, end=" ")
            else:
                print(" " * n, end=" ")
        else:
            print(" * " * n, end=" ")

#打印右半边菱形
n=int(input("请输入行数："))
#for a in range(n+1):
#   for m in range(a+1):
c=n
b=n
for i in range(1,n+1):
    print("*" * (2 * i - 1),"  " * (c - 1))
    c-=1
if(i==n):
    for y in range(1, n):
        print("*" * (2 * b - 3),"  " * y)
        b = b - 1
#打印左半边时将星号和空格位置调换就行
