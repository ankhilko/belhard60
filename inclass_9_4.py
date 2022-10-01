from pprint import pprint

text = '''
Мобильный телефон 3000

ru от 1 от 18000

ru от 5 от 17000

Мобильный телефон 4000

fr от 1 от 18000

ru от 5 от 17000

Мобильный телефон 8900

en от 1 от 18000

ru от 5 от 17000
ru от 50 от 15000


'''
countries = ['ru', 'en', 'fr']
from_prices = ['от 1', 'от 5', 'от 20', 'от 50']
# ррезультат
data = {
    'Мобильный телефон 3000': {
        'ru': {
            'от 1': 18000,
            'от 5': 18000,
        }
    }
}

list1 = text.split('\n')
list1 = [i for i in list1 if i]

flag = 0
dic1 = {}
for line in list1:
    if line.split()[0] not in countries:
        dic1[line] = {}
        flag = line
    elif line.split()[0] in countries:
        temp = line.split()
        if temp[0] not in dic1[flag]:
            dic1[flag][temp[0]] = {}
        dic1[flag][temp[0]][f'{temp[1]} {temp[2]}'] = temp[-1]

pprint(dic1)

