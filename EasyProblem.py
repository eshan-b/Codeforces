input()  # skip n
ans = "EASY"

# could use any() if casting wasn't needed
for response in input().split():
    if response == '1':
        ans = "HARD"
        break

print(ans)
