# def sum(x, y):
#     return x + y
# f = sum
sum = lambda x, y: x + y +1

def mylt(x, y):
    return x*y

def calc(op, a, b):
    print(op(a, b))
    
calc(lambda x, y: x + y +1, 4, 5)