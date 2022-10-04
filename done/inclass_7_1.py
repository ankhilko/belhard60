
# class Rectangle():
#
#     def __init__(self, a: tuple, b: tuple) -> None:
#         self.a = a
#         self.b = b
#         self.x = abs(self.a[0] - self.b[0])
#         self.y = abs(self.a[1] - self.b[1])
#         pass
#
#     def area(self) -> int:
#         return self.x * self.y
#
#     def perimetr(self) -> int:
#         return (self.x + self.y) * 2
#
#     pass
#
#
# rect = Rectangle((4, 3), (1, 1))
# print(rect.area())
# print(rect.perimetr())

# написать класс Person - на вхо коснтруктора поступает возраст и имя
# birthday увеличивает возраст, когда возраст увеличивает и запрашивает
# surname

# class Person():
#
#     def __init__(self, age: int, name: str) -> None:
#         self.name = name
#         self.age = age
#         if self.age < 0:
#             print('не смешно')
#
#         self.surname: str
#         pass
#
#     def birthday(self):
#         self.age += 1
#         print(f'{self.name} стал старще на 1 год. Теперь {self.name} {self.age} лет')
#         if self.age == 18:
#             self.surname = input('введите фамилию: ')
#
# petia = Person(int(input('введите возраст: ')), input('введите имя: '))
#
# for i in range(18):
#     petia.birthday()


# Написать класс Markup, на вход конструктора поступают данные о товаре: название, описание, цена
# Метод markdown, формирует из исходных данных текст, в котором название обернутов в **,
# описание __, а цена ~~
# Title
# Very Cool Description
# 100USD
# Метод html, формирует из исходных данных текст, в котором название обернутов в <b></b>,
# # описание <i></i>, а цена <strike></strike>
# <b>Title</b>
# <i>Very Cool Description</i>
# <strike>100USD</strike>

# class Markup():
#
#     def __init__(self, title: str, description: str, price: int) -> None:
#         self.title = title
#         self.description = description
#         self.price = price
#
#         pass
#
#     def markdown(self):
#         a = '**' + self.title + '**'
#         b = '--' + self.description + '--'
#         c = '~~' + str(self.price) + '~~'
#         return a + '\n' + b + '\n' + c
#
#     def html(self):
#         a = '<b>' + self.title + '</b>'
#         b = '<i>' + self.description + '</i>'
#         c = '<strike>' + str(self.price) + '</strike>'
#         return a + '\n' + b + '\n' + c
#
#
#
# towar = Markup('Товар', 'Описание', 150)
#
# print(towar.markdown())
# print(towar.html())

# import re
# url = input("url: ").strip()
# username = re.search(r".*/(.+)$", url).group(1)
# print(username)

import pandas

list2 = pandas.read_excel('exl.xlsx')


