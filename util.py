import math as math
import sys


# isNumber takes a string c and checks if the given string is a float or integer.
def isNumber(c: str):
    for i in range(len(c)):
        if not (str.isnumeric(c[i]) or c[i] == '.'):
            return False
    return True


OP = ['+', '-', '/', '*', '^', 'log', 'exp']


# isOperator checks if the given string is an operator.
def isOperator(c: str):
    c = c.lower()

    for i in range(len(OP)):
        if c == OP[i]:
            return True
    return False


# perform takes an operaton and returns the output of this operation.
def perform(val1: float | int, op: str | int, val2: float | int = sys.float_info.min):
    op = op.lower()
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
        case 'log':
            return math.log(val1)
        case 'exp':
            return math.exp(val1)
    return "could not perform operation: " + str(val1) + op + str(val2)
