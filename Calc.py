from decimal import *
import math
OPERATORS = ('+', '-', '*', '/', '^', '(', ')', '.', 'l', 'o', 'g', 'e', 'x', 'p')
DIGITS = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
stack = []


def is_valid(lst):
    for i in lst:
        if i not in OPERATORS and i not in DIGITS:
            return False
    return True


def calc(lst):
    bracket(lst, 0)
    while stack.__len__()>1 or stack.__len__()==0:

        new_list = stack.copy()
        stack.clear()
        bracket(new_list, 0)
    return stack[0]


def classify(lst):
    number_list=[]
    operator_list = []
    number = ''
    for i in lst:
        if not is_operator(i) or i == '.':
            number = number + i
        else:
            number_list.append(number)
            operator_list.append(i)
            number = ''
    number_list.append(number)
    return number_list, operator_list


def operation(number_list, operator_list):
    try:
        log_exp(number_list, operator_list)
        power(number_list, operator_list)
        mul_div(number_list, operator_list)
        add_sub(number_list, operator_list)
    except ZeroDivisionError:
        print("Zero can't be divided")
        quit()
    except InvalidOperation:
        print("Invalid input")
        quit()
    return number_list, operator_list


def bracket(lst, count):
    if '(' not in lst:
        number_list = classify(lst)[0]
        operator_list = classify(lst)[1]
        if stack:
            stack.pop()
        stack.append(str(operation(number_list, operator_list)[0][0]))
        if '(' in stack:
            stack.append(')')
        return
    else:
        i = 0
        while i < lst.__len__():
            stack.append(lst[i])
            if str(lst[i]) == '(':
                count = count + 1
                nlst = []
                i += 1
                while  count != 0:
                    if str(lst[i]) == '(':
                        count+=1
                    if str(lst[i]) == ')':
                        count-=1
                    if count == 0:
                        break
                    nlst.append(lst[i])
                    i +=1
                bracket(nlst,count)
            i +=1


def log_exp(number_list, operator_list):
    i = 0
    while i < operator_list.__len__():
        if operator_list[i] == 'l':
            if operator_list[i+1] == 'o':
                if operator_list[i+2] == 'g':
                    operator_list.pop(i)
                    operator_list.pop(i)
                    operator_list.pop(i)
                    number_list.pop(i)
                    number_list.pop(i)
                    number_list.pop(i)
                    number_list[i] = Decimal(str(math.log(float(number_list[i]))))
                else:
                    print('error')
                    break
            else:
                print('error')
                break
            i -= 1
        elif operator_list[i] == 'e':
            if operator_list[i+1] == 'x':
                if operator_list[i+2] == 'p':
                    operator_list.pop(i)
                    operator_list.pop(i)
                    operator_list.pop(i)
                    number_list.pop(i)
                    number_list.pop(i)
                    number_list.pop(i)
                    number_list[i] = Decimal(str(math.exp(float(number_list[i]))))
                else:
                    print('error')
                    break
            else:
                print('error')
                break
            i -= 1
        i += 1


def power(number_list, operator_list):
    i = 0
    while i < operator_list.__len__():
        if operator_list[i] == '^':
            result = Decimal(number_list[i]) ** Decimal(number_list[i + 1])
            operator_list.pop(i)
            number_list.pop(i)
            number_list.pop(i)
            number_list.insert(i, result)
            i -= 1
        i += 1


def mul_div(number_list, operator_list):
    i = 0
    while i < operator_list.__len__():
        if operator_list[i] == '*':
            result = Decimal(number_list[i]) * Decimal(number_list[i + 1])
            operator_list.pop(i)
            number_list.pop(i)
            number_list.pop(i)
            number_list.insert(i, result)
            i -= 1
        elif operator_list[i] == '/':
            result = Decimal(number_list[i]) / Decimal(number_list[i + 1])
            operator_list.pop(i)
            number_list.pop(i)
            number_list.pop(i)
            number_list.insert(i, result)
            i -= 1
        i += 1


def add_sub(number_list, operator_list):
    for i in range(1, number_list.__len__()):
        number1 = number_list[0]
        number2 = number_list[1]
        if operator_list[0] == '+':
            result = Decimal(number1) + Decimal(number2)
        elif operator_list[0] == '-':
            result = Decimal(number1) - Decimal(number2)
        operator_list.pop(0)
        number_list.pop(1)
        number_list[0] = result


def is_operator(op):
    return op in OPERATORS


while True:
    sequence = input("Please enter a sequence that you want to compute: (q to end)")
    se_lst = list(sequence)
    if sequence == 'q':
        break
    elif is_valid(se_lst):
        result = calc(se_lst)
        stack.clear()
        print("The result for", sequence, "is", "%.3f" % float(result))
        again = input("Would you like to have another try? y/n")
        if again == 'y':
            continue
        elif again == 'n':
            break
    else:
        print("Error:The sequence must only include operators and digits")
