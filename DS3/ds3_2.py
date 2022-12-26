# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5

# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]


from random import sample
len_list = (int(input('Введите длину списка: ')))

new_list = sample(range(1,len_list+1), k=len_list)
print('Созданный массив: ', new_list)

comp_list = []
for i in range((len(new_list) // 2 + len(new_list) % 2)):
    new_num = new_list[i] * new_list[-i-1]
    comp_list.append(new_num)
print('Произведения: ',comp_list)
