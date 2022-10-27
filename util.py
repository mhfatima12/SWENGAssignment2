import math as math


# isNumber takes a string c and checks if the given string is a float or integer.
def isNumber(c: str):
    for i in range(len(c)):
        if not (str.isnumeric(c[i]) or c[i] == '.'):
            return False
    return True


operators = ['+', '-', '/', '*', '^']


# isOperator checks if the given string is an operator.
def isOperator(c: str):
    if len(c) != 1:
        return False

    for i in range(len(operators)):
        if c == operators[i]:
            return True
    return False


# perform takes an operaton and returns the output of this operation.
def perform(val1: float | int, op: str | int, val2: float | int):
    match op:
        case '+':
            return val1 + val2
        case '-':
            return val1 - val2
        case '*':
            return val1 * val2
        case '/':
            if val2 == 0.0:
                return "divide by zero"
            return val1 / val2
        case '^':
            return math.pow(val1, val2)
    return "could not perform operation: " + str(val1) + op + str(val2)
