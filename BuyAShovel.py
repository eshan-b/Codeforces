n, k = map(int, input().split())
curr = 1

while True:
    if (n * curr) % 10 == 0 or (n * curr) % 10 == k:
        print(curr)
        break
    curr += 1
