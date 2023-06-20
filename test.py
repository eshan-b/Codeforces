arr = [100, 101, 102, 105]
arr_sum, arr_max = 0, arr[0]

for x, num in enumerate(arr):
    arr_sum += num  # calc sum (all num)

    if (num > arr_max) and (x < 3):
        arr_max = num

print(arr_sum, arr_max)
