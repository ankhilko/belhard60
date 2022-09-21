# 3. Вводится число, посчитать факториал этого числа

n = int(input('введите целое число: '))

result = 1
for i in range(0, n + 1):
    if i != 0:
        result *= i

print(f'{n}! = {result}')
