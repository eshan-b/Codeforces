n = int(input())
cnt = 1
prev = input()

for _ in range(n - 1):
    curr = input()

    if curr != prev:
        cnt += 1

    prev = curr

print(cnt)
