# 1. Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int

def int_to_bin(int_n):
    res = []
    while int_n > 0:
        if int_n % 2 == 0:
            res.insert(0, '0')
        else:
            res.insert(0, '1')
        int_n //= 2
    return ''.join(res)


def bin_to_int(bin_n):
    res = 0
    for i, n in enumerate(str(bin_n)):
        res += float(n) * 2**(len(str(bin_n)) - 1 - i)
    return round(res)


print(int_to_bin(19))

print(bin_to_int(10100))
