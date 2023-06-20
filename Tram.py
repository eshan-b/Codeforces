from cmath import inf


n = int(input())
max, curr = 0, 0

for _ in range(n):
    outflow, inflow = map(int, input().split())

    curr -= outflow
    curr += inflow

    if max < curr:
        max = curr

print(max)
