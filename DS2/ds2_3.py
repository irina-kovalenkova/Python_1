# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите
# на экран их сумму.
# in
# 6

# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071
num_list = []
n = int (input ('Введите длину списка '))
for k in range (1, n+1):
    num_list.append ((1 + 1 / k) ** k)
my_formatted_list = [ '%.3f' % elem for elem in num_list ]
print (my_formatted_list)
print (round((sum(num_list)) , 3))
