from logg import logging
import mod_calc

def select_type_num():
    while True:
        type_num = input("\n"
                         "== Select type of number ==\n"
                         "___________________________\n"
                         "\n"
                         "   1 - rational numbers    \n"
                         "   2 - complex numbers     \n"
                         "   3 - EXIT                \n"
                         "___________________________\n"
                         "Your number:  ")
        if type_num == '0':
            logging.info("Stop programm")
            exit()
        elif type_num == '1':
            operation_for_rational_numbers()
        elif type_num == '2':
            operation_for_complex_numbers()
        elif type_num not in ['1', '2', '0']:
            logging.error("Error")
            print("Error. Incorrect input.")
            continue
        else:
            break
        
def operation_for_rational_numbers():
    while True:
        type_op = input("\n"
                        "== Select type of operation ==\n"
                        "______________________________\n"
                        "1  - sum                       \n"
                        "2  - subtraction               \n"
                        "3  - multiplication            \n"
                        "4  - division                  \n"
                        "5  - exponentiation            \n"
                        "6  - root of number            \n"
                        "0  - previous menu             \n"
                        "00 - EXIT                      \n"
                        "______________________________\n"
                        "Select operation:  ")
        if type_op not in ['1', '2', '3', '4', '5', '6', '7', '8', '0', '00']:
            logging.error("Error")
            print("Error. Incorrect input.")
            continue
        elif type_op == '00':
            logging.info("Stop program")
            exit()
        elif type_op == '0':
            logging.info('go to previous menu')
            break
        else:
            n1, n2 = rational_num(type_op)
            mod_calc.actions(type_op, n1, n2)
            logging.info('finish program')
            exit()


def rational_num(oper):
    while True:
        try:
            num_1 = float(input("Enter 1 number: ").replace(',', '.'))
            num_2 = float(input("Enter 2 number: ").replace(',', '.'))
            return num_1, num_2
        except:
            logging.error("Error")
            print("Error. Incorrect input.")
            return
        

def complex_num(oper):
    while True:
        if oper == '60' or oper == '5':
            try:
                num_1 = int(input("Enter 1 real part: "))
                num_2 = int(input("Enter 1 imaginary number: "))
                num_3 = float(input("Enter 2 number: ").replace(',', '.'))
                num_C_1 = complex(num_1, num_2)
                return num_C_1, num_3
            except:
                logging.error("Error")
                print("Error. Incorrect input.")
                return
        else:
            try:
                num_1 = int(input("Enter 1 real part: "))
                num_2 = int(input("Enter 1 imaginary number: "))
                num_3 = int(input("Enter 2 real part: "))
                num_4 = int(input("Enter 2 imaginary number: "))
                num_C_1 = complex(num_1, num_2)
                num_C_2 = complex(num_3, num_4)
                return num_C_1, num_C_2
            except:
                logging.error("Error")
                print("Error. Incorrect input.")
                return
            
            
def operation_for_complex_numbers():
    while True:
        type_op = input("\n"
                        "== Select type of operation ==\n"
                        "______________________________\n"
                        "1  - sum                       \n"
                        "2  - subtraction               \n"
                        "3  - multiplication            \n"
                        "4  - division                  \n"
                        "5  - exponentiation            \n"
                        "0  - previous menu             \n"
                        "00 - EXIT                      \n"
                        "______________________________\n"
                        "Select operation:  ")
        
        if type_op not in ['1', '2', '3', '4', '5', '0', '00']:
            logging.error("Error")
            print("Error. Incorrect input.")
            continue
        elif type_op == '00':
            logging.info("Stop program")
            exit()
        elif type_op == '0':
            logging.info('go to previous menu')
            break
        else:
            if type_op == '6': type_op = '60'
            n1, n2 = complex_num(type_op)
            mod_calc.actions(type_op, n1, n2)
            logging.info('finish program')
            exit()

def rational_num(oper):
    while True:
        try:
            num_1 = float(input("Enter 1 number: ").replace(',', '.'))
            num_2 = float(input("Enter 2 number: ").replace(',', '.'))
            return num_1, num_2
        except:
            logging.error("Error")
            print("Error. Incorrect input.")
            return

def complex_num(oper):
    while True:
        if oper == '60' or oper == '5':
            try:
                num_1 = int(input("Enter 1 real part: "))
                num_2 = int(input("Enter 1 imaginary number: "))
                num_3 = float(input("Enter 2 number: ").replace(',', '.'))
                num_C_1 = complex(num_1, num_2)
                return num_C_1, num_3
            except:
                logging.error("Error")
                print("Error. Incorrect input.")
                return
        else:
            try:
                num_1 = int(input("Enter 1 real part: "))
                num_2 = int(input("Enter 1 imaginary number: "))
                num_3 = int(input("Enter 2 real part: "))
                num_4 = int(input("Enter 2 imaginary number: "))
                num_C_1 = complex(num_1, num_2)
                num_C_2 = complex(num_3, num_4)
                return num_C_1, num_C_2
            except:
                logging.error("Error")
                print("Error. Incorrect input.")
                return