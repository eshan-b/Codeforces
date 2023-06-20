for _ in range(int(input())):
    num = int(input())
    new_num = (((num % 10) - 1) * 10)
    l = len(str(num))
    arr = [1, 3, 6, 10]
    new_num += arr[l - 1]
    print(new_num)
