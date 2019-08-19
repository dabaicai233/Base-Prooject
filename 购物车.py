#购物车
"""
思路：
1.提示用户选择需要操作的功能：添加商品，删除商品，退出系统
2.引导用户输入金额
3.根据用户的选择执行不同的操作
"""

#商品列表
productList = [("food",18),("iphone",8000),("bike",888),("kindle",500),("pen",30)]


#购物车
shoppingCar = []

print("*********欢迎进入xxxx自选超市**********")

saving = input("请输入金额：")
if saving.isdigit():
    saving = int(saving)

    #加购商品并不是一次完成的，可能会进行无数次
    while True:
        print("1.添加商品\n2.删除商品\n3.退出系统")
        choice = input("根据上面的功能提示，请输入你的选择：")

        #判断输入功能的合法性
        if choice.isdigit():
            choice = int(choice)
            if choice >= 1 and choice <= 3:
                if choice == 1:
                    #添加商品
                    #展示商品
                    for i,product in enumerate(productList):
                        print(i,":",product)

                    #引导用户选择需要购买的商品的编号
                    index = int(input("请输入商品编号："))

                    #通过用户输入的商品编号获取商品
                    item = productList[index]   #item是一个元组，item[0]:商品名称 ，item[1]；商品价格

                    #如果金额足够，则可以加购
                    if item[1] < saving:
                        saving -= item[1]

                        #加购到购物车
                        shoppingCar.append(item)

                        print("商品加购完成")
                    else:
                        print("余额不足，还剩%d" % (saving))

                elif choice == 2:
                    #删除商品
                    if shoppingCar:
                        deleteProduct = input("请输入需要删除的商品名称：")

                        for product in shoppingCar:
                            if product[0] == deleteProduct:
                                shoppingCar.remove(product)

                        print("删除成功")
                        print("删除完成之后的购物车如下：")
                        for product in shoppingCar:
                            print(product)
                    else:
                        print("购物车为空，请先去加购商品")
                else:
                    #购物车结算
                    print("---------你已经加购了如下商品--------")
                    for product in shoppingCar:
                        print(product)

                    print("你还剩%d钱" % (saving))

                    #退出系统
                    break
            else:
                print("很抱歉，暂未开通该功能")
        else:
            print("功能选择有误")
else:
    print("金额输入有误")
