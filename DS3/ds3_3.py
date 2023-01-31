# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011

# user_n = int(input('Введите число: '))
# n = user_n
# num_list = []
# while n > 0:
#     num = n % 2
#     num_list.append(str(num))
#     n = n // 2
# num_list.reverse()
# num = int(''.join(num_list))
# print('Число в двоичной системе = ', num)

#_______________________________________________________________________

# решение учителя

def conv_bin(num:int):
    list_nums = []
    
    while num > 0:
        list_nums.insert(0, num % 2)
        num //= 2
        
    print(*list_nums, sep = '')
conv_bin(int(input()))        
        
