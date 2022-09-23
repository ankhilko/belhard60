# 7. Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка

lst = [2, 3, 4, 5, 6, 7, 8, 8]

new_lst = []
for i in range(len(lst)):
    if i == len(lst) - 1:
        new_lst.append(lst[i - 1] + lst[0])
        continue
    new_lst.append(lst[i - 1] + lst[i + 1])

print(new_lst)
