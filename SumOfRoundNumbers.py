for cases in range(int(input())):
    num = input()

    place_values = []
    for index, x in enumerate(num):
        if x != '0':
            place_values.append(int(x) * (10 ** ((len(num) - 1) - index)))

    print(len(place_values))
    print(*place_values)
