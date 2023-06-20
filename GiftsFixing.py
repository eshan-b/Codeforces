for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    mina, minb = a[0], b[0]
    # find both min... O(n)
    for x in range(len(a)):
        if a[x] < mina:
            mina = a[x]

        if b[x] < minb:
            minb = b[x]

    ans = 0
    for x in range(len(a)):
        ans += max(a[x] - mina, b[x] - minb)

    print(ans)
