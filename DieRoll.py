from fractions import Fraction

a, b = map(int, input().split())
m = max(a, b)
num = 6 - m + 1
frac = Fraction(num / 6).limit_denominator()
print(f"{frac.numerator}/{frac.denominator}")
