# 6. Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные

lst = [1, 3, 4, 6, 7, 10, 9, 7]


def reverse_2_even_odd(lst):
    lst.sort()
    res = list(filter(lambda x: not x % 2, lst)) + list(filter(lambda x: x % 2, lst))
    return res


print(reverse_2_even_odd(lst))
