
# def f(x):
#     return x**2
 
# g = f                 #создаем переменную типа "функция", переменная хранит в себе функцию

# print(type(f))        #какой тип данных у функции, чем сама по себе является функция
# print(type(g))

# print(f(2))    #2 в квадрате = 4
# print(g(2))    #ответ такой же как в f(2)
#________________________________________________________________________________________

# def calc1(x):
#     return x + 10

# print(calc1(10))

# def calc2(x):
#     return x * 10
# print(calc2(10))

#мы можем взять функцию, которая в место аргумента будет принимать операцию и что-то выдавать

# def math(op, x):
#     print(op(x))

# math(calc2, 10)
# math(calc1, 10)
#теперь не надо каждый раз писать функцию, а можно вызывать ее

#________________________________________________________________________________________
#================LAMBDA============================

# def sum(x, y):
#     return x+y
#f = sum

#sum = lambda x, y: x + y   #фактически тоже самое, что и стр 34-36

# def mylt(x, y):
#     return x*y

# def calc(op, a, b):
#     print(op (a, b))
#     return op(a, b)
    
# #calc(sum, 4, 5)
# #мы можем сразу в код забрасывать lambda:  

# calc(lambda x, y: x + y, 5, 5)
#______________________________________________________________________________________
#============List Comprehension======================================
#чтобы быстро создавать списки

# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]

#смотри main.py
#будут перебираться все числа в диапазоне от 1 до 20, из них 
#выбираться четные, после этого  они будут возводится в третью степень

# def f(x):
#     return x**3

# list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]   #а можно подключить картежи, и будет пара, число и степень
# print(list)

#_____________________________________________________________________________________
#========================map==========================================================

# функция map() применяет указанную функцию  к каждому элементу итерируемого объекта
#и возвращает итератор с новыми объектами

# f(x) => x + 10
# map(f, [1, 2, 3, 4, 5])
# [11, 12, 13, 14, 15]

# li = [x for x in range(1, 20)]
# li = list(map(lambda x: x + 10, li))
# print(li)

#______________________________________________________

# data = list(map(int, input().split()))    #преобразует введенные данные, разделенные пробелом (split()) 
# print(data)                                #в список чисел

#______________________________________________________

# data = list(map(int, '1 2 3'.split()))    
# for e in data:
#     print(e)
    
# print('--')  

# for e in data:
#     print(e)

#_______________________________________________________

# def where (f, col):
#     return [x for x in col if f(x)]
# data = '1 2 3 5 8 15 23 38'.split()

# res = map(int, data)
# res = where(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

#_________________________________________________________________________________________
#=================================filter===================================================

#функция filter() применяет указанную функцию к каждому элементу итерируемого объекта
#и возвращает итератор с теми объектами, для которых функция вернула True

# f(x) => x - четное
# filter(f, [1, 2, 3, 4, 5])
# return => [ 2, 4]
#____________________________________________________________
# data = [x for x in range(10)]

# res = list(filter(lambda x: not x % 2, data))
# print(res)

#__________________________________________________________

# data = '1 2 3 5 8 15 23 38'.split()

# res = map(int, data)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

#________________________________________________________________________________________
#=================================zip====================================================

# функция zip() применяется к набору итерируемых объектов и возвращает 
# итератор с кортежами из элементов входных данных
#ПРобегается по минимальному набору данных
#zip ([1, 2, 3], [о, д, т,], [3, r, р])
# =>    [(1, o, 3), (2, д, r), (3, т, p)]

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 345, 32434]

# data = list(zip(users, ids, salary))
# print(data)

#__________________________________________________________________________________________
#================================enumerete==============================================

# функция elumerate() применяется к итерируемому объекту и возвращает новый итератор с кортежами
# из индекса и элементов входных данных

#enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
# =>    [(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# data = list(enumerate(users))
# print(data)