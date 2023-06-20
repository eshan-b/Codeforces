for cases in range(int(input())):
    length = int(input())
    days = list(input())
    new = days.copy()

    for x in range(length - 1):
        if (days[x] == days[x + 1]):
            new.remove(days[x + 1])

    print("YES" if len(new) == len(set(new)) else "NO")
