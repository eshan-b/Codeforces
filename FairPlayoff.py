for _ in range(int(input())):
    arr = list(map(int, input().split()))

    # finalists
    m1 = max(arr[0], arr[1])
    m2 = max(arr[2], arr[3])

    # real max(es)
    arr.sort()

    print("YES" if {m1, m2} == {arr[2], arr[3]} else "NO")
