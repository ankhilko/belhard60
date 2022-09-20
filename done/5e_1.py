# 1. Вводится строка, вывести из строки только цифры

text = input('введите строку: ')
text_modified = ''.join(i for i in text if i.isdigit())
print('только цифры:', text_modified)
