for _ in range(int(input())):
    index = int(input())
    curr = 0

    for num in range(1, 1667):
        if (num % 3 != 0) and (num % 10 != 3):
            curr += 1

            if curr == index:
                print(num)
                break
