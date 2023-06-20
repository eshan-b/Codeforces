word = input()
word_list = list(word)
cnt = 0

for char in word_list:
    if char.isupper():
        cnt += 1

print(word.upper() if (cnt > len(word) - cnt) else word.lower())
