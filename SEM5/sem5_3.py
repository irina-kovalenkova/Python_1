# 'Напишите  программу, удаляющую из этого текста все вабвс слова, 
# содержащие "абв"'
     


# my_text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
#     этого абв текста все вабвс слова, содерабващие содержащие "абв"'

# def del_some_words(my_text):
#     my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
#     return " ".join(my_text)

# my_text = del_some_words(my_text)
# print(my_text)

#=========================================================================
#Второй вариант

my_str = 'абв пкелп абв авс'

new_str = list(filter(lambda elem: 'абв' not in elem, my_str.lower().split()))
print(*new_str)