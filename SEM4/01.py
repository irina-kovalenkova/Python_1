import my_module


list_num = input('Введите числа через пробел ->').split()

print(my_module.find_min_max(list_num))
print(*my_module.find_min_max(list_num)) #если ставим *, то в ответе убирает скобки, "распаковывает"
