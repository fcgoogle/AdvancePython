"""
什么是魔法函数？
"""


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    # 魔法函数可以增强类的功能，双下划线开头和结尾，python预先定义
    # 定义了该魔法函数之后，该类实例化的对象就会是一个可迭代的对象
    def __getitem__(self, item):
        return self.employee[item]


company = Company(["tom", "bob", "jane"])


emploee = company.employee
# for em in emploee:
#     print(em)

# for循环company对象的时候，对象会优先寻找iter魔法函数
# 如果找到，for循环则会拿到一个迭代器
# 找不到则寻找getitem，然后每次循环即调用魔法函数getitem
# 直到抛出异常则结束for循环
for em in company:
    print(em)
