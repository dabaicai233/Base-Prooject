"""
商品类：
	商品名称   商品价格   商品剩余量
"""

class Goods(object):
    def __init__(self,name,price,balance):
        self.name = name
        self.price = price
        self.balance = balance

    def __str__(self):
        return "【Goods】商品名称:%s 商品价格：%d  商品剩余量:%d" % (self.name,self.price,self.balance)
