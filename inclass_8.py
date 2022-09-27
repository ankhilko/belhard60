class User(object):

    def __init__(self, name: str, email: str, age: int):
        self.name = name
        self.email = email
        self.age = age

    def birthday(self, integer=1):
        self.age += integer


class Manager(User):
    # def __init_subclass__(cls, **kwargs):
    #     pass
    def __int__(self):
        super.__init__()


vasya = Manager(
    "Vasya",
    "e@mail.ru",
    40
)

print(vasya.age)
vasya.birthday()
print(vasya.age)

