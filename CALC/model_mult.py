x = 0 
y = 0

def init(a, b):
    global x              # связывает x и a
    global y
    x = a
    y = b
    
def do_it():
    return x * y
