n, time = map(int, input().split())
line = list(input())

while time > 0:
    x = 0
    while x < n - 1:
        # if B G then swap to G B
        if (line[x] == 'B' and line[x + 1] == 'G'):
            line[x + 1] = 'B'
            line[x] = 'G'
            x += 2  # skip next iter
        else:
            x += 1

    time -= 1

print(*line, sep="")
