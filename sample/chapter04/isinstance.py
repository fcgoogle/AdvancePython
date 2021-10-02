"""
尽量使用isinstance去判断类型
"""


class A:
    pass


class B(A):
    pass


b = B()
a = A()

print(isinstance(b, B))
# isinstance 会找到类的继承链
print(isinstance(b, A))

# is 和 == 符号不相同，is是用来判断两者ID是否相同，==符号是用来判断两者的值是否相等
print(type(b) is B)
print(type(b) is A)


