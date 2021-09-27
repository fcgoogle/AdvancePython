def ask(name="bobby"):
    print(name)


def decorator_func():
    print("dec start")
    return ask


my_ask = decorator_func()
my_ask("tom")


#
# class Person:
#     def __init__(self):
#         print("bobby1")


# obj_list = [ask, Person]
# for item in obj_list:
#     print(item())

# my_func = ask
# my_func('bobby')
# my_class = Person
# my_class()


