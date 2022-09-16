# Вывести первые N цисел кратные M и больше K

n = None
m = None
k = None

while not n:
    try:
        n = int(input('введите N: '))
    except ValueError:
        print('вводить можно только целое число!')

while not m:
    try:
        m = int(input('введите M: '))
    except ValueError:
        print('вводить можно только целое число!')

while not k:
    try:
        k = float(input('введите K: '))
    except ValueError:
        print('вводить можно только число!')

counter = 0

number = int(k + 1)

list_of_numbers = []

while counter < n:
    if not number % m:
        list_of_numbers.append(number)
        counter += 1
    number += 1

print(list_of_numbers)
