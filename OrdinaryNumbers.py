for _ in range(int(input())):
    n = int(input())
    l = len(str(n))
    print((9 * (l - 1)) + (n // int('1' * l)))
