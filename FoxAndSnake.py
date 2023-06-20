rows, columns = map(int, input().split())
isRight = True

for row in range(rows):
    if row & 1 == 0:
        print("#" * columns)
    else:
        if isRight:
            print("." * (columns - 1) + "#")
            isRight = False
        else:
            print("#" + "." * (columns - 1))
            isRight = True
