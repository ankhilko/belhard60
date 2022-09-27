# class User(object):
#
#     def __init__(self, name: str, email: str, age: int):
#         self.name = name
#         self.email = email
#         self.age = age
#
#     def birthday(self, integer=1):
#         self.age += integer
#
#
# class Manager(User):
#     # def __init_subclass__(cls, **kwargs):
#     #     pass
#     def __int__(self, salary=100):
#         super.__init__()
#         self.salary = salary
#
#     def birthday(self, integer=1):
#         self.age += integer * 3
#
#
# class Boss(Manager):
#     def __init__(self, name: str, email: str, age: int):
#         super().__init__(name, email, age)
# # alt + ENTER
#
#
#
#
# vasya = Manager(
#     "Vasya",
#     "e@mail.ru",
#     40
# )
#
# print(vasya.age)
# vasya.birthday()
# print(vasya.age)
#
#

# class CRUDUser():
#
#     def create(self):
#         pass
#
#     def read(self):
#         pass
#
#     def update(self):
#         pass
#
#     def delete(self):
#         pass
#
#
# class CRUDCategory():
#
#     def create(self):
#         pass
#
#     def read(self):
#         pass
#
#     def update(self):
#         pass
#
#     def delete(self):
#         pass
#
#
# crud = CRUDUser()
#
#
# def foo(crud):
#     crud.get()

#
# class Class:
#     def foo(self): # public method
#         print('foo')
#         pass
#     def __foo(self): # private class method
#         print('foo')
#         pass
#     def _bar(self): # protected method
#         print('bar')
#         pass
#
#
# c = Class()
# c.__bar()

# class User:
#
#     def __init__(self, card_number: str):
#         self.__card_number = card_number # не будет наследоваться приопределении субкласса!!!!!
#
#     @property
#     def card_number(self):
#         return '**** **** **** ' + self.__card_number[-4:]
#
#     @card_number.setter
#     def card_number(self, value):
#         self.__card_number = value
#
#
# class Manager(User):
#     def __init__(self, card_number: str):
#         super().__init__(card_number)
#         self.__card_number = card_number
#     @property
#     def card_number(self):
#         return self.__card_number
#
#     @card_number.setter
#     def card_number(self, value):
#         self.__card_number = value
#
#
# vasya = Manager('2434 3423 2342 3242')
#
# print(vasya.card_number)


# from abc import ABC, abstractmethod
# # for all abstract classes
#
# class User(ABC):
#     @abstractmethod # обязательный к определению в дочернем классе!!!!!
#     def foo(self):
#         pass
#
#     def bar(self):
#         print('bar')
#
# class Manager(User):
#     def __init__(self):
#         pass
#
#     def foo(self):
#         print('foo')
#
#
# user = Manager()
#
# user.foo()
# user.bar()
#

# from dataclasses import dataclass
#
# @dataclass
# class User:
#     name: str
#     email: str
#     age: int
#     pass
#
# vasya = User(name='Vasya', email='vasya@info.com', age=20)
#
# vasya.email = 'v@info.com'
#
# print(vasya)
#
# print(vasya.__dict__)
#
# petya = User(**{'name': 'Petya', 'email': 'vasya@info.com', 'age': 20})
# print(petya)





