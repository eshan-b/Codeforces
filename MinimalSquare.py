for _ in range(int(input())):
    a, b = map(int, input().split())
    print(min(max(a * 2, b), max(a, b * 2)) ** 2)
