for cases in range(int(input())):
    nums = list(map(int, input().split()))
    timur_value = nums[0]

    nums.sort(reverse=True)
    timur_place = nums.index(timur_value)

    print(timur_place)
