# *Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры

n = int(input('введите число n: '))
dic_c = {n: {'name': input('введите имя: '), 'email': input('введите e-mail: ')} for n in range(0, n + 1)}

print(dic_c)
