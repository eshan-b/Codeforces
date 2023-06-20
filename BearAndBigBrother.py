l, b = map(int, input().split())
yrs = 0

while (l <= b):
    l *= 3
    b *= 2
    yrs += 1

print(yrs)
