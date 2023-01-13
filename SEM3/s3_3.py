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

# a = int(input())
# b = int(input())
# for i in range(a, b+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else :
#         print(i)




# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# num = int(input())
# i = 2
# list_num = []
# while i * i <= num:
#     while num % i == 0:
#         num = num / i
#         list_num.append(i)
#     i = i + 1
# if num > 1:
#     list_num.append(num)
# print(list_num)

# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
#
# out
# 9.000000
from decimal import *
#import decimal
n = float(input('ВВедите число: '))
#a = input('a: ')
#d = len ( str(a).split('.')[1] )
#print(d)

#decimal.getcontext().prec = 3
getcontext().prec = 3
res = Decimal(n)
#k = decimal(n)
print(res)
# Decimal(1) / Decimal(7)




# # # number = float(input())
#
# # # num =
# #
# number = Decimal(A)
# number = 3 * number
# print(number)       # 0.30


#____________________________________________________
# num_list = [23, 56, 89, 23, 57, 89, 56, 99]
#
# num_dict = {}
# for i in num_list:
#     num_dict[i] = num_dict.get(i, 0) + 1
#
# new_list = [key for key, value in num_dict.items() if value == 1]
# print(f'Список неповторяющихся элементов: {new_list}')

 # при d = 0.001,π = 3.141    10^(-1)≤d≤10^(-10).

#
# from math import pi
# a = float(input())
# #d = int(input("Введите число для заданной точности числа Пи:\n"))
# d = len ( str(a).split('.')[1] )
# print(f'число Пи с заданной точностью {d} равно {round(a, d)}')

#__________________________________________________________