n = int(input())
students = list(map(int, input().split()))
programming, math, pe = [], [], []

for index, student in enumerate(students):
    if student == 1:
        programming.append(index)
    elif student == 2:
        math.append(index)
    else:
        pe.append(index)

if programming and math and pe:
    teams = min(len(programming), len(math), len(pe))
    print(teams)

    for team in range(teams):
        print(programming[team] + 1, end=" ")
        print(math[team] + 1, end=" ")
        print(pe[team] + 1)
else:
    print(0)
