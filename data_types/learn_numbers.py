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


from decimal import Decimal

a = Decimal('0.1')
b = Decimal('0.2')
c = Decimal('0.3')
print(a + b == c)
print(Decimal('0.1') + Decimal('0.2') == Decimal('0.3'))


from fractions import Fraction
print(Fraction('0.1') + Fraction('0.2') == Fraction('0.3'))
print(Fraction(1, 10) + Fraction(2, 10) == Fraction(3, 10))