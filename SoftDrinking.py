friends, bottles, liters, limes, slices, salt, nl, np = map(
    int, input().split())
arr = [(bottles * liters) // nl, limes * slices, salt // np]
print(min(arr) // friends)
