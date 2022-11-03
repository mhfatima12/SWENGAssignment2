from typing import List

OPERATORS = ('+', '-', '*')
DIGITS = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')


def is_valid(lst):
    for i in lst:
        if i not in OPERATORS and i not in DIGITS:
            return False
    return True


def calc(lst):
    number_list = []
    operator_list = []
    number = ''
    for i in lst:
        if is_digit(i):
            number = number + i
        else:
            number_list.append(int(number))
            operator_list.append(i)
            number = ''
    number_list.append(int(number))
    operator_list, number_list = mul(operator_lst=operator_list, number_lst=number_list)
    operator_list, number_list = add_sub(operator_lst=operator_list, number_lst=number_list)
    return number_list[0]


def mul(operator_lst: List, number_lst: List):
    i = 0
    while i < operator_lst.__len__():
        if operator_lst[i] == '*':
            product = number_lst[i] * number_lst[i + 1]
            operator_lst.pop(i)
            number_lst.pop(i)
            number_lst.pop(i)
            number_lst.insert(i, product)
            i -= 1
        i += 1
    return operator_lst, number_lst


def add_sub(operator_lst: List, number_lst: List):
    for i in range(1, number_lst.__len__()):
        number1 = number_lst[0]
        number2 = number_lst[1]
        if operator_lst[0] == '+':
            result = number1 + number2
        elif operator_lst[0] == '-':
            result = number1 - number2
        operator_lst.pop(0)
        number_lst.pop(1)
        number_lst[0] = result
    return operator_lst, number_lst


def is_digit(digit):
    return digit in DIGITS


def calculate(sequence):
    se_lst = list(sequence)
    if is_valid(se_lst):
        try:
            result = calc(se_lst)
        except BaseException as e:
            return e
        else:
            return result
    else:
        return "Error: The sequence must only include operators and digits"


# while True:
#     sequence = input("Please enter a sequence that you want to compute: (q to end)")
#     if sequence == 'q':
#         break
#     else:
#         calculate(sequence)
