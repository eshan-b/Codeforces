for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    is_valid = True
    for x in range(1, n):
        if abs(arr[x] - arr[x - 1]) > 1:
            is_valid = False
            print("NO")
            break

    if is_valid:
        print("YES")
