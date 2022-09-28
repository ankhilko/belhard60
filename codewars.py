# def is_pangram(s):
#     for i in list(chr(j) for j in range(ord('a'), ord('z') + 1)):
#         if i in s.lower():
#             continue
#         else:
#             return False
#     else:
#         return True

# def high_and_low(numbers):
#     temp = list(set(numbers.split()))
#     for i in range(len(temp)):
#         temp[i] = int(temp[i])
#     numbers = ' '.join([str(max(temp)), str(min(temp))])
#     return numbers
#
# print(high_and_low('4 4 -3 5 6 7 9 0'))


# def sort_array(source_array):
#     # Return a sorted array.
#     for i in range(0, len(source_array) - 1):
#         if source_array[i] % 2:
#             for j in range(i + 1, len(source_array)):
#                 if source_array[j] % 2:
#                     if source_array[i] > source_array[j]:
#                         source_array[i], source_array[j] = source_array[j], source_array[i]
#     return source_array
#
# sort_array([1,2,3,4,5,6,7,8,9,10])


# def duplicate_encode(word):
#     #your code here
#     return ''.join(')' if word.count(i) > 1 else '(' for i in word)
# print(duplicate_encode('sdfghfghjfeogri'))


# import re
#
# url = input('input twitter username: ').strip()
# # https://www.twitter.com/sanr
# # http://www.twitter.com/sanr
# # https://twitter.com/sanr
# # http://twitter.com/sanr
# # www.twitter.com/sanr
# # twitter.com/sanr
# # sanr
# username = re.sub(r"^(https?://)?(www\.)?twitter\.con/", "", url)
#
# print(f'twitter user name = {username}')


import re

url = input()

username: str

if match := re.search(r'^(?:https?://)?(?:www\.)?twitter.com/([a-z0-9_]+)/?$', url, re.IGNORECASE):
# if match := re.search(r'^(?:https?://)?(?:www\.)?twitter.com/([a-z0-9_]+)', url, re.IGNORECASE):
    username = match.group(1)

print(username)


