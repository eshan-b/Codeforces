for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    max = min = arr[0]

    for num in arr:
        if num > max:
            max = num
        if num < min:
            min = num

    print(max - min)
