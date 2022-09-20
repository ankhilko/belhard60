# LIFO - last in first out
# FIFO - first in first out

# a = 2
# b = 5
#
# def function(arguments):
#     pass
#
# function(a)
#
# print(a)

# функция которая не возвращает - возвращает None )))


# функция с запахом )))
# def foo(a, lst=[]):
#     lst.append(a)
#     print(lst)
#
#
# function_name = 'foo'
# globals().get(function_name)(3)
# globals().get('foo')(4)

# a = 'global'

# def goo():
#     a = 'nonlocal'
#
#     def fooo():
#
#         nonlocal a
#         print(a)
#         a = 4
#         print(a)
#
#     fooo()
# goo()


# конфигурирование

# def foo():
#     pass
# def baz():
#     pass
# def error():
#     pass
#
# data = {
#     'a': foo,
#     'b': baz,
# }
#
# n = input()
#
# data.get(n, error)()



# func = lambda a, b: a * b
# print(func(a, b))


# применяет функцию к списку аргументов
# map(int, ['1', '2'])

# numbers = ['1', '2', '323', '33']
# print(list(map(lambda a: int(a) * 2, numbers)))
#
#
# # проверить, если функция возвращает True - то выбрать значение, если нет, скипнуть значение
# print(list(filter(lambda x: int(x) % 2, numbers)))
#
#
# def is_palind(text: str) -> bool:
#     pass
#
# text = 'qwertyui'
# lst = [1, 2, 3, 5]
# tup = (True, False)
#
# result = list(zip(text, lst, tup))
# print(result)
#
# from itertools import zip_longest
#
# result = list(zip_longest(text, lst, tup))
# print(result)


# def foo(a):
#     def baz(b):
#         return a+b
#     return baz

def foo(n):
    for i in range(n):
        yield i

print(list(foo(20)))

for j in foo(10):
    print(j)


# при рекурсии должа быть точка выхода

def multi(numb):
    res = 1
    for i in numb:
        if isinstance(i, (int, float)):
            res *= i
        else:
            res *= multi(i)
    return res

