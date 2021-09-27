"""
type -> class -> object

python所有东西，一切皆对象
python一切对象都继承object对象

type即是一个对象，也是一个类
python所有东西都是type类的实例，包括它自己，type对象是type类自己的实例
"""
print(type(type))
print(type(object))
print(3>2==2)
x = 43
ch = 'A'
y = 1
print(x>=y and ch<'b' and y)
print(3**3)
k = 1000
while k > 1:
    print(k)
    k = k / 2

dict2 = {123: 123}
print(dict2)
