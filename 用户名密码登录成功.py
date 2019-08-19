usename = input("请输入你的用户名：")
password = input("请输入密码：")
if usename == "admin" and password == "123abc":
    print("登录成功")
else:
    print("用户名或密码错误！")