for _ in range(int(input())):
    apt, x = map(int, input().split())
    curr_apt = 2
    floor = 1

    while (curr_apt < apt):
        curr_apt += x
        floor += 1

    print(floor)
