# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры


text = input('введите текст: \n').lower()
dic_ch = {}

for char in text:
    if char.isalpha():
        if char not in dic_ch:
            dic_ch[char] = 1
        else:
            dic_ch[char] += 1

print(dic_ch)
