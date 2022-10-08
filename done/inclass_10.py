
from itertools import cycle, repeat, zip_longest


numbers = [1, 2, 3, 4, 5, 6, 7]
# for i in cycle(numbers):
#     print(i)

result = [[1, 2], [3, 4], [5, 6], [7]]

numbers = iter(numbers)
result2 = list(zip_longest(numbers, numbers, numbers))
print(result2)
# result3 = list(zip_longest(numbers * 2))



from datetime import datetime, timedelta

delt = timedelta(
    days=177
)

dat = datetime(
    year=2000,
    month=3,
    day=13
)

print(dat)
print(dat + delt)




print(datetime.now())
print(datetime.utcnow())
print(datetime.now().timestamp()) # milliseconds
print(datetime.utcnow().timestamp()) # from 01.01.1970
print(datetime.fromtimestamp(45678909876.6688))

print(datetime.now().strftime('%a %A'))

print(datetime.strptime('01.02.2000 13:48', '%d.%m.%Y %H:%M'))



