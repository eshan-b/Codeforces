n = int(input())
seq = list(input())
cnt = 0

for x in range(1, n):
    if seq[x - 1] == seq[x]:
        cnt += 1

print(cnt)
