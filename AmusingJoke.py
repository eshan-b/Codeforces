in_word = list(input() + input())
in_word.sort()
out_word = list(input())
out_word.sort()

print("YES" if in_word == out_word else "NO")
