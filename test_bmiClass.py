from bmiClass import BMI


def test_calculate():
    test1 = BMI(5, 3, 125)
    test2 = BMI(6, 1, 240)
    test3 = BMI(4, 11, 100)
    test4 = BMI(9, 11, 350)
    test5 = BMI(2, 5, 80)
    test6 = BMI(7, 9, 500)
    test7 = BMI(1, 4, 30)
    test8 = BMI(3, 5, 250)
    test9 = BMI(5, 7, 130)
    test10 = BMI(6, 1, 135)

    # I got these test values from the BMI Calculator on the CDC's website
    # inputting the integers that were used in each test case above.
    assert BMI.calculate(test1) == '22.1'
    assert BMI.calculate(test2) == '31.7'
    assert BMI.calculate(test3) == '20.2'
    assert BMI.calculate(test4) == '17.4'
    assert BMI.calculate(test5) == '66.9'
    assert BMI.calculate(test6) == '40.6'
    assert BMI.calculate(test7) == '82.4'
    assert BMI.calculate(test8) == '104.6'
    assert BMI.calculate(test9) == '20.4'
    assert BMI.calculate(test10) == '17.8'
