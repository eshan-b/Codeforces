for _ in range(int(input())):
    nums = list(map(int, input().split()))
    nums.sort()
    print("YES" if (nums[0] + nums[1] == nums[2]) else "NO")
