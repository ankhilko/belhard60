# **Вывести четные числа от 2 до N по 5 в строку

n = None

while not n:
    try:
        n = int(input())
    except ValueError:
        print('you need to input an integer: ')

for i in range(2, n + 1, 10):
    for j in range(i, min(i + 9, n + 1), 2):
        print(j, end=' ')
    print()
