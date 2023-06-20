for _ in range(int(input())):
    num = int(input())

    c1 = c2 = num // 3
    if (num % 3 == 1):
        c1 += 1
    elif (num % 3 == 2):
        c2 += 1

    print(c1, c2)
