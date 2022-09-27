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

class CRUDUser():

    def create(self):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
class CRUDCategory():

    def create(self):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

crud = CRUDUser()

def foo(crud):
    crud.get()




