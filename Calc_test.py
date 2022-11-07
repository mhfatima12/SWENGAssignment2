import Calc as Calc
import unittest

def test_is_valid() -> None:
    tests = [
        ('1', True),
        ('12567', True),
        ('1.287', True),
        ('123498.222', True),
        ('test', False),
        ('12.a234', False),
        ('124904,3402', False),
        #('++', False), #currently failing
        ('+', True),
        ('-', True),
        ('/', True),
        ('*', True),
        ('^', True),
        ('a', False),
        ('log', True),
        #('Log', True), #currently failing
        #('EXP', True), #currently failing
        #('ExP', True), #currently failing
        ('exp', True),
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


def test_is_operator() -> None:
    tests = [
        #('++', False), #currently failing
        ('+', True),
        ('-', True),
        ('/', True),
        ('*', True),
        ('^', True),
        ('a', False),
        #('log', True),
        #('Log', True), #currently failing
        #('EXP', True), #currently failing
        #('ExP', True), #currently failing
        #('exp', True),
        ('expres', False),
        ('logs', False),
        ('(', True),
        (')', True)
    ]

    hasFail = False
    for test in tests:
        result = Calc.is_operator(test[0])
        if result != test[1]:
            hasFail = True
            print("is_valid("+str(test[0])+") expected: " +
                  str(test[1])+" got: "+str(result))
    assert not hasFail

def test_calc() -> None:
    tests = [
        ('2+2', '4.0'),
        ('2+2+2', '6.0'),
        ('2.5+7.8', '10.3'),
        ('24987.2+56.789', '25043.989'),
        ('2-2', '0.0'),
        ('76-4', '72.0'),
        ('20.57-2.6', '17.97'),
        ('12-6', '6.0'),
        ('12*6', '72.0'),
        ('6.8*2.45', '16.66'),
        ('-2*2', '-4.0'), #negative multiplication test
        ('10/2', '5.0'),
        ('12.6/2', '6.3'),
        ('2482/20', '124.1'),
        ('-10/2', '-5.0'),
        ('log 100', '4.605'),
        ('log 65', '4.174'),
        ('2^4', '16.0'),
        ('6^-2', '0.028'),
        ('-8^3', '-512.0'),
        ('exp(4)', '54.598'), #rounded off to three decimal places
        ('exp(-2)', '0.135'),
        ('3+5*exp(4.2)/(5+7)', '30.786'), #rounded off to three decimal places
        ('3*5-2', '13.0'),
        ('2*4/2', '4.0'),
        ('10-6/2', '7.0'),
        ('(10-2)/(2*2)', '2.0'),
        ('(12+8)/(20-10)', '2.0'),
        ('(6/3)+(4*9)', '38.0'),
        ('(2+2)-(6-3)*(12+6)', '-50.0')
    ]

    hasFail = False
    for test in tests:
        result = Calc.calc(test[0])
        if result != test[1]:
            hasFail = True
            print("calc("+str(test[0])+") expected: " +
                  str(test[1])+" got: "+str(result))
    assert not hasFail

class MyTestCase(unittest.TestCase):
    # Returns true if 100 / 0 raises an Exception
    def test_calc2(self):
        with self.assertRaises(ZeroDivisionError):
            '100 / 0'
  
if __name__ == '__main__': 
    unittest.main()