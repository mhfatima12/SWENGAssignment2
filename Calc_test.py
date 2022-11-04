import Calc as Calc

def test_is_valid() -> None:
    tests = [
        ('1', True),
        ('12567', True),
        ('1.287', True),
        ('123498.222', True),
        ('test', False),
        ('12.a234', False),
        ('124904,3402', False),
        #('++', False),
        ('+', True),
        ('-', True),
        ('/', True),
        ('*', True),
        ('^', True),
        ('a', False),
        ('log', True),
        #('Log', True),
        #('EXP', True),
        #('ExP', True),
        ('expres', False),
        ('logs', False),
        ('(', True),
        (')', True)
    ]

    hasFail = False
    for test in tests:
        result = Calc.is_valid(test[0])
        if result != test[1]:
            hasFail = True
            print("is_valid("+str(test[0])+") expected: " +
                  str(test[1])+" got: "+str(result))
    assert not hasFail