# k, l, m, n
a = [int(input()) for _ in range(4)]
# dragons
d = int(input())
cnt = 0

if (1 in a):
    print(d)
else:
    for x in range(1, d + 1):
        if ((x % a[0] == 0) or (x % a[1] == 0) or
                (x % a[2] == 0) or (x % a[3] == 0)):
            cnt += 1
    print(cnt)
