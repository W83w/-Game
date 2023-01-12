import decimal
import fractions
from fractions import Fraction
from decimal import Decimal

print(1/3)
A = (2/3) + (1/2)
print(A)
A = decimal.Decimal('3.141')
A = A + 1
print('Decimal 3.141 + 1 =', A)
A = decimal.getcontext().prec = 2
print("getcontext", A)
decimal.Decimal('1.00')/decimal.Decimal('3.00')
from fractions import Fraction
F = Fraction(2,3)
F = F + 1
print('fraction 2,3 + 1 = ',F)
F = F + Fraction(1 + 21)
print('1 + 21 = ', F)
F = 1 > 2, 1 < 2
print(F)
F = bool("spam")
print(F)
X = None
X = [None] * 2

print(X)
Y = type(X)
print(Y)

if type(X) == list:
    print("Yes")
A = decimal.Decimal(1)/decimal.Decimal(7)
print(A)
decimal.getcontext().prec = 4
A = decimal.Decimal(1)/decimal.Decimal(7)
print(A)
A = decimal.Decimal(0.1) + decimal.Decimal(0.1) + decimal.Decimal(0.1) - decimal.Decimal(0.3)
print(A)
pay = decimal.Decimal(str(1999 + 1.33))
print(str(pay))
A = decimal.Decimal('1.00')/decimal.Decimal('3.00')
print(A)
with decimal.localcontext() as B:
    B.prec = 2
    C = decimal.Decimal('1.00') / decimal.Decimal('3.00')
    print(C)

decimal.getcontext().prec = 2
C = Decimal(1)/Decimal(3)
print("Decimal:", C)

C = decimal.Decimal(str(1/3)) + decimal.Decimal(str(6/12))
print('Decimal 1/3 + 6/12', C)



x = Fraction(1, 3)
y = Fraction(4, 6)
c = x - y
c = x + y
c = x ** y
print('Fractions 1 3 / 4 6 = ', C)

C = fractions.Fraction(1, 10) + fractions.Fraction(1, 10) + fractions.Fraction(1, 10) - fractions.Fraction(3, 10)
print(C)
C = Fraction.from_float(1.75)
print('float', C)

