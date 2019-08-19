#测试文件


from shopcar.operation import Operation
def main():
    op = Operation()

    while True:
        print("1.注册 2.登录 3.添加商品 4.删除商品 5.结算购物车 6.退出")
        select = int(input("请输入你的选择："))
        if select == 1:
            op.user_register()
        elif select == 2:
            op.user_login()
        elif select == 3:
            op.add_goods()
        elif select == 4:
            op.del_goods()

        elif select == 5:
            op.get_acount()

        elif select == 6:
            op.user_exit()
            break
        else:
            print("输入有误")



if __name__ == "__main__":
    main()