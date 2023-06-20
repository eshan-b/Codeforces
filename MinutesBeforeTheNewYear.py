for _ in range(int(input())):
    hr, min = map(int, input().split())
    print((23 - hr) * 60 + (60 - min))
