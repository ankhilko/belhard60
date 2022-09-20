# 5) 2. Дан список строк, наобходимо реализовать пагинатор:
# Если пользователь вводит ">" то выводится следующий  элемент из списка,
# если вводит пользователь "<" то предыдущий по этому списку,
# а так же предусмотреть, что
# если пользователь сейчас находится на последнем элементе,
# то следующий это первый, а если находится на первом элементе,
# то предыдущий это последний, чтобы пользователь
# мог прокручивать список по кругу в любом направлении

# возьмем список строк
list_of_lines = 'если пользователь сейчас находится на последнем элементе'.split()

directions = ('>', '<')
direction_sign = None

current_position = 0

while direction_sign != 'exit':

    while direction_sign not in directions:
        direction_sign = input('please input \'>\' or \'<\': ')

    if direction_sign == '>':
        if current_position < len(list_of_lines) - 1:
            current_position += 1
        else:
            current_position = 0
    if direction_sign == '<':
        if current_position > 0:
            current_position -= 1
        else:
            current_position = len(list_of_lines) - 1

    print(list_of_lines[current_position])
    direction_sign = input('please input \'>\' or \'<\': ')
