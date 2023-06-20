problems, commute = map(int, input().split())
time = 240 - commute
series_sum = problems * ((5 + 5 * problems) / 2)
print(series_sum)
