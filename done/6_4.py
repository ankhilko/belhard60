# 4. Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно

lst = ['asfasfasf', 6748247, [1, 3], {1, 3, 7}, 'asdas', (3, 4), '789']

print(list(filter(lambda x: isinstance(x, str), lst)))
