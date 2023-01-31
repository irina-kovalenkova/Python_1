# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

num = input()
sum = 0
m = len(num) - 2
num = float(num)
num *= (10 ** m)

print(int(num))

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10
print(sum)

