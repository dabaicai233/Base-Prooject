"""
因为一个程序可能有很多用户，则需要将用户保存在本地
			将注册的用户添加在字典中
				key：用户id 【用户id随机产生即可，从10000~99999中随机产生一个】
				value：对应的用户对象

	行为：
	用户注册——》根据下面信息生成一个用户，并将用户保存在本地
		随机产生 id
		输入姓名和密码
		创建一个购物车对象


	登录 ——》 登录成功返回为 True  否则返回为 False
		输入用户id 检测是否有该用户  没有的话提示注册
		有的话检测用户登录状态 若为 True  提示已登录
		否则 再输入密码进行登录
			不要忘记修改用户的登录状态

	购买商品 ——》验证用户是否登录，没有登录提示登录
		否则
			列出仓库中商品名单
				1. Mac电脑
				2.PthonBook
				3.草莓键盘
				4.iPhone
			用户输入对应的编号 在仓库中获得对应的商品
			用户输入数量 — 与该商品的的剩余量对比
				> 剩余量
					让用户重新输入并提示该商品的剩余量
				<=剩余量
					将该商品添加在该用户的购物车中
					并将仓库中的数据量做出相应的减少
				注意：将修改之后的结果同步在本地文件中，时刻保持数据的正确性

	删除购物车的商品——》验证用户是否登录，没有登录提示登录
		否则
			请用户输入商品名字 查看该用户的购物车中是否有该商品
			如果没有，提示购物车中没有该商品
			否则：
				先选择要删除的商品
				请用户设置删除的数量
					数量  >=   购物车中商品数量
						购物车清单中删除该商品
					否则：
						购物车清单中做出相应的减少
			注意：将修改之后的结果同步在本地文件中，时刻保持数据的正确性


	结算——》验证用户是否登录 没有登录提示登录
		否则
			获取该用户的购物车中商品清单，计算总额
		注意： 结算完成 购物车清空
			  将修改之后的结果同步在本地文件中，时刻保持数据的正确性


	退出登录———》验证用户是否登录 没有登录提示登录
		否则
			修改用户登录状态
		注意：将修改之后的结果同步在本地文件中，时刻保持数据的正确性
"""
from  shopcar.goods import  Goods
from  shopcar.user import  User
from  shopcar.shoppingcar import  ShoppingCar
from  shopcar.storage import  Storage
import  os,pickle,random

class Operation(object):
    #当程序启动的时候，加载本地用户文件，判断文件是否存在
    def __init__(self):
        self.load_all_user()

    def load_all_user(self):
        #存在
        if os.path.exists("user.txt"):
            with open("user.txt","rb") as f:
                self.userDict = pickle.load(f)
        #不存在
        else:
            #定义一个字典
            self.userDict = {}

    #保存用户的信息到本地磁盘
    def save_user(self):
        with open("user.txt", "wb") as f:
            pickle.dump(self.userDict,f)

    #随机生成 一个用户id
    def get_uid(self):
        #用户id是唯一的，一定不能出现重复的情况
        #获取随机数的过程中，如果发现随机数在字典中已经存在，则重新获取
        while True:
            uid = str(random.choice(range(10000, 100000)))

            if uid not in self.userDict:
                return uid

    #注册
    def user_register(self):
        #获取用户id
        uid = self.get_uid()
        print("你的用户id是：%d" % (uid))
        #购物车对象
        sp = ShoppingCar()
        #用户名和密码
        username = input("请输入你的姓名：")
        pwd = input("请输入你的密码：")
        #根据以上的信息创建用户的对象
        user = User(username,uid,pwd,sp)

        #将创建好的用户的对象添加到用户字典中保存起来
        #uid作为key，用户对象作为value
        self.userDict[uid] = user

        #将信息同步到本地文件
        self.save_user()

        print("注册成功")

    #登录
    def user_login(self):
        uid = input("请输入用户的id：")
        #判断uid在字典中是否存在
        if uid not in self.userDict:
            print("用户id不存在，请先注册")
            #self.user_register()
            return

        #在uid存在的情况下，判断用户当前的登录状态
        #根据uid获取对应的用户对象
        user = self.userDict[uid]

        if user.isLogin:
            #已经登录成功
            return user

        #未登录
        while True:
            psw = input("请输入密码：")
            if psw == user.psd:
                # 修改用户的登录状态
                user.isLogin = True

                print("登录成功")
                return user
            else:
                print("请输入正确的密码：")

    #购买商品
    def add_goods(self):
        #在添加商品之前，校验用户是否登录成功
        user = self.user_login()

        if user == None:
            print("请先进行登录")
            return

        #说明用户登录成功
        print("商品列表如下：")
        print("""
        0.Mac book
        1.kindle
        2.python book
        3.bicyle
        """)

        #引导用户选择商品
        index = input("请输入需要添加的商品编号：")
        if index.isdigit():
            #用户选择的商品编号同时也是从列表中获取商品对象的下标
            index = int(index)

            if index >= 0 and index <= 3:
                #获取仓库对象
                storage = Storage()
                #从仓库对象的商品列表中获取指定的商品对象
                goods = storage.goodslist[index]

                #引导用户输入需要购买的商品数量
                num = int(input("请输入需要购买的商品数量;"))

                if num < 0:
                    print("输入有误")
                else:
                    #判断用户输入的数量和库存量之间的关系
                    if num <= goods.balance:
                        # 根据用户的选择，重新实例化对象【需要添加到用户购物车中的对象】
                        user_goods = Goods(goods.name,goods.price,num)
                        #仓库中的剩余量需要发生改变
                        goods.balance -= num

                        #将重新实例化的对象添加到购物车中
                        #商品对象作为key，商品数量作为value
                        user.shoppingcar.goodsDict[user_goods] = num

                        #保持用户和仓库中本地文件的同步
                        self.save_user()
                        storage.save_goods()

                        print("商品添加成功")
                    else:
                        print("剩余量不足，为:%d件" % (goods.balance))
            else:
                print("该商品还未上架")

        else:
            print("编号输入有误")

    #删除商品
    def del_goods(self):
        # 在删除商品之前，校验用户是否登录成功
        user = self.user_login()

        if user == None:
            print("请先进行登录")
            return

        #说明登录成功
        gname = input("请输入需要删除的商品的名称:")

        #定义一个变量，获取需要被删除的商品对象
        goods = None
        #定义一个变量，用于标记商品是否存在
        flag = False   #默认不存在

        #遍历用户的购物车的字典
        for user_goods in user.shoppingcar.goodsDict:
            if user_goods.name == gname:
                goods = user_goods
                flag = True

        if not flag:
            print("商品不存在")
            return


        #操作仓库
        #在仓库中获取该商品
        storage = Storage()

        index = 0
        for i in range(len(storage.goodslist)):
            if storage.goodslist[i].name == gname:
                index = i

        #通过商品的位置获取商品的对象
        storage_goods = storage.goodslist[index]

        #引导用户输入需要删除的商品数量
        num = int(input("请输入需要删除的商品数量："))

        if goods.balance >= num:
            #将该用户对应的商品删除
            goods.balance -= num
            #购物车中的商品数量，字典重新赋值
            user.shoppingcar.goodsDict[goods] = goods.balance

            #仓库中添加回同等的数量
            storage_goods.balance += num
        else:
            #将购物车中的商品删除
            user.shoppingcar.goodsDict.pop(goods)
            #在仓库中添加回去
            storage_goods.balance += goods.balance

        #同步数据到本地文件
        self.save_user()
        storage.save_goods()

    #结算购物车
    def get_acount(self):
        user = self.user_login()

        if user == None:
            print("请先进行登录")
            return

        #获取
        total = 0
        for key,value in user.shoppingcar.goodsDict.items():
            total += value * key.price

        print("总计为：%d" % (total))

        #清空购物车
        user.shoppingcar.goodsDict.clear()

        #保存用户信息
        self.save_user()

    #退出
    def user_exit(self):
        user = self.user_login()

        if user != None:
            #修改登录状态为False
            user.islogin = False
            #同时需要保存到本地文件中
            self.save_user()

