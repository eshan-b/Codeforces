cost, balance, num = map(int, input().split())
# arithmetic series: k(w * (w + 1)/2))
total = cost * ((num * (num + 1)) // 2)
print(total - balance if total > balance else 0)
