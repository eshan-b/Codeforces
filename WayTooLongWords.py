words = [input() for _ in range(int(input()))]
words = [word[0] + str(len(word) - 2) + word[-1]
         if (len(word) > 10) else word for word in words]
print(*words, sep="\n")
