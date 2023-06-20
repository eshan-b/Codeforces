arr = list(map(int, input().split()))
arr.sort()
med = arr[1]
print(abs(med - arr[0]) + abs(med - arr[2]))
