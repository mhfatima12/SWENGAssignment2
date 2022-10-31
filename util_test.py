import util as util


def test_isNumber() -> None:
    tests = [
        ('1', True),
        ('1.345', True),
        ('90857.592', True),
        ('abcd', False),
        ('13759a.039', False),
        ('124904,3402', False),
    ]

    hasFail = False
    for test in tests:
        result = util.isNumber(test[0])
        if result is not test[1]:
            hasFail = True
            print("isNumber("+test[0]+") expected: " +
                  str(test[1])+" got: "+str(result))
    assert not hasFail


def test_isOperator() -> None:
    tests = [
        ('1', False),
        ('++', False),
        ('+', True),
        ('-', True),
        ('/', True),
        ('*', True),
        ('^', True),
        ('a', False),
        ('a+c', False),
        ('log',True),
        ('Log',True),
        ('EXP',True),
        ('ExP',True),
        ('expres',False),
        ('logs',False)
    ]

    hasFail = False
    for test in tests:
        result = util.isOperator(test[0])
        if result != test[1]:
            hasFail = True
            print("isOperator("+str(test[0])+") expected: " +
                  str(test[1])+" got: "+str(result))
    assert not hasFail


def test_perform() -> None:
    tests = [
        (1, '+', 2, 3),
        (2, '-', 5, -3),
        (5, '-', 2, 3),
        (3, '^', 2, 9),
        (5, '/', 0, 'divide by zero'),
        (4, '*', 2, 8),
        (1.5, '-', 0.5, 1.0),
        (345, '***', 7, 'could not perform operation: 345***7'),
        (2, 'exp', 0,7.38905609893065),
        (2, 'exp', 10,7.38905609893065),
        (2, 'log', 0,0.6931471805599453),
        (2, 'log', 10,0.6931471805599453),
    ]

    hasFail = False
    for test in tests:
        result = util.perform(test[0], test[1], test[2])
        if result != test[3]:
            hasFail = True
            print("perform("+str(test[0])+test[1]+str(test[2])+") expected: " +
                  str(test[3])+" got: "+str(result))
    assert not hasFail
