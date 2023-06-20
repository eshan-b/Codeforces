for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    one, sum = 0, 0

    for num in arr:
        if num == 1:
            one += 1
        sum += num

    if sum & 1 != 0:
        print("NO")
    else:
        half_sum = sum // 2
        if (half_sum & 1 == 0) or (half_sum & 1 != 0 and one != 0):
            print("YES")
        else:
            print("NO")
