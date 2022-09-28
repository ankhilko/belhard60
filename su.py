import random
from pprint import pprint

numbers = [list(range(1, 10)) for i in range(9)]
for lst in numbers:
    random.shuffle(lst)

su = [[' ' for i in range(3)] for j in range(3)]

for i in range(3):
    for j in range(3):
        # su.append()
        pass
for line in su:
    print(line)

for i in range(9):
    pass

pprint(numbers)


def fill_3(lst):
    for line in lst:
        yield line

