for cases in range(int(input())):
    rating = int(input())
    print("Division", end=" ")
    if rating < 1400:
        print("4")
    elif rating < 1600:
        print("3")
    elif rating < 1900:
        print("2")
    else:
        print("1")
