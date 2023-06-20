input()  # ignore n
arr = list(map(int, input().split()))
officers, crimes = 0, 0

for num in arr:
    if num > 0:
        officers += num
    elif num == -1:
        if officers:
            officers -= 1
        else:
            crimes += 1

print(crimes)
