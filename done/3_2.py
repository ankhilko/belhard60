# Пользователь вводит 3 числа, найти среднее арифмитическое с точность 3

# так как в ТЗ не указано, то требуем от пользователся вводить через пробел

num_1_2_3 = input('Пожалуйста, введите три числа через пробел: ')

num_1, num_2, num_3 = num_1_2_3.strip().split()
num_1 = float(num_1)
num_2 = float(num_2)
num_3 = float(num_3)

result = round((num_1 + num_2 + num_3) / 3, 3)

print(f'среднее арифмитическое данных чисел равно {result}')
