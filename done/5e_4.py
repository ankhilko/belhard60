# 4. Вводится число N, вывести первые N чисел последовательности Фибоначи

n = int(input('ввдите целое число: '))

fibonacci = []

for i in range(n):
    if i in [0, 1]:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[i - 2] + fibonacci[i - 1])

print(fibonacci)
