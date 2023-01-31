#  Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10

# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]


from random import sample

def big_nums(num):
    list_nums = sample(range(1, num * 2), num)
    print(list_nums)
    return [list_nums[num] for num in range(1, len(list_nums)) if list_nums[num] > list_nums[num - 1]]   
print(big_nums(int(input())))    
    