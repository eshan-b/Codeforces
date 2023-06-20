m_win, c_win = 0, 0

for _ in range(int(input())):
    m, c = map(int, input().split())
    if m > c:
        m_win += 1
    elif m < c:
        c_win += 1

print("Mishka" if m_win > c_win else (
    "Chris" if m_win < c_win else "Friendship is magic!^^"))
