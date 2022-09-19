# Заполнить список степенями числа 2 (от 2^1 до 2^n).

n = int(input('ведите n: '))
list_2n = [2**i for i in range(1, n + 1)]
print(list_2n)
