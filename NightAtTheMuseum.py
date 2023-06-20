str = input()
ans = 0
prev = ord('a')

for char in str:
    # find current distance from [char -> prev]
    curr_dist = abs(ord(char) - prev)

    # rotate CW or CCW
    if curr_dist > 13:
        ans += 26 - curr_dist
    else:
        ans += curr_dist

    # update to new character position
    prev = ord(char)

print(ans)
