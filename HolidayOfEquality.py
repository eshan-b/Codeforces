n = int(input())
arr = list(map(int, input().split()))
max = max(arr)
sum = 0

for num in arr:
    sum += max - num

print(sum)
