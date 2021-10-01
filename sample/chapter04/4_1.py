"""
鸭子类型,就像魔法函数，函数不与本身所在的类绑定，
任何类都可以写上该函数，并因此给该类赋予这个魔法函数的一些特性，比如可迭代性
"""


class Cat:
    def say(self):
        print("i'am a cat.")


class Dog:
    def say(self):
        print("i'm a dag.")

    # def __iter__(self):
    #     pass

    def __getitem__(self, item):
        return 'bobby'


class Duck:
    def say(self):
        print("i'm a duck.")


animal_list = [Cat, Dog, Duck]
# 三个类都定义了同名的say方法，实现了类似静态语言中多态的特性
for animal in animal_list:
    animal().say()


a = ['bobby1', 'bobby2']
b = ['bobby2', 'bobby1']

name_tuple = ('bobby3', 'bobby4')
name_set = set()
name_set.add("bobby5")
name_set.add("bobby6")

# a.extend(b)
# extend传入一个可迭代的对象即可，默认会调用对象内部的__iter__方法，或者__getitem__方法，来
# a.extend(name_set)
# print(a)


dog = Dog()
a.extend(dog)

