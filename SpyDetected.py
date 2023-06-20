for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    is_found = False

    for x in range(1, n - 1):
        if (arr[x] != arr[x + 1]) and (arr[x] != arr[x - 1]):
            print(x + 1)
            is_found = True
            break

    if not is_found:
        print(1 if arr[0] != arr[1] else n)
