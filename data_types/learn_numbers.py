from decimal import Decimal
from fractions import Fraction
from math import floor, ceil, pi
from random import randint, seed

seed(101)

def lesson_5():
    # age = 1000000000000000000000000000000000000000

    # print(type(age))

    # age = int('111', 2)

    # 2 / 0

    age = 1.0
    my_inf = float('inf')
    print(age, type(age))

    print('the end')

    # eps = 0.0000001
    eps = 1e-6

    a = 0.1
    b = 0.2
    c = 0.3
    print(
        abs((a + b) - c) < eps
    )

    a = Decimal('0.1')
    b = Decimal('0.2')
    c = Decimal('0.3')
    print(a + b == c)
    print(Decimal('0.1') + Decimal('0.2') == Decimal('0.3'))

    print(Fraction('0.1') + Fraction('0.2') == Fraction('0.3'))
    print(Fraction(1, 10) + Fraction(2, 10) == Fraction(3, 10))


print(type(1.0 + 5)) # convert to greater type
print(type(Decimal('1.0') + 5))


print(abs(10), abs(-10))
print(min(4, 1, -4, 2, 15), max(4, 1, -4, 2, 15), sum([4, 1, -4, 2, 15], -18))
print(round(3.141593, 3), floor(3.141593), ceil(3.141593))
print(pi)

print(randint(5, 10), randint(5, 10), randint(5, 10))