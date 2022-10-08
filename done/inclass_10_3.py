import math

with open('yext.txt', 'r') as file:
    data = file.readlines()
#
#     for i, line in enumerate(data):
#         print(f'line {i + 1} has {len(line.split())} words and {len([i for i in line if i.isalpha()])} symbols')

with open('new.txt', 'w') as file:
    j = 0
    new = []
    while j < len(data):
        for i in range(0, len(data[j]) - 2, 2):
            file.write(f'{round((int(data[j][i]) + int(data[j+1][i+1]) + int(data[j][i+1]) + int(data[j+1][i+1]))/4)}')
        j += 2
        file.write('\n')


data = 'C2H5OH2'
data += ' '
dict1 = {}
for i in range(len(data) - 1):
    if data[i].isalpha():
        if data[i] not in dict1:
            if data[i + 1].isdigit():
                dict1[data[i]] = int(data[i + 1])
            else:
                dict1[data[i]] = 1
        elif data[i + 1].isdigit():
            dict1[data[i]] += int(data[i + 1])
        else:
            dict1[data[i]] += 1
            pass
        pass
    pass

print(dict1)




