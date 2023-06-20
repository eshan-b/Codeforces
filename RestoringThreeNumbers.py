arr = list(map(int, input().split()))
abc = max(arr)

for num in arr:
    if num != abc:
        print(abc - num, end=" ")
