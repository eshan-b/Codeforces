for cases in range(int(input())):
    length = int(input())
    arr = list(map(int, input().split()))

    shift_even, shift_odd = 0, 0
    for index, num in enumerate(arr):
        if (index % 2 != num % 2):  # if an even or odd is out of place
            if (num % 2 == 0):
                shift_even += 1
            else:
                shift_odd += 1

    if (shift_even != shift_odd):
        print(-1)
    else:
        print(shift_even)
