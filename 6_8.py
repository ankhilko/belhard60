# 8. Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны

from cc_6_6 import cc_dic

city = input('введите город: ')

for key, value in cc_dic.items():
    if city in value:
        print(f'{city} находится в {key}.')
#        found = True
        break
else:
    print(f'{city} в нашем мире не найден.')
print('спасибо, что воспользовались нашим сервисом!')
