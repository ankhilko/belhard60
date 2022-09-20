

a = ['qwerty']
print(a[40:10])

# %s - string
# %d - decimal

name = "ddasda"
text2 = ' fdf sdf {} {} {}'.format(name, name, name)
"asufauf %s" % (name)

import babel
"doesn't suport f-strings - only .format() ((("

text = "as fd a sd".split(sep=" ", maxsplit=2)

text1 = " separator ".join(text)

print(text)

start_position, end_position = 0, 10

finding = text1.find("string to find", start_position, end_position)

rfinding = text1.rfind("d", start_position, end_position)


print(finding)

index()
rindex()



print(text1.partition("d"))

print(text1.replace(" ", "wadhawudhw", 2))
s = "dasda"

s.isdigit()
s.isdecimal() # десятичное число
s.isnumeric()

s.isalpha()
s.isalnum() # только буквы и / или цифры
s.isidentifier() # роверяетб может ли быть наименованием переменной
s.isspace() # пустые (пробельные символы - разрелители) символы
s.startswith(" ") #
s.endswith(" ") #






s.islower()
s.isupper()
s.istitle() #первая буква каждогос слова большая остальные мал

s.lower()
s.upper()
s.title()
s.strip()
s.capitalize() # первая буква в строке - болшаяб остальные малые
s.swapcase()

s = "100000000dddd\t10"

print(s.expandtabs(20))

s.rstrip()
s.lstrip()
s.strip()
print(s.strip("10")) # удаляет любые символы входяящие в строку вначале и в конце

s.removeprefix("d")
s.removesuffix("da")

s.zfill(10)

s.rjust(10, "ddd")
s.ljust(10, "ddd")

s.encode()
s.decode()


a = 13
b = 21
print(bin(a))
print(bin(b))
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
# + 1 * (-1) - индекс элемента с противоположной стороны в строке
# зеркалим

a >> 3
b << 3
# обавить или удалить биты в числе или символе

n = not False or True and False
print(n)
