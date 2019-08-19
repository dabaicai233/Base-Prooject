#1.简单的装饰器
def test():
    print("hello")

#test()

#装饰器的书写步骤
#a。书写闭包
#b。给外部函数设置参数，参数是函数，fun是一个形参，需要传一个函数的实参，标识符可以自定义
def outter1(fun):
    def inner1():
        # d。增加新的功能【说明：调用原函数和增加新功能没有一定的顺序要求，根据需求决定】
        print("123124")

        #c.调用原函数
        fun()
    return  inner1

#注意1：需要被装饰的函数作为外部函数的参数，调用的时候必须保持参数的一致
f1 = outter1(test)     #fun = test     f1 = inner1
#注意2：f1相当于指向内部函数，则调用的时候也需要和内部函数的参数保持一致
f1()

#注意3：将一个被需要增加功能的函数传递给闭包，经过装饰之后，需要将装饰的结果返回【两个要素：参数，返回值】
#练习：给下面的函数增加功能，打印九九乘法表
def show():
    for i in range(10):
        print(i)

def func1(f):
    def func2():
        f()
        for i in range(1,10):
            for j in range(1,i + 1):
                print("%dx%d=%d" % (j,i,i *j),end=" ")

            print("")
    return  func2

result = func1(show)
result()

print("*" * 20)

#2.有参数的装饰器
def getAge(age):
    print("年龄：%d" % (age))

# getAge(18)
# getAge(-10)

#需求：在不修改原函数的基础上，进行数据的过滤【校验】，如果用户输入的数据为负数，置为正数
def wrapper(f):
    def inner(num):
        #增加新的功能
        if num < 0:
            num = -num

        #调用原函数
        f(num)

    return inner

f2 = wrapper(getAge)
f2(18)
f2(-10)

#有参数的装饰器的使用场景：需要被装饰的函数有参数，增加新功能的过程中需要操作参数


print("====" *  20)

#3.使用@可以将装饰器直接应用到指定的函数
#Python2.4支持使用标识符@将装饰器应用到函数中，只需要在装饰器的名称前面添加@

#注意：采用@使用装饰器，则装饰器必须出现在被需要装饰的函数的前面
def wrapper1(f):
    def inner(num):
        #增加新的功能
        if num < 0:
            num = -num

        #调用原函数
        f(num)
    return inner

#注意：该步操作只是将被需要装饰的函数传参给装饰器
@wrapper1
def getAge1(age):
    print("年龄：%d" % (age))

#注意：该步实际触发了内部函数的调用
getAge1(18)
getAge1(-10)

print("***" * 20)

#4.同一个装饰器应用于不同的函数,给不同的函数动态增加同一个功能
#注意：不同的函数可能存在参数不一致的情况，装饰器必须是通用的，采用不定长参数
def wrapper2(func):
    def inner(*args,**kwargs):
        print("124324")

        func(*args,**kwargs)

    return inner

@wrapper2
def func1():
    print("func1")

@wrapper2
def func2(a,b):
    print("func2",a,b)

@wrapper2
def func3(num1,num2,num3):
    print("func3",num1,num2,num3)

#注意：一个函数被装饰器应用之后，执行的顺序：外部函数----->内部函数----》原函数
func2(1,2)
# f = wrapper2(func2)
# f(1,2)

func3(34,6,65)

print("*" * 20)

#5.将多个装饰器作用于同一个函数：为了给该函数增加多个不同的功能
def wrapper51(func):
    def inner(*args,**kwargs):

        func(*args,**kwargs)
        print("装饰器1~~~~")

    return  inner

def wrapper52(func):
    def inner(*args, **kwargs):

        func(*args, **kwargs)
        print("装饰器2~~~~")
    return inner


@wrapper51
@wrapper52
def func5():
    print("func~~~~5")
func5()

"""
1.func5----->print("func~~~~5")
2.func5给wrapper51传参
3.func5----->装饰之后的函数


注意：如果有多个装饰器作用域同一个函数，则每个装饰器中传递的函数是不一样的
      哪个装饰器靠近原函数，则将原函数传递给该装饰器，其他的装饰器中传递的函数都是上一个装饰器装饰的结果

@wrapper51
@wrapper52
def func5():
    print("func~~~~5")

wrapper52（func5）---->得到装饰之后的函数
wrapper51（装饰之后的函数）

结论：不管有多少个装饰器同时作用于同一个函数，原函数只会被执行一次，装饰器按照顺序执行
"""

#练习;
def wrapper61(func):
    def inner(*args,**kwargs):
        func(*args,**kwargs)
        for i in range(3):
            print(i)

    return  inner

def wrapper62(func):
    def inner(*args, **kwargs):

        print("wrapper 6~~~~2")
        func(*args, **kwargs)
    return inner

@wrapper62
@wrapper61
def test():
    print("test")

test()
"""
wrapper 6~~~~2
test
0
1
2
"""








