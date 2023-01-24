# 1. Создайте список из N натуральных чисел(0 до N),
# упорядоченных по возрастанию. Среди чисел не хватает
# одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найдите это число.

with open(r"D:\GeekBrains\Python\SEM5\New_file.txt", 'w') as f:
    f.write('1 2 3 \n4 5 6 8 \n')


#вывод файла    
path = r'D:\GeekBrains\Python\SEM5\New_file.txt'
data = open(path, 'r')
num_row = []
for line in data:
    print(line)
    num_row += list(map(int, line.split()))
data.close()
print(num_row)


for i, elem in enumerate(num_row[:-1]):
    if elem +1 != num_row[i + 1]:
        print(elem + 1)