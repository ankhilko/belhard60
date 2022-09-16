# Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе
# число

a = None
b = None
x = None

op = ['+', '-', '*', '/', '//', '%']

while not a:
    try:
        a = float(input('введите A: '))
    except ValueError:
        print('вводить можно только число!')

while x not in op:
    try:
        x = op[op.index(input('введите требуемую операцию: '))]
    except ValueError:
        print('вводить можно только математические операции:', *op)


while not b:
    try:
        b = float(input('введите B: '))
    except ValueError:
        print('вводить можно только число!')

op_dic = {
    '+': f'{a} + {b} = {a + b}',
    '-': f'{a} - {b} = {a - b}',
    '*': f'{a} * {b} = {a * b}',
    '/': f'{a} / {b} = {a / b}',
    '//': f'{a} // {b} = {int(a // b)}',
    '%': f'{a} % {b} = {int(a % b)}',
}
print(op_dic[x])
