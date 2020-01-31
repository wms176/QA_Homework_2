from retireClass import Retire


def test_calculate():
    test1 = Retire(21, 20000, 0.35, 500000)
    test2 = Retire(34, 57000, 0.20, 200000)
    test3 = Retire(52, 250000, 0.40, 2000000)
    test4 = Retire(29, 120000, 0.17, 450000)
    test5 = Retire(16, 15000, 0.10, 100000)
    test6 = Retire(45, 170000, 0.38, 1000000)
    test7 = Retire(12, 500, 0.10, 1000)
    test8 = Retire(37, 84000, 0.25, 650000)
    test9 = Retire(30, 48000, 0.30, 350000)
    test10 = Retire(18, 15000, 0.10, 100000)

    # I got these test values by writing an equation to find the age on paper
    # and solving each of the test cases with a calculator.
    assert test1.calculate() == 74
    assert test2.calculate() == 47
    assert test3.calculate() == 67
    assert test4.calculate() == 45
    assert test5.calculate() == 65
    assert test6.calculate() == 56
    assert test7.calculate() == 27
    assert test8.calculate() == 60
    assert test9.calculate() == 48
    assert test10.calculate() == 67
