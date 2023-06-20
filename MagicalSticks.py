for _ in range(int(input())):
    n = int(input())
    ans = n // 2 if not(n & 1) else n // 2 + 1
    print(ans)
