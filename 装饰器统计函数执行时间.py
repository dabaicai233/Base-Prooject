#需求：书写一个装饰器，统计一个函数执行需要的时间
import time
def wrapper(f):
 def inner():
     t1 = time.time()
     f()

     t2= time.time()

     print("函数执行需要的时间为：",t2 - t1)

 return  inner
@wrapper
def show():
 for i in range(100000):
     i += 1

show()