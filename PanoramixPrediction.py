# sieve of erathosthenes
limit = 55
prime = [True for _ in range(limit + 1)]
prime[0] = prime[1] = False

for x in range(2, int(limit ** 0.5) + 1):
    for y in range(x * 2, limit + 1, x):
        prime[y] = False

arr = []
for index, val in enumerate(prime):
    if val:
        arr.append(index)


n, m = map(int, input().split())
print("YES" if arr[arr.index(n) + 1] == m else "NO")
