r, c = map(int, input().split())
is_color = False

for _ in range(r):
    line = input().split()
    for color in line:
        if color not in ('W', 'G', 'B'):
            is_color = True
            break

print("#Color" if is_color else "#Black&White")
