# 7) 4. Дан список чисел, отсортировать его по возрастанию без использования sort и sorted

list_of_numbers = input('введите числа: ').split()

for n in range(len(list_of_numbers)):
    list_of_numbers[n] = int(list_of_numbers[n])

for i in range(len(list_of_numbers)):
    j = 0
    while j < len(list_of_numbers) - 1:
        if list_of_numbers[j] > list_of_numbers[j + 1]:
            list_of_numbers[j], list_of_numbers[j + 1] = list_of_numbers[j + 1], list_of_numbers[j]
        j += 1

print(list_of_numbers)
