n = int(input())
for _ in range(n):
    curr = int(input())
    print(int((curr / 2) - 1) if curr & 1 == 0 else int(curr / 2))
