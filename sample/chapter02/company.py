"""
什么是魔法函数？
"""


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    # 魔法函数可以增强类的功能，双下划线开头和结尾，python预先定义
    # 定义了该魔法函数之后，该类实例化的对象就会是一个可迭代的对象
    # def __getitem__(self, item):
    #     return self.employee[item]

    def __len__(self):
        return len(self.employee)


company = Company(["tom", "bob", "jane"])
# 序列切片背后的原理，实质上是因为该数据类型存在特定的魔法函数，赋予了其
# 可切片，可遍历,可计算长度等序列的特性
# company1 = company[:2]


emploee = company.employee
# for em in emploee:
#     print(em)

# for循环company对象的时候，对象会优先寻找iter魔法函数
# 如果找到，for循环则会拿到一个迭代器
# 找不到则寻找getitem，然后每次循环即调用魔法函数getitem
# 直到抛出异常则结束for循环
# for em in company:
#     print(em)

print("------------------")
# for em1 in company1:
#     print(em1)

# 类定义中，实现了len的魔法函数，则可以在外部对对象使用内置len（）时调用类中的
# 魔法函数len，如果没有会退而求其次寻找getitem魔法函数，多次调用getitem直到发出异常
print(len(company))
