n = int(input())
arr = list(map(int, input().split()))

minIndex = maxIndex = 0
min = max = arr[0]

for x in range(1, n):
    if arr[x] < min:
        min = arr[x]
        minIndex = x
    if arr[x] > max:
        max = arr[x]
        maxIndex = x

ans = maxIndex + (n - (minIndex + 1)) - (1 if minIndex < maxIndex else 0)
print(ans)
