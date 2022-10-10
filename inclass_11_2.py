import sqlite3

with open('table.csv', 'r') as file:

    data = file.readlines()
    data2 = []

    for line in data:
        data2.append(line.strip().split('~'))

conn = sqlite3.connect('sql.db') # db.sqlite3 two variant of file naming
cur = conn.cursor()

# for line in data2[1:]:
#     cur.execute('''
#     INSERT INTO posts(title, body, is_published, user_id) VALUES(?, ?, ?, ?);
#     ''', (line[0], line[1], line[2], line[3],))
# conn.commit()

# data3 = map() привести к кортежу кортежей

cur.executemany('''
INSERT INTO posts(title, body, is_published, user_id) VALUES(?, ?, ?, ?);
''', (data2[1:]), )
conn.commit()

cur.execute('''
SELECT title, body, is_published, user_id FROM posts ORDER BY title DESC;
''')

list1 = cur.fetchall()

with open('newbd.csv', 'w') as file:
    for line in list1:
        line = list(line)
        for i in range(len(line)):
            line[i] = str(line[i])
        file.write('~'.join(line))
        file.write('\n')
