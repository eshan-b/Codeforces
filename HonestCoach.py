for cases in range(int(input())):
    n = int(input())
    athletes = sorted(list(map(int, input().split())))

    # finding smallest difference
    min_diff = athletes[-1]  # largest num in list
    for x in range(n - 1):
        curr_diff = athletes[x + 1] - athletes[x]

        if curr_diff < min_diff:
            min_diff = curr_diff

    print(min_diff)
