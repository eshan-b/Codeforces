a = list(map(int, input().split()))
b = input()
sum = 0

for num in b:
    sum += a[int(num) - 1]

print(sum)
