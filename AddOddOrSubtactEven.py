for _ in range(int(input())):
    a, b = map(int, input().split())
    diff = b - a
    ans = 1

    if diff == 0:           # base case
        ans = 0
    elif diff < 0:          # negative (even case)
        if diff % 2 != 0:
            ans += 1
    else:                   # positive (odd case)
        if diff % 2 == 0:
            ans += 1

    print(ans)
