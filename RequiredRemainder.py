for _ in range(int(input())):
    x, y, n = map(int, input().split())
    quotient = n // x
    remainder = n % x

    if (remainder >= y):
        print(quotient * x + y)
    else:
        print((quotient - 1) * x + y)
