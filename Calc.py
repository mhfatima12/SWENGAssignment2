from decimal import *
import math
import sys
from typing import List

OPERATORS = ('+', '-', '*', '/', '^', '(', ')', '.', 'l', 'o', 'g', 'e', 'x', 'p', 'L', 'O', 'G', 'E', 'X', 'P')
DIGITS = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
WELCOME = "Please enter a sequence that you want to compute: (q to quit)"
INVALID_INPUT = "Invalid input: please type like log3+-5*exp(4.2)/(5+7) or log(3)+(-5)*exp(4.2)/(5+7)"
ERROR_INPUT = "Error: The sequence must only include operators and digits"
ZERO_DIVISION = "Error: division by zero"
MATHEMATICAL_ERROR = "Mathematical Error: the domain of log must be positive"
stack = []


# check if input is valid
def is_valid(lst):
    last_item = ''
    for i in lst:
        if i not in OPERATORS and i not in DIGITS:
            return False
        if lst.__len__() > lst.index(i) and i in OPERATORS and i != '-' and last_item == i:
            return False
        last_item = i
    return True


# main calc part calls bracket to store and load stack
def calc(lst):
    bracket(lst)
    while stack.__len__() > 1 or stack.__len__() == 0:
        new_list = stack.copy()
        stack.clear()
        bracket(new_list)
    final_result = stack[0]
    stack.clear()
    return str(round(float(final_result), 3))


# classify list into two lists of numbers and operators
def classify(lst):
    number_list = []
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


# do operation in correct order
def operation(number_list, operator_list):
    try:
        log_exp(number_list, operator_list)
        power(number_list, operator_list)
        mul_div(number_list, operator_list)
        add_sub(number_list, operator_list)
    except ZeroDivisionError:
        raise Exception(ZERO_DIVISION)
    except InvalidOperation:
        raise Exception(INVALID_INPUT)
    except ValueError as e:
        raise ValueError(MATHEMATICAL_ERROR)
    except Exception as e:
        raise e
    return number_list, operator_list


# store the content outside brackets and compute content inside brackets and store the result in stack
def bracket(lst):
    count = 0
    if '(' not in lst:
        number_list = classify(lst)[0]
        operator_list = classify(lst)[1]
        if stack:
            stack.pop()
        stack.append(str(operation(number_list, operator_list)[0][0]))
        if '(' in stack:
            bracket_number = stack.count('(')
            for j in range(0, bracket_number):
                stack.append(')')
        return
    else:
        i = 0
        while i < lst.__len__():
            stack.append(lst[i])
            if str(lst[i]) == '(':
                count = count + 1
                new_list = []
                i += 1
                while count != 0:
                    if str(lst[i]) == '(':
                        count += 1
                    if str(lst[i]) == ')':
                        count -= 1
                    if count == 0:
                        break
                    new_list.append(lst[i])
                    i += 1
                bracket(new_list)
            i += 1


# do log and exp calculation
def log_exp(number_list: List, operator_list: List):
    i = 0
    while i < operator_list.__len__():
        if operator_list[i] == 'l' or operator_list[i] == 'L':
            if operator_list.__len__() > i + 2 and (operator_list[i + 1] == 'o' or operator_list[i + 1] == 'O') and (
                    operator_list[i + 2] == 'g' or operator_list[i + 2] == 'G'):
                operator_list.pop(i)
                operator_list.pop(i)
                operator_list.pop(i)
                number_list.pop(i)
                number_list.pop(i)
                number_list.pop(i)
                if number_list[i] is None or number_list[i] == '':
                    raise ValueError("Invalid Input: log has no arguments given")
                if float(number_list[i]) <= 0.0:
                    raise ValueError(MATHEMATICAL_ERROR)
                number_list[i] = math.log(float(number_list[i]))
            else:
                raise Exception(INVALID_INPUT)
            i -= 1
        elif operator_list[i] == 'e' or operator_list[i] == 'E':
            if operator_list.__len__() > i + 2 and (operator_list[i + 1] == 'x' or operator_list[i + 1] == 'X') and (
                    operator_list[i + 2] == 'p' or operator_list[i + 2] == 'P'):
                operator_list.pop(i)
                operator_list.pop(i)
                operator_list.pop(i)
                number_list.pop(i)
                number_list.pop(i)
                number_list.pop(i)
                number = number_list[i]
                if operator_list.__len__() > i and operator_list[i] == '-' and number == '':
                    operator_list.pop(i)
                    number = '-' + number_list[i + 1]
                    number_list.pop(i)
                number_list[i] = Decimal(str(math.exp(float(number))))
            else:
                raise Exception(INVALID_INPUT)
            i -= 1
        elif operator_list[i] == 'o' or operator_list[i] == 'g' or operator_list[i] == 'x' or operator_list[i] == 'p':
            raise Exception(INVALID_INPUT)
        i += 1


# do power calculation
def power(number_list: List, operator_list: List):
    i = 0
    while i < operator_list.__len__():
        if operator_list[i] == '^':
            number1 = number_list[i]
            number2 = number_list[i + 1]
            if operator_list.__len__() > i + 1 and operator_list[i + 1] == '-' and number2 == '':
                operator_list.pop(i + 1)
                number2 = '-' + number_list[i + 2]
                number_list.pop(i + 1)
            result = Decimal(number1) ** Decimal(number2)
            operator_list.pop(i)
            number_list.pop(i)
            number_list.pop(i)
            number_list.insert(i, result)
            i -= 1
        i += 1


# do multiply and division calculation
def mul_div(number_list: List, operator_list: List):
    i = 0
    while i < operator_list.__len__():
        if operator_list[i] == '*' or operator_list[i] == '/':
            number1 = number_list[i]
            number2 = number_list[i + 1]
            if operator_list.__len__() > i + 1 and operator_list[i + 1] == '-' and number2 == '':
                operator_list.pop(i + 1)
                number2 = '-' + number_list[i + 2]
                number_list.pop(i + 1)
            if operator_list[i] == '*':
                result = Decimal(number1) * Decimal(number2)
            elif operator_list[i] == '/':
                result = Decimal(number1) / Decimal(number2)
            operator_list.pop(i)
            number_list.pop(i)
            number_list.pop(i)
            number_list.insert(i, result)
            i -= 1
        i += 1


# do addition and subtraction calculation
def add_sub(number_list: List, operator_list: List):
    i = 0
    while i < operator_list.__len__():
        if operator_list[i] == '+' or operator_list[i] == '-':
            number1 = number_list[i]
            number2 = number_list[i + 1]
            if operator_list.__len__() > i + 1 and operator_list[i + 1] == '-' and number2 == '':
                operator_list.pop(i + 1)
                number2 = '-' + number_list[i + 2]
                number_list.pop(i + 1)
            if operator_list[i] == '+':
                result = Decimal(number1) + Decimal(number2)
            elif operator_list[i] == '-':
                if number1 == "":
                    number1 = '0'
                result = Decimal(number1) - Decimal(number2)
            operator_list.pop(i)
            number_list.pop(i)
            number_list.pop(i)
            number_list.insert(i, result)
            i -= 1
        i += 1


# check if is operator
def is_operator(op):
    last_op = ''
    for i in op:
        if i not in OPERATORS:
            return False
        if op.__len__() > op.index(i)  and i != '-' and last_op == i:
            return False
        last_op = i
    return True


# remove whitespace in a string
def remove_whitespace(sequence: str):
    return sequence.replace(" ", "")


def calculate(sequence):
    try:
        sequence = remove_whitespace((sequence))
        lst = list(sequence)
        if is_valid(lst):
            result = calc(lst)
            return round(float(result), 5)
        return ERROR_INPUT
    except Exception as e:
        return e

"""
# user input and result output
if __name__ == '__main__':
    while True:
        sequence = input(WELCOME)
        sequence = remove_whitespace((sequence))
        print(sequence)
        lst = list(sequence)
        if sequence == 'q':
            break
        elif is_valid(lst):
            result = calc(lst)
            stack.clear()
            print("The result for", sequence, "is", "%.3f" % float(result))
        else:
            sys.exit(ERROR_INPUT)"""