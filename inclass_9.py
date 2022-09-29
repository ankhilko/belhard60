#
# with open("README.md", 'r') as file:
#     # print(*file.readlines())
#     for line in file:
#         print(line)
#
#     file.seek(0)
#
# import json
#
# with open("ds.json", 'r', encoding='utf-8') as file:
#     data = json.load(file)
#     json.dump(data, file, indent=2, ensure_ascii=False)
#     # json.dump(data, file, indent=2, ensure_ascii=False, separators=[':', ','])
#
#
# # если у нас строкой    text = '{"name": "Mina"}'
#     data = json.loads(file)
#     data2 = json.dump(data, indent=2, ensure_ascii=False)
#


# from pydantic import BaseModel, Field, EmailStr, validator, root_validator
#
#
# class Data(BaseModel):
#     a: int
#     b: int
#
#
# dates = ['email@nun.com', 'gin@mail.ru']
#
# class User(BaseModel):
#     name: str = Field(min_length=4, max_length=10)
#     age: int = 0
# #    languages: list = Field(unique_items=True)
# #    data: Data
#     email: EmailStr
#     text: str
#
#     @validator('email', pre=True) # не надо вызывать - сам делается перед стартом
#     def val_em(cls, value):
#         if value in dates:
#             raise ValueError('email is not unique')
#         return value
#
#
#     @root_validator(pre=True) # не надо вызывать - сам делается перед стартом
#     def val_name_in_em(cls, values):
#         if values['name'].lower() not in values['email'].lower():
#             raise ValueError('name not in email')
#         values['text'] = values['name'] + values['email']
#         return values
#
#
#
# vasya = User(name='Petya', age=45, email="petyahren@mail.ru")
#
# print(vasya)
# print(vasya.dict())



import csv

with open('nina.csv', 'r', encoding='utf-8') as file:
    data = csv.reader(file, delimiter=',')
    for user in data:
        print(user)

with open('nina.csv', 'r', encoding='utf-8') as file:
    data = csv.DictReader(file, delimiter=',')
    for user in data:
        print(user)


dicts2 = {
    {'1': 'dfghjk', '2': 'awdawawf', '3': 'awfawfawf'},
    {'1': 'dfk', '2': 'awdawawf', '3': 'awfawf'},
    {'1': 'dk', '2': 'awdf', '3': 'fawf'},
    {'1': 'jk', '2': 'af', '3': 'f'},
    {'1': 'ghjk', '2': 'aawawf', '3': 'ff'}
}

with open('nina2.csv', 'x', encoding='utf-8') as file:
    fields = ['a', 'b', 'c']
    writer = csv.DictWriter(file, fieldnames=fields, delimiter=',')
    for user in data:
        print(user)



