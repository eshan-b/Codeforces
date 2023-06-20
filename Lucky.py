for cases in range(int(input())):
    arr = [int(x) for x in input()]
    print("YES" if sum(arr[0:3]) == sum(arr[3:6]) else "NO")
