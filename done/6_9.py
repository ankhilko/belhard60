# 9. Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)

users = {
    1: {'name': 'Alex', 'surname': 'Murfy', 'phone': '+12345678', 'email': 'amur@gnom.com', },
    2: {'name': 'Nina', 'surname': 'Mina', 'phone': '+19876278', 'email': '', },
    3: {'name': 'Kate', 'surname': 'Kitty', 'phone': '', 'email': 'kiki@gnom.com', },
    4: {'name': 'Greg', 'surname': 'Gregor', 'phone': '+15567756', },
    5: {'name': 'Freak', 'surname': 'Nuts', 'phone': '', 'email': 'freenut@gnom.com', },
}

for key, value in users.items():
    if not value.get('email'):
        print(value['name'])
