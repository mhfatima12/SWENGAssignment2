OPERATORS = ('+', '-', '*')
DIGITS = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')


def is_valid(lst):
    for i in lst:
        if i not in OPERATORS and i not in DIGITS:
            return False
    return True


def calc(lst):
    number = ''
    for i in lst:
        if is_digit(i):
            number = number + i
        else:
            number_list.append(int(number))
            operator_list.append(i)
            number = ''
    number_list.append(int(number))
    mul()
    add_sub()
    return number_list[0]


def mul():
    i = 0
    while i < operator_list.__len__():
        if operator_list[i] == '*':
            product = number_list[i] * number_list[i + 1]
            operator_list.pop(i)
            number_list.pop(i)
            number_list.pop(i)
            number_list.insert(i, product)
            i -= 1
        i += 1


def add_sub():
    for i in range(1, number_list.__len__()):
        number1 = number_list[0]
        number2 = number_list[1]
        if operator_list[0] == '+':
            result = number1 + number2
        elif operator_list[0] == '-':
            result = number1 - number2
        operator_list.pop(0)
        number_list.pop(1)
        number_list[0] = result


def is_digit(digit):
    return digit in DIGITS


while True:
    sequence = input("Please enter a sequence that you want to compute: (q to end)")
    se_lst = list(sequence)
    if sequence == 'q':
        break
    elif is_valid(se_lst):
        try:
            number_list = []
            operator_list = []
            result = calc(se_lst)
        except BaseException as e:
            print(e)
        else:
            print("The result is {0}.".format(result))
        finally:
            again = input("Would you like to have another try? y/n")
            if again == 'y':
                continue
            elif again == 'n':
                break
    else:
        print("Error:The sequence must only include operators and digits")
