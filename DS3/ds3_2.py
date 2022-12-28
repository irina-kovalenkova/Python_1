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
# len_list = (int(input('Введите длину списка: ')))

# new_list = sample(range(1,len_list+1), k=len_list)
# print('Созданный массив: ', new_list)

# comp_list = []
# for i in range((len(new_list) // 2 + len(new_list) % 2)):
#     new_num = new_list[i] * new_list[-i-1]
#     comp_list.append(new_num)
# print('Произведения: ',comp_list)

#____________________________________________________________________________

#решение учителя

def list_rand_nums(count):
    if count < 0:
        print("Negative value of the number of numbers!")
        return []
    
    list_nums = sample(range(1, count * 2), count)
    return list_nums

def prod_pairs(list_nums: list):
    res_list = []
    len_list = len(list_nums)
    
    for k in range(len_list//2):
        res_list.append(list_nums[k] * list_nums[len_list - k -1])
        
    if len_list % 2:
        res_list.append(list_nums[len_list // 2])
    return res_list
    
all_list = list_rand_nums(int(input('Number of numbers: ')))
print(all_list)
print(prod_pairs(all_list))        