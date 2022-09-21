# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами

text = input()
text_1 = text.replace(' ', '-')
text_2 = '-'.join(text.split())
print(text_1)
print(text_2)
