text = '''
Мобильный телефон 3000

ru от 1 от 18000

ru от 5 от 17000
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
    if flag == 0:
        dic1[line] = {}
        flag = 1
    elif line[:2] in countries:
        pass



