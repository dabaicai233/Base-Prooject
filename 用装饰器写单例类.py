def singleton1(cls):
    instance = None  # 代表的是被修饰的类的实例

    def currentInstance(*args, **kwargs):
        nonlocal instance
        if not instance:
            instance = cls(*args, **kwargs)

        return instance

    return currentInstance


@singleton1
class Xxx():
    pass


def singleton2(cls):
    instanceDict = {}

    def currentInstance(*args, **kwargs):
        if cls not in instanceDict:
            instanceDict[cls] = cls(*args, **kwargs)

        return instanceDict[cls]

    return currentInstance