for _ in range(int(input())):
    l = int(input())
    even_sum, odd_sum = 0, 0

    if l % 4 == 0:
        print("YES")

        for even in range(2, l + 1, 2):
            print(even, end=" ")
            even_sum += even

        for odd in range(1, (l - 2) + 1, 2):
            print(odd, end=" ")
            odd_sum += odd

        print(even_sum - odd_sum)
    else:
        print("NO")
