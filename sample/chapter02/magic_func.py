"""
魔法函数一览
"""


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    # def __str__(self):
    #     return ",".join(self.employee)

    def __repr__(self):
        return ",".join(self.employee)


company = Company(["tom", "bob", "jane"])

# 此时隐性的调用了str（company）,在使用内置函数str时候，又调用了类中的魔法函数str
print(company)
print(str(company))


class Nums(object):
    def __init__(self, num):
        self.num = num

    def __abs__(self):
        return abs(self.num)


my_num = Nums(-19)
print(abs(my_num))


class MyVector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # 矢量的x，y轴各自相加后，在传如类模版中，新实例话一个矢量对象
        re_vector = MyVector(self.x + other.x, self.y + other.y)
        return re_vector

    def __str__(self):
        # 两种格式化显示的方案
        return f'x:{self.x}, y:{self.y}'
        # return "x:{x}, y:{y}".format(x=self.x, y=self.y)


first_vector = MyVector(1, 2)
second_vector = MyVector(2, 3)
print(first_vector + second_vector)


