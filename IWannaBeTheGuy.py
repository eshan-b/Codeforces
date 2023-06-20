lvls = int(input())
expected = [(x + 1) for x in range(lvls)]

p_lvls = list(map(int, input().split()))[1:]
q_lvls = list(map(int, input().split()))[1:]

actual = list(set(p_lvls + q_lvls))

print("I become the guy." if actual == expected else "Oh, my keyboard!")
