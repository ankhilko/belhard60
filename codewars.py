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


