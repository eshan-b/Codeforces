n = int(input())
two_cnt = n // 2
three_cnt = 0

if n - (two_cnt * 2) == 1:
    two_cnt -= 1
    three_cnt += 1

print(two_cnt + three_cnt)
if three_cnt:
    print('2 '*two_cnt + '3')
else:
    print('2 '*two_cnt)
