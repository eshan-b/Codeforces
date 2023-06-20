for _ in range(int(input())):
    arr = list(map(int, input().split()))  # a, b, c, n
    arr_sum, arr_max = 0, arr[0]

    # find max and sum at same time... O(n)
    for x, num in enumerate(arr):
        arr_sum += num  # calc sum (all num)

        if (num > arr_max) and (x < 3):  # max of first a, b, c
            arr_max = num

    print("YES" if (arr_sum % 3 == 0 and arr_sum / 3 >= arr_max) else "NO")
