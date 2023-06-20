name = "Timur"

for _ in range(int(input())):
    n = int(input())
    str = input()
    print("YES" if (set(str) == set(name) and len(str) == 5) else "NO")
