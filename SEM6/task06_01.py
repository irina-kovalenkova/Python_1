#1. Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,* приоритет операций стандартный.
#* Добавьте скобки, приоритет операций меняется.

actions = {
"^": lambda x, y: str(float(x) ** float(y)),
"*": lambda x, y: str(float(x) * float(y)),
"/": lambda x, y: str(float(x) / float(y)),
"+": lambda x, y: str(float(x) + float(y)),
"-": lambda x, y: str(float(x) - float(y))
}

def cut(ls):
    lst =[]
    index_ = 0
    
    while index_ < len(ls):
        if ls[index_] == "(":
            end = ls.index(")")
            lst.append(ls[index_ + 1:end])
            index_ = end
        else:
            lst.append(ls[])
            
    
    
user_ls = input('...').split()