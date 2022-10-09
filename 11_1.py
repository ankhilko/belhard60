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
data = []
cur.executemany('''
INSERT INTO posts(title, body, is_published, user_id) VALUES(?, ?, ?, ?);
''', (data[1:]), )
conn.commit()



