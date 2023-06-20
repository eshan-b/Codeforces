arr = list(map(int, input().split()))
size = len(arr)
print(size - len(set(arr)))
