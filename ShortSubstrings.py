for _ in range(int(input())):
    word = list(input())
    length = len(word)

    for x in range(0, length, 2):
        print(word[x], end="")

    if (length & 1 == 0):
        print(word[length - 1])
