cnt = 0

for _ in range(int(input())):
    occupied, capacity = map(int, input().split())
    if (capacity - occupied) >= 2:
        cnt += 1

print(cnt)
