# 1. Написать программу генерации треугольника паскаля указанной глубины

n = None

while not n:
    try:
        n = int(input())
        if n < 1:
            raise ValueError
    except ValueError:
        print('you need to input an integer bigger than 0: ')

triangle = []
triangle2 = []

temp = [1]

triangle.append(list(tuple(temp)))
triangle2.append(' '.join(str(i) for i in temp))

if n == 1:
    pass
else:
    for row_number in range(1, n):
        for position in range(1, row_number):
            temp[position] = triangle[row_number - 1][position] + triangle[row_number - 1][position - 1]
        temp.append(1)
        triangle.append(list(tuple(temp)))
        triangle2.append(' '.join(str(i) for i in temp))

for item in triangle:
    print(item)

for item in triangle2:
    print(item.center(len(triangle2[-1]), ' '))
