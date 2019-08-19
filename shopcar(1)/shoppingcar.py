"""
购物车类：
	商品列表：程序初始时，商品列表为空
"""
class ShoppingCar(object):
    def __init__(self):
        #向购物车中存储商品，商品对象的为key，数量为value
        self.goodsDict = {}

    def __str__(self):
        return "【ShoopingCar】%s" % (self.goodsDict)