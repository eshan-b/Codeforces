n = int(input())
cards = list(map(int, input().split()))
sereja = dima = 0

turn = True  # sereja turn
for _ in range(n):
    left = cards[0]
    right = cards[-1]
    curr = max(left, right)

    if turn:
        sereja += curr
        cards.remove(curr)
        turn = False
    else:
        dima += curr
        cards.remove(curr)
        turn = True

print(sereja, dima)
