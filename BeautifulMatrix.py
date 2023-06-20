# matrix = [list(map(int, input().split())) for _ in range(5)]
num, ans = 0, 0

for x in range(5):
    row = list(map(int, input().split()))
    for y in range(5):
        if row[y] == 1:
            ans = abs(x - 2) + abs(y - 2)
            break

print(ans)
