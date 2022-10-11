import sqlite3

conn = sqlite3.connect('../sql.db') # db.sqlite3 two variant of file naming
cur = conn.cursor()

# DDL data definition language

cur.execute('''
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(20) NOT NULL,
    email VARCHAR(5) NOT NULL UNIQUE
);
''')
conn.commit()

cur.execute('''
CREATE TABLE IF NOT EXISTS posts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(20) NOT NULL,
    body VARCHAR(140) NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
''')

conn.commit()
# user_id INTEGER NOT NULL - неявная ссылка not unique

# DML data manipulation language

# cur.execute('''
# INSERT INTO users(name, email) VALUES(?, ?);
# ''', ('Petya', 'petr@mail.ru'))
# conn.commit()
# #
# cur.execute('''
# INSERT INTO users(name, email) VALUES('Vasya', 'vasya@nail.ru');
# ''')
# НИ КОГДА НЕ ПЕРДАВАЙТЕ ДАННЫЕ В ЗАПРОСЫ
# conn.commit()
# cur.execute('''
# UPDATE users SET name=?;
# ''', ('masha', ))
# conn.commit()

# cur.execute('''
# UPDATE users SET name=? WHERE id=?;
# ''', ('Vasya', 1))
# conn.commit()
#
# cur.execute('''
# UPDATE users SET name=? WHERE id=?;
# ''', ('Pert', 2))
# conn.commit()
# cur.execute('''
# DELETE FROM users WHERE name=?;
# ''', ('Pert', ))
# conn.commit()
# cur.execute('''
# DELETE FROM users;
# ''')
# conn.commit()
# cur.execute('''
# DELETE FROM users WHERE name in ('Pasha', 'Masha');
# ''')
# conn.commit()

# cur.execute('''
# SELECT email FROM users WHERE not name='Vasya';
# ''')
# print(cur.fetchall())
#
# cur.execute('''
# SELECT email FROM users;
# ''')
# print(cur.fetchall())
#
# cur.execute('''
# SELECT * FROM users;
# ''')
# print(cur.fetchall())
#
# cur.execute('''
# SELECT * FROM users;
# ''')
# print(cur.fetchone())
# print(cur.fetchone())
# print(cur.fetchone())
# print(cur.fetchone())
# print(cur.fetchone())

cur.execute('''
SELECT users.name, posts.title FROM users JOIN posts ON users.id = 
posts.user_id WHERE users.id != 1 AND not users.name = 'Petya';
''')
print(cur.fetchall())



