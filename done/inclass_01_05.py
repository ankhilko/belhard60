# строка из 3+ слов - поменять первое и последнее местами

# in_string = input("Введите строку: ").strip()
#
# list_string = in_string.split()
# list_string[0], list_string[-1] = list_string[-1], list_string[0]
# in_str_new = " ".join(list_string)
# print(in_str_new)
#
# space_first = in_string.find(" ")
# space_last = in_string.rfind(" ")
#
# new_string = in_string[space_last + 1:] + in_string[space_first:space_last + 1] + in_string[:space_first]
#
# print(new_string)

# вводится 3-х значное числоб найти сумму цифр

# number = input()
# print(int(number[0]) + int(number[1]) + int(number[2]))


# отец = ХХ
# сын = УУ
#
# через скололь лет был, есть, будет отец 2Х

# father = int(input("father age: "))
# son = int(input("son age: "))
# print(father - 2 * son)

# слово начинается на гласную

# word = input().lower()
# print(word[0] in "euioay" or word[0] in "уёеыаоэяию")

# вводится слово - полиндром

# word = input("Input line: ").strip().lower().replace(" ", "")
# print("Is polymdrom =", word == word[::-1])

#
# lst = [1 ,1, 2, 3, 4]
#
# lst.append('asdasd')
# lst.extend(45)
#
# print(lst)

# print(sum(i for i in range(1, int(input()) + 1)))
# print(sum(range(1, int(input()) + 1)))

# уникалье символы
# text = input()
#
# for i in range(len(text)):
#     if text[i] in text[:i] or text[i] in text[i + 1:]:
#         continue
#     print(text[i])
#
# for i in text:
#     if text.count(i) == 1:
#         print(i)
#
# print([i for i in text if text.count(i) == 1])


# text1 = 'рига'
# text2 = 'игра'
#
# print(list(text1.lower()).sort() == list(text2.lower()).sort())

# while not input().isdigit('enter number: '):
#     print('not number')
#     pass
#
# while not (number := input().isdigit('enter number: ')):
#     print('not number')
#     pass

# text = input()
# n = 0
# pair = False
# for i in range(1, len(text)):
#     if text[i-1] == text[i] and not pair:
#         n += 1
#         pair = True
#     elif pair:
#         pair = False
#
# print(f'{n} пара')
#
#
# count = 1
# pair = 0
# while count < len(text):
#     if text[count - 1] == text[count]:
#         pair += 1
#         count += 2
#     else:
#         count += 1
#
# print(f'{pair} пара')


x = float(input('в день км: ')) # в день + 10%
y = float(input('сколько ищем: ')) # пробежал км
z = 1 # сколько дней

while x < y:
    z += 1
    x *= 1.1

print(f'на {z} день')

