n = int(input())
hate, love = "I hate ", "I love "
ans = ""

for x in range(n):
    if (x & 1 == 0):
        ans += hate
    else:
        ans += love
    if (x != n - 1):
        ans += "that "

ans += "it"

print(ans)
