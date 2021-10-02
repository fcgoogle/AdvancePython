"""
抽象基类
子类必须要继承并重写基类的特定的类方法，否则子类在初始化实例化的时候就会抛出异常（接口的强制规定）
可以模拟实现，通过在父类的类方法里抛出NotImplementedError
"""
from collections.abc import Sized
import abc


class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass


class RedisBase(CacheBase):
    def get(self):
        pass

    def set(self, key, value):
        pass


redis_base = RedisBase()


# 应用场景一：检查某个类，是否具有某种方法
class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    # 魔法函数可以增强类的功能，双下划线开头和结尾，python预先定义
    # 定义了该魔法函数之后，该类实例化的对象就会是一个可迭代的对象
    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)


com = Company(["bobby1", "bobby2"])

# 应用场景一：检查某个类，是否具有某种方法
print(hasattr(com, "__len__"))
print(len(com))

# 应用场景二：在某些情况下希望判定某个对象的类型
print(isinstance(com, Sized))

# 应用场景三：强制某个子类必须实现某些方法
# 实现了一个web框架，继承cache（redis， cache， memory_chache）
# 需要设计一个抽象基类，制定子类必须继承某些方法

# 如何去模拟一个抽象基类
# class CacheBase():
#     def get(self, key):
#         raise NotImplementedError
#
#     def set(self, key, value):
#         raise NotImplementedError
#
#
#
# class RedisCache(CacheBase):
#     pass

# 希望在初始化该类的时候就可以检查类方法，并抛出异常
# redis_cache = RedisCache()
# redis_cache.set("key", "value")
