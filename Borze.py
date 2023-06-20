str = input()
x = 0

while x < len(str):
    if str[x] == '.':
        print(0, end="")
    elif str[x] == '-' and str[x + 1] == '.':
        print(1, end="")
        x += 1  # skip
    elif str[x] == '-' and str[x + 1] == '-':
        print(2, end="")
        x += 1  # skip

    x += 1
