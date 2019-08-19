#.自定义一个类，其中定义实例函数，静态函数和类函数，并重写str函数，在类外面进行调用各个函数
class CustomClass(object):
    def __init__(self, name):
        self.name = name


# 实例函数
def show(self):
    pass


# 类函数
@classmethod
def func1(cls):
    pass


# 静态函数
@staticmethod
def func2():
    pass


# 重写__str__函数
def __str__(self):
    # 注意：返回的一定是一个字符串
    return self.name