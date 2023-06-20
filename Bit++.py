cnt = 0

for _ in range(int(input())):
    exp = input()
    if '+' in exp:
        cnt += 1
    elif '-' in exp:
        cnt -= 1

print(cnt)
