input()  # ignore n
nums = list(map(int, input().split()))
max = min = nums[0]
cnt = 0

for num in nums:
    if num > max:
        max = num
        cnt += 1
    if num < min:
        min = num
        cnt += 1

print(cnt)
