# 5. Вводится строка, избавиться от букв в верхнем регистре

text = input('введите строку: ')
print(''.join(i for i in text if not i.istitle()))
