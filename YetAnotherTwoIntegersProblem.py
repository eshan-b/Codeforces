for cases in range(int(input())):
    a, b = map(int, input().split())
    diff = abs(a - b)

    tens = diff // 10
    extra = diff % 10

    if extra > 0:
        tens += 1

    print(tens)
