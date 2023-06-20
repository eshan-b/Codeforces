num1, num2 = input(), input()
ans = ""

for x in range(len(num1)):
    if (num1[x] != num2[x]):
        ans += '1'
    else:
        ans += '0'

print(ans)
