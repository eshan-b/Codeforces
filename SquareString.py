for cases in range(int(input())):
    word = input()
    if len(word) % 2 != 0:
        print("NO")
    else:
        print("YES" if word[0: len(word) // 2]
              == word[len(word) // 2:] else "NO")
