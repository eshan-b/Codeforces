for _ in range(int(input())):
    w, h, n = map(int, input().split())

    # base case
    if n == 1:
        print("YES")
        continue

    cnt = 1
    while w % 2 == 0:
        cnt *= 2
        w /= 2

    while h % 2 == 0:
        cnt *= 2
        h /= 2

    print("YES" if cnt >= n else "NO")
