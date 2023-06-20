def solve(n):
    half = n // 2

    for x in range(1, n):
        if x < half:
            a += 2 ** x
        else:
            b += 2 ** x

    print(a - b)


for _ in range(int(input())):
    n = int(input())
    solve(n)
