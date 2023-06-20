str = input()
print(0 if str == "{}" else len(set((str[1:-1]).split(', '))))
