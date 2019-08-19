import  os,pickle
from shopcar.goods import Goods

"""
仓库类：【信息保存在本地磁盘：程序刚启动时把列表先存储到文件中，之后使用再读取出来】
	商品列表
	       商品名称    	价格        剩余量
		Mac电脑	   	20000    100
		PthonBook 	30	  	200
		草莓键盘         80      	60
		iPhone		7000		70
"""
#不管是哪个位置获取，或者哪个用户获取，访问到的仓库都是同一个，使用单例设计模式
#装饰器实现单例
def singleton(cls):
    instance = None

    def getInstance(*args,**kwargs):
        nonlocal instance
        if not instance:
            instance = cls(*args,**kwargs)

        return instance
    return getInstance


#注意：单例只不过只能创建一个对象出来，其他的用法和普通类的用法完全相同
@singleton
class Storage(object):
    def __init__(self):
        self.load_goods()

    #加载商品：如果保存商品的文件存在，则需要将内容从文件中加载出来，如果文件不存在，需要生成文件，需要将商品信息写入到文件
    def load_goods(self):
        if not os.path.exists("goodslist.txt"):
            #将商品列表添加到文件中
            self.goodslist = []

            #模拟数据
            names = ["mac book",'kindle','python book','bicyle']
            prices = [8888,500,78,1000]
            balances = [23,54,54,100]

            #遍历列表，获取相同位置上的信息，构建商品对象，添加到商品列表中
            for i in range(len(names)):
                goods = Goods(names[i],prices[i],balances[i])
                self.goodslist.append(goods)

            #将商品列表写入到本地磁盘
            self.save_goods()

        else:
            #加载文件中的商品列表
            self.custom_load()

    #将数据持久化到磁盘上
    def  save_goods(self):
        with open("goodslist.txt", "wb") as f:
            pickle.dump(self.goodslist, f)

    #将磁盘上的数据读取出来
    def custom_load(self):
        with open("goodslist.txt", "rb") as f:
            self.goodslist = pickle.load(f)