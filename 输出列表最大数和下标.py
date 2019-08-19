#输出最大数和下标
l1 = [1,2,3,4,5,6,10,7,8,9]
max =l1[0]
for n in range(len(l1)):
    if l1[n]>max:
        max=l1[n]
        m=n
print(m,max)