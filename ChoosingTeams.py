n, k = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for num in arr:
    if k + num <= 5:
        cnt += 1

print(cnt // 3)
