n = int(input())
bills = [100, 20, 10, 5, 1]
cnt = 0

for bill in bills:
    temp = n // bill
    cnt += temp
    n -= temp * bill

print(cnt)
