# 5. Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза

lst = [1, 3, 4, 6, 7, 3, 9, 9, 0]

for i in range(len(lst)):
    lst.insert(i, lst.pop())

print(lst)
