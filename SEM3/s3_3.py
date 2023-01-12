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
# print(find_index_coin(my_list, 'dfd')>




# Если перечислить все натуральные числа ниже 10, которые кратны 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел 23.
#
# Напишите программу, которая принимает натуральное число n и находит сумму всех чисел ниже переданного числа n, которые делятся на 3 или на 5.


a = int(input())
fact = 1
for i in range(1, a + 1):
    fact = fact * i
print(fact)
