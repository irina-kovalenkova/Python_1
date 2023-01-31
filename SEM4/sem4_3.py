# 3. На вход программе подается число n.
# Программа печатает численный треугольник.
# Используем вложенные циклы.

num = int(input())
for i in range(1, num + 1):
    for k in range(i):
        print(i, end='')
    print()