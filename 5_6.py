# 6) 3. Вводятся две строки, a и b, и возвращать количество раз,
# когда в обеих строках под одинаковыми индексами стоит одна и та же пара букв.

a = input('строка \'a\': ')
b = input('строка \'b\': ')
x = 0

for i in range(min(len(a), len(b))):
    if a[i] == b[i]:
        x += 1

print(f'в обеих строках под одинаковыми индексами стоит {x} пар букв')
