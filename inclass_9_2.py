import pandas


frame = pandas.DataFrame(
    {
        'name': ['Petya', 'Vasya'],
        'age': [43, 32]
    }
)

print(frame[frame['age'] > 40])

print(frame)

frame.to_excel('sheet.xlsx', sheet_name='users')


# frame1 = pandas.read_excel('name.xlsx')









