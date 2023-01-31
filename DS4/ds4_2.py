# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input())
i = 2
list_num = []
while i * i <= num:
    while num % i == 0:
        num = num / i
        list_num.append(i)
    i = i + 1
if num > 1:
    list_num.append(num)
print(list_num)