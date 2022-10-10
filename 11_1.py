import sqlite3

conn = sqlite3.connect('hw11.sqlite3')
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
    FOREIGN KEY (user_id) REFERENCES users(id), 
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
data = [['Alex', 'alex@mail.com'], ['Max', 'mx@mail.com'], ['Nina', 'nina@mail.com']]
cur.executemany('''
INSERT INTO users(name, email) VALUES(?, ?);
''', data, )

data = (f'Category {i}' for i in range(1, 4))
for n in data:
    cur.execute('''
    INSERT INTO categories(name) VALUES(?);
    ''', (n, ))

data = ['Sent', 'Confirmed', 'Paid', 'Ready', 'Delivered']
for n in data:
    cur.execute('''
    INSERT INTO statuses(name) VALUES(?);
    ''', (n, ))

data = [['2', '1'], ['3', '2'], ['3', '3'], ['1', '1'], ['2', '5']]
cur.executemany('''
INSERT INTO orders(user_id, status_id) VALUES(?, ?);
''', data, )

data = [[f'Product {i}', f'Description of product {i}', f'{i % 2 + 1}'] for i in range(1, 7)]
cur.executemany('''
INSERT INTO products(title, description, category_id) VALUES(?, ?, ?);
''', data, )


data = [['1', '1'], ['1', '6'], ['2', '2'], ['3', '2'], ['3', '5'], ['3', '1'], ['4', '2'], ['4', '2'], ['5', '1']]
cur.executemany('''
INSERT INTO order_items(order_id, product_id) VALUES(?, ?);
''', data, )
