num = list(input())
cnt = 0

for digit in num:
    if digit == '4' or digit == '7':
        cnt += 1

print("YES" if (cnt == 4 or cnt == 7) else "NO")
