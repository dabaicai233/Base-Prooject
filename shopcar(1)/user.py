"""
用户类：
	姓名  用户id【这个标识对于每个用户而言是唯一的]】    密码     拥有购物车  用户登录状态【默认为 False 表示没有登录】
"""
class User(object):
    def __init__(self,name,uid,psd,shoppingcar):
        self.name = name
        self.uid = uid
        self.psd = psd
        self.shoppingcar = shoppingcar
        #登录状态
        #实例属性如果在程序开始的时候由默认值，则不需要在构造函数中预留对应的参数，否则用户可以进行任意的传值
        self.isLogin = False


    def __str__(self):
        return "【User】姓名：%s 密码：%s 用户id：%s 是否登录：%s" % (self.name,self.psd,self.uid,self.isLogin)