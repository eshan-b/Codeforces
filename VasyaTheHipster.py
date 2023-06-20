n1, n2 = map(int, input().split())
min, max = 0, 0

if n1 < n2:
    min = n1
    max = n2
else:
    min = n2
    max = n1

print(min, end=" ")
print((max - min) // 2)
