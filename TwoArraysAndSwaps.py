for _ in range(int(input())):
    n, swaps = map(int, input().split())

    a = list(map(int, input().split()))
    a.sort()

    b = list(map(int, input().split()))
    b.sort(reverse=True)

    for x in range(n):
        if swaps <= 0:
            break

        if b[x] > a[x]:
            a[x], b[x] = b[x], a[x]
            swaps -= 1

    print(sum(a))
