#3 напишите программу, которая определит позицию 
# второго вхождения строки в списке, либо сообщит,. что ее нет

# def find_index_coin(new_list, text, num = 2):
#     count = 0
#     result = -1
#     for i in range(len(new_list)):
#         if text == my_list[i]:
#             count += 1
#         if count == num:
#             result = i
#     return result
#
# my_list = ['wef', 'dfd', 'sfer', 'dfd',  'efff', 'dfd', 'eeee']
# print(find_index_coin(my_list, 'dfd'))

a = int(input())

if a == 0:
    print('зеленый')
elif 1 <= a <= 10:
    if a % 2 == 0:
        print('черный')
    if a % 2 != 0:
        print('красный')
elif 11 <= a <= 18:
    if a % 2 == 0:
        print('черный')
    if a % 2 != 0:
        print('красный')
elif 19 <= a <= 28:
    if a % 2 == 0:
        print('черный')
    if a % 2 != 0:
        print('красный')
elif 29 <= a <= 36:
    if a % 2 == 0:
        print('черный')
    if a % 2 != 0:
        print('красный')
else:
    print('ошибка ввода')