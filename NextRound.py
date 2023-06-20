n, k = map(int, input().split())
count = 0
nums = list(map(int, input().split()))

for num in nums:
    if num >= nums[k - 1] and num > 0:
        count += 1

print(count)
