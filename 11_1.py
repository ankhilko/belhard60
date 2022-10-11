import csv
import sqlite3
import os

os.mkdir('hw11')

conn = sqlite3.connect('hw11/hw11.sqlite3')
cur = conn.cursor()

# tables without dependencies:
cur.execute('''
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(24) NOT NULL,
    email VARCHAR(24) NOT NULL UNIQUE
);
''')
# conn.commit()
cur.execute('''
CREATE TABLE IF NOT EXISTS categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(24) NOT NULL UNIQUE
);
''')
# conn.commit()
cur.execute('''
CREATE TABLE IF NOT EXISTS statuses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(10) NOT NULL UNIQUE
);
''')
# conn.commit()

# tables with first level dependencies:
cur.execute('''
CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    status_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (status_id) REFERENCES status(id)
);
''')
# conn.commit()
cur.execute('''
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(36) NOT NULL,
    description VARCHAR(140),
    category_id INTEGER NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);
''')
# conn.commit()

# tables with second level dependencies:
cur.execute('''
CREATE TABLE IF NOT EXISTS order_items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id)
    FOREIGN KEY (product_id) REFERENCES products(id)
);
''')
conn.commit()

# adding data:

# step 1: data to csv:
users_data = [['Alex', 'alex@mail.com'], ['Max', 'mx@mail.com'], ['Nina', 'nina@mail.com']]
users_data.insert(0, ['name', 'email'])
with open('hw11/users_data.csv', 'w') as file:
    for line in users_data:
        file.write(','.join(line))
        file.write('\n')

categories_data = [f'Category {i}' for i in range(1, 4)]
categories_data.insert(0, 'category')
with open('hw11/categories_data.csv', 'w') as file:
    for line in categories_data:
        file.write(line)
        file.write('\n')

statuses_data = ['Sent', 'Confirmed', 'Paid', 'Ready', 'Delivered']
statuses_data.insert(0, 'status')
with open('hw11/statuses_data.csv', 'w') as file:
    for line in statuses_data:
        file.write(line)
        file.write('\n')

orders_data = [['2', '1'], ['3', '2'], ['3', '3'], ['1', '1'], ['2', '5']]
orders_data.insert(0, ['user_id', 'status_id'])
with open('hw11/orders_data.csv', 'w') as file:
    for line in orders_data:
        file.write(','.join(line))
        file.write('\n')

products_data = [[f'Product {i}', f'Description of product {i}', f'{i % 2 + 1}'] for i in range(1, 7)]
products_data.insert(0, ['title', 'description', 'category_id'])
with open('hw11/products_data.csv', 'w') as file:
    for line in products_data:
        file.write(','.join(line))
        file.write('\n')

order_items_data = [['1', '1'], ['1', '6'], ['2', '2'], ['3', '2'], ['3', '5'], ['3', '1'], ['4', '2'], ['4', '2'], ['5', '1']]
order_items_data.insert(0, ['order_id', 'product_id'])
with open('hw11/order_items_data.csv', 'w') as file:
    for line in order_items_data:
        file.write(','.join(line))
        file.write('\n')

# step 2: csv to database:
with open('hw11/users_data.csv', 'r') as file:
    datalist = list(csv.reader(file))
    cur.executemany('''
    INSERT INTO users(name, email) VALUES(?, ?);
    ''', datalist[1:], )

with open('hw11/categories_data.csv', 'r') as file:
    datalist = list(csv.reader(file))
    for n in datalist[1:]:
        cur.execute('''
        INSERT INTO categories(name) VALUES(?);
        ''', n, )

with open('hw11/statuses_data.csv', 'r') as file:
    datalist = list(csv.reader(file))
    for n in datalist[1:]:
        cur.execute('''
        INSERT INTO statuses(name) VALUES(?);
        ''', n, )

with open('hw11/orders_data.csv', 'r') as file:
    datalist = list(csv.reader(file))
    cur.executemany('''
    INSERT INTO orders(user_id, status_id) VALUES(?, ?);
    ''', datalist[1:], )

with open('hw11/products_data.csv', 'r') as file:
    datalist = list(csv.reader(file))
    cur.executemany('''
    INSERT INTO products(title, description, category_id) VALUES(?, ?, ?);
    ''', datalist[1:], )

with open('hw11/order_items_data.csv', 'r') as file:
    datalist = list(csv.reader(file))
    cur.executemany('''
    INSERT INTO order_items(order_id, product_id) VALUES(?, ?);
    ''', datalist[1:], )

# # send the data to the database
conn.commit()


cur.execute('''
SELECT products.title FROM products JOIN categories ON categories.id = 
products.category_id WHERE categories.name = 'Category 2';

''')
print(cur.fetchall())
